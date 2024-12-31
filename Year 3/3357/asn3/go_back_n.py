import threading, queue, logging, time

class GBN_sender:
    def __init__(self, input_file, window_size, packet_len, nth_packet, send_queue, ack_queue, timeout_interval, logger):
        self.input_file = input_file
        self.packet_len = packet_len
        self.window_size = window_size
        self.base = 0                  # first unacknowledged packet
        self.send_queue = send_queue
        self.ack_queue = ack_queue
        self.packets = self.prepare_packets()   
        self.acks_list = [False] * len(self.packets)        # list of bools to track packages acknowledged
        self.timeout_interval = timeout_interval    # timeout period for retransmitting if no ACK
        self.packet_timers = [0] * len(self.packets)    # keeps track of timeout for each packet
        self.nth_packet = nth_packet  # rep interval of packets being dropped (every n packets sent)
        self.dropped_list = []        # stores sequence numbers of packets that have been dropped
        self.logger = logger
        self.send_count = 0

    def prepare_packets(self):
        packets = []
        seq_len = 16
        chunk_len = self.packet_len-seq_len
        
        with open(self.input_file, "r") as file:
            content = file.read()

        binary = ''.join(format(ord(char), '08b') for char in content)
        
        seq_num = 0
        for i in range(0, len(binary), chunk_len):
            chunk = binary[i : i+chunk_len]

            if len(chunk) < chunk_len:
                chunk = chunk.ljust(chunk_len, '0')
            
            seq_binary = format(seq_num, '016b')
            packet = chunk+seq_binary
            packets.append(packet)
            seq_num += 1
        
        return packets
          
    def send_packets(self):
        for i in range(self.base, min(self.base + self.window_size, len(self.packets))):
            if self.acks_list[i]:
                continue

            if self.base >= len(self.packets):
                self.logger.info("All packets sent")
                break
            
            packet = self.packets[i]
            data = packet[:self.packet_len - 16]
            seq_num = packet[-16:]
            seq_int = int(seq_num, 2)

            if i % self.nth_packet == self.nth_packet-1 and seq_int not in self.dropped_list:
                self.dropped_list.append(seq_int)
                self.logger.info(f"packet {seq_int} dropped")
            else:
                self.logger.info(f"sendingpacket{seq_int}")
                packet = data + seq_num
                self.send_queue.put_nowait(packet)
                self.packet_timers[i] = time.time()            
            
            self.logger.info(f"send_queue contents: {[packet[-16:] for packet in list(self.send_queue.queue)]}")

        return
    
    def send_next_packet(self):
        self.base+=1
        if self.base < len(self.packets) and self.acks_list[self.base]:
            lastInd = min(self.base + self.window_size-1, len(self.packets)-1)
            packet = self.packets[lastInd]
            seq_num = packet[-16:]
            seq_int = int(seq_num, 2)
            

            if lastInd % self.nth_packet == self.nth_packet-1 and seq_int not in self.dropped_list:
                self.dropped_list.append(seq_int)
                self.logger.info(f"packet {seq_int} dropped")
            else:
                self.logger.info(f"sendingpacket{seq_int}")
                self.send_queue.put_nowait(packet)
                self.packet_timers[lastInd] = time.time()

        return

    def check_timers(self):
        check_time = time.time()
        timeout = False

        for i in range(self.base, min(self.base + self.window_size, len(self.packets))):
            if not self.acks_list[i] and (check_time - self.packet_timers[i] > self.timeout_interval):
                packet = self.packets[i]
                seq_num = packet[-16:]
                seq_int = int(seq_num, 2)
                self.logger.info(f"packet {seq_int} timed out")
                timeout = True
        return timeout

    def receive_acks(self):
        while True:
            if self.base>= len(self.packets):
                break
            
            try:
                ack = self.ack_queue.get()
                packet = self.packets[ack]
                seq_num = packet[-16:]
                seq_int = int(seq_num, 2)

                if self.base <= ack and ack < len(self.packets):
                    if not self.acks_list[ack]:     # if the packet has not been acknowledged
                        self.acks_list[ack] = True
                        self.logger.info(f"ack{seq_int}received")
                        self.send_next_packet()
                        while self.base < len(self.packets) and self.acks_list[self.base]:
                            self.base += 1

                else:
                    self.logger.info(f"ack {seq_int} received, Ignoring")
            except queue.Empty:
                break
                        
    def run(self):
        self.send_packets()

        ack_thread = threading.Thread(target=self.receive_acks, daemon=True)
        ack_thread.start()
        
        while self.base < len(self.packets):
            if self.check_timers():
                for i in range(self.base, min(self.base + self.window_size, len(self.packets))):
                    if not self.acks_list[i]:
                        packet = self.packets[i]
                        seq_num = packet[-16:]
                        seq_int = int(seq_num, 2)
                        self.logger.info(f"retransmittingpacket{seq_int}")
                        
                        self.send_packets()

        self.send_queue.put(None)
            
class GBN_receiver:
    def __init__(self, output_file, send_queue, ack_queue, logger):
        self.output_file = output_file
        self.send_queue = send_queue
        self.ack_queue = ack_queue
        self.logger = logger
        self.packet_list = []
        self.expected_seq_num = 0

    def process_packet(self, packet):
        seq_num = packet[-16:]
        seq_int = int(seq_num, 2)
        expected_seq_num = format(self.expected_seq_num, '016b')
        
        if seq_num == expected_seq_num:
            self.packet_list.append(packet)
            self.ack_queue.put(seq_int)
            self.logger.info(f"packet{seq_int}received")
            self.expected_seq_num += 1
            self.send_queue.task_done()
            return True
        else:
            if self.expected_seq_num > 0:
                last_ack_rcv = self.expected_seq_num - 1
                self.ack_queue.put(last_ack_rcv)
                self.logger.info(f"packet{seq_int}receivedoutoforder")
                return False
            self.send_queue.task_done()

    
    def write_to_file(self):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            for packet in self.packet_list:
                data = packet[:-16]
                conv_data = ''.join(chr(int(data[i : i+8], 2)) for i in range(0, len(data), 8))
                file.write(conv_data)
        return

    def run(self):
        while True:
            packet = self.send_queue.get()

            if packet is None:
                self.send_queue.task_done()
                break
            
            self.process_packet(packet)
        
        self.write_to_file()
        return