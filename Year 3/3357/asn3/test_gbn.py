from go_back_n import GBN_sender, GBN_receiver
import threading, queue, logging, time
log_file = 'simulation.log'
in_file = 'input_test.txt'
out_file = 'output_test.txt'


window_size = 4
packet_len = 32
nth_packet = 19
timeout_interval = 1

with open(in_file, 'w') as f: 
    f.write("Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World World HelloWorld")

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file, 'w')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(file_handler)

send_queue, ack_queue = queue.Queue(), queue.Queue()
sender = GBN_sender(input_file = in_file, window_size = window_size, packet_len = packet_len, nth_packet = nth_packet, send_queue = send_queue, ack_queue = ack_queue, timeout_interval = timeout_interval, logger = logger)
receiver = GBN_receiver(output_file = out_file, send_queue = send_queue, ack_queue = ack_queue, logger = logger)

sender_thread = threading.Thread(target=sender.run) 
sender_thread.start() 
receiver.run() 
sender_thread.join() 

with open(log_file, 'r') as log:
    log_content = log.read()
    assert "packet 19 dropped" in log_content, "Expected 'packet 19 dropped' log not found"
    assert "ack 18 received, Ignoring" in log_content, "Expected 'ack 18 received, Ignoring' log not found"
    assert "packet 19 timed out" in log_content, "Expected 'packet 19 timed out' log not found"

print("Gradescope-aligned Test Passed")

def test_basic_transmission():
    # Start sender and receiver threads
    sender_thread = threading.Thread(target=sender.run)
    sender_thread.start()
    receiver.run()  # Run receiver in the main thread
    
    sender_thread.join()  # Wait for sender thread to complete

    # Check if sent and received data match
    with open(in_file, 'r') as f1, open(out_file, 'r') as f2:
        sent, received = f1.read(), f2.read()
    
    assert sent == received, f"Data mismatch: Sent {sent}, Received {received}"
    print("Basic Transmission Test Passed")

# --- TEST 2: Timeout and retransmission test ---
def test_timeout_and_retransmission():
    sender_thread = threading.Thread(target=sender.run)
    sender_thread.start()
    
    # Allow some packets to be sent and check timeout
    time.sleep(2 * timeout_interval)  # Adaptive wait based on timeout_interval

    sender_thread.join()

    with open(log_file, 'r') as log:
        log_content = log.read()
        assert "packet 19 timed out" in log_content, "Expected timeout log not found for packet 19"
    
    print("Timeout and Retransmission Test Passed")

# --- Adjusted Packet Dropping Test ---
def test_packet_dropping():
    # Configure nth_packet to trigger a drop at packet 19
    sender.nth_packet = 19

    sender_thread = threading.Thread(target=sender.run)
    receiver_thread = threading.Thread(target=receiver.run)

    sender_thread.start()
    receiver_thread.start()
    
    sender_thread.join()
    receiver_thread.join()
    
    # Check for the exact drop log for packet 19
    with open(log_file, 'r') as log:
        log_content = log.read()
        assert "packet 19 dropped" in log_content, "Packet 19 drop not logged as expected"
    
    print("Packet Dropping Test Passed")

# --- TEST 4: Sliding Window test ---
def test_sliding_window_behavior():
    # Test sliding window behavior by starting with a larger window size
    window_size = 4  # 4 packets in the window
    sender = GBN_sender(
        input_file=in_file,
        window_size=window_size,
        packet_len=packet_len,
        nth_packet=1,
        send_queue=send_queue,
        ack_queue=ack_queue,
        timeout_interval=timeout_interval,
        logger=logger
    )

    sender_thread = threading.Thread(target=sender.run)
    sender_thread.start()
    
    # Sleep to allow the window to slide
    time.sleep(1)  # Allow some time for the sender to send and the receiver to process

    # Check if window moves forward (check logs for sliding window activity)
    sender_thread.join()
    
    with open(log_file, 'r') as log:
        log_content = log.read()
        assert "sendingpacket" in log_content, "Sliding window did not move as expected"
    
    print("Sliding Window Behavior Test Passed")

# --- TEST 5: End-to-End Simulation ---
def test_end_to_end_simulation():
    # Full test with all aspects: basic transmission, timeout, retransmission, dropping
    sender_thread = threading.Thread(target=sender.run)
    sender_thread.start()
    receiver.run()
    
    sender_thread.join()
    
    # Check if the data sent matches the data received
    with open(in_file, 'r') as f1, open(out_file, 'r') as f2:
        sent, received = f1.read(), f2.read()
    
    assert sent == received, f"Data mismatch: Sent {sent}, Received {received}"
    print("End-to-End Simulation Test Passed")

# Run all tests
test_basic_transmission()
test_timeout_and_retransmission()
test_packet_dropping()
test_sliding_window_behavior()
test_end_to_end_simulation()