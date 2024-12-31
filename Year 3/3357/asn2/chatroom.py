import socket
import threading

class ServerTCP:
    def __init__(self, server_port):
        self.server_port = server_port     #port # for which server will listen for messages
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', self.server_port))
        print(f"TCP CHATROOM\nThis is the server side.\nI am ready to receive connections on port {server_port}\nPress CTRL+C to shut down the server.\nWaiting for clients to connect...\n\n")
        self.server_socket.listen()
        self.server_socket.settimeout(5)
        self.clients = {}
        self.run_event = threading.Event()
        self.handle_event = threading.Event()

    def accept_client(self):
        try:
            client_socket, client_address = self.server_socket.accept()
            client_socket.settimeout(5)
            name = client_socket.recv(1024).decode('utf-8')

            if name in self.clients.values():
                client_socket.send(b"Name already taken.")
                self.close_client(client_socket)
                return False
            
            else:
                client_socket.send(b"Welcome!")
                self.clients[client_socket] = name
                self.broadcast(client_socket, "join")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
                return True
        except socket.timeout:
            print("Waiting for a client connection timed out.")
            return False
        except Exception as e:
            print(f"An error occurred in ServerTCP: {e}")
            return False
            

    def close_client(self, client_socket):
        try:
            if client_socket in self.clients.keys():
                name = self.clients[client_socket]
                del self.clients[client_socket]
                try:
                    client_socket.close()
                    print(f"Closed connection for {name}.")
                    return True
                except Exception as e:
                    print(f"An error occurred while closing the client socket: {e}")
                    return False
        except KeyError:
            return False

    def broadcast(self, client_socket_sent, message):
        x = self.clients.get(client_socket_sent, "Unknown")
        if message == "join":
            broadMessage = f"User {x} joined"
            print(broadMessage)
        elif message == "exit":
            broadMessage = f"User {x} left"
            print(broadMessage)
        else:
            broadMessage = f"{x}: {message}"
        
        for client in self.clients.keys():
            if client != client_socket_sent:
                try:
                    client.send(broadMessage.encode('utf-8')) 
                except Exception as e:
                    print(f"An error occurred in ServerTCP broadcast: {e}")

    def shutdown(self):
        for client in self.clients.keys():
            try: 
                client.send(b"server-shutdown")
                self.close_client(client)
            except Exception as e:
                print(f"Error sending shutdown message in ServerTCP: {e}.")
        
        self.run_event.set()        #set to stop
        self.handle_event.set()     #set to stop
        self.server_socket.close()
        print("Server has been shut down.")

    def get_clients_number(self):
        return len(self.clients)
    
    def handle_client(self, client_socket):
        try:
            while not self.handle_event.is_set():
                request = client_socket.recv(4096).decode('utf-8')
                if request=="exit":
                    self.broadcast(client_socket, "exit")
                    self.close_client(client_socket)
                    break
                self.broadcast(client_socket, request)
        except socket.timeout:
            print("No data received from the client; continuing.")
        except Exception as e:
            print(f"An error occurred in ServerTCP handle_client: {e}")
        finally:
            self.close_client(client_socket)

    def run(self):
        try:
            while not self.run_event.is_set():
                self.accept_client()
        except KeyboardInterrupt:
            print("A Keyboard Interrupt error has occurred in ServerTCP run.")
            self.shutdown()
        except Exception as e:
            print(f"An error occurred in ServerTCP handle_client: {e}")
            self.shutdown()

class ClientTCP:
    def __init__(self, client_name, server_port):
        self.server_addr = "localhost"
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_name = client_name
        print(f"TCP CHATROOM\nThis is the client side.")
        self.exit_run = threading.Event()
        self.exit_receive = threading.Event()
        
    def connect_server(self):
        try:
            self.client_socket.connect((self.server_addr,self.server_port))

            self.send(self.client_name)
            response = self.client_socket.recv(4096).decode('utf-8')

            if "Welcome" in response:
                print(response)
                return True
            else:
                print(response)
                return False
        except Exception as e:
            print(f"Error has occurred in Client TCP connect_server: {e}")

    def send(self, text):
        self.client_socket.send(text.encode('utf-8'))

    def receive(self):
        while not self.exit_receive.is_set():
            try:
                response = self.client_socket.recv(4096).decode('utf-8')

                if "server-shutdown" in response:
                    print("Server shutting down.")
                    self.exit_run.set()
                    self.exit_receive.set()
                    break
                else:
                    print(f"{response}")
            except Exception as e:
                print(f"An error occurred in ClientTCP receive: {e}")

        
    def run(self):
        try:
            if self.connect_server():
                print('You are now connected to the chatroom.\nType "exit" to leave the chatroom.')

                recThread = threading.Thread(target=self.receive)
                recThread.start()

                while not self.exit_run.is_set():
                    message = input(f"{self.client_name}: ")

                    if message.lower()=="exit":
                        self.send("exit")
                        self.exit_run.set()
                        self.exit_receive.set()
                        break
                    else: 
                        self.send(message)
                    
                recThread.join()
        except KeyboardInterrupt:
            self.send("exit")
            self.exit_receive.set()
        finally:
            self.client_socket.close()

class ServerUDP:
    def __init__(self, server_port):
        self.server_port = server_port
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.server_socket.bind(('localhost',self.server_port))
        self.clients = {}
        self.messages = []  #in tuples, client_addr: message content
        print(f"UDP CHATROOM\nThis is the server side.\nI am ready to receive connections on port {server_port}\nPress CTRL+C to shut down the server.\nWaiting for clients to connect...\n\n")

    def accept_client(self, client_addr, message):
        client_name = message.split(":",1)[0]

        if client_name in self.clients.values():
            self.server_socket.sendto(b"Name already taken.", client_addr)
            return False
        
        self.server_socket.sendto(b"Welcome!", client_addr)
        self.clients[client_addr] = client_name
        self.messages.append((client_addr,f"User {client_name} joined"))
        self.broadcast()
        return True
    
    def close_client(self, client_addr):
        if client_addr in self.clients:
            client_name = self.clients[client_addr]
            del self.clients[client_addr]
            self.messages.append((client_addr,f"User {client_name} left"))
            self.broadcast()
            return True
        return False
        
    def broadcast(self):
        if self.messages:
            addr, broadMessage = self.messages[-1]
            for client in self.clients:
                if client != addr:
                    try:
                        self.server_socket.sendto(broadMessage.encode('utf-8'),client)
                    except Exception as e:
                        print(f"Error occurred in ServerUDP broadcast: {e}")

    def shutdown(self):
        try:
            clients_list = list(self.clients.keys())
            for client in clients_list:
                self.server_socket.sendto(b"server-shutdown",client)
                self.close_client(client)
            
            self.server_socket.close()
            print("Server has been shut down.")
        except Exception as e:
            print(f"Error occurred in ServerUDP shutdown: {e}")

    def get_clients_number(self):
        return len(self.clients)
    
    def run(self):
        try:
            while True:
                message, addr = self.server_socket.recvfrom(4096)
                message = message.decode('utf-8')

                if not message.strip():
                    continue

                name = message.split(":",1)[0]
                request = message.split(":",1)[1]

                if request.lower()=="join":
                    self.accept_client(addr, message)
                    print(f"User {name} joined")
                elif request.lower()=="exit":
                    if self.close_client(addr):
                        print(f"User {name} left")
                else:
                    if addr in self.clients:
                        self.messages.append((addr, f"{name}: {request}"))
                        self.broadcast()
        except KeyboardInterrupt:
            print(f"Server shutting down.")
            self.shutdown()
        except Exception as e:
            print(f"Error occurred in ServerUDP run: {e}")
            self.shutdown()

class ClientUDP:
    def __init__(self, client_name, server_port):
        self.server_addr = 'localhost'
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_name = client_name
        print(f"UDP CHATROOM\nThis is the client side.")
        self.exit_run = threading.Event()
        self.exit_receive = threading.Event()

    def connect_server(self):
        try:
            self.send("join")
            response, addr = self.client_socket.recvfrom(4096)
            response = response.decode('utf-8')
            if "Welcome" in response:
                print(response)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error has occurred in Client UDP connect_server: {e}")

    def send(self, text):
        self.client_socket.sendto(f"{self.client_name}:{text}".encode('utf-8'),(self.server_addr,self.server_port))
        
    def receive(self):
        while not self.exit_receive.is_set():
            try:
                response, _ = self.client_socket.recvfrom(4096)
                response = response.decode('utf-8')

                if "server-shutdown" in response:
                    print("Server shutting down.")
                    self.exit_run.set()
                    self.exit_receive.set()
                    break
                else:
                    print(f"{response}")
            except Exception as e:
                print(f"An error occurred in ClientUDP receive: {e}")
        
    def run(self):
        try:
            if self.connect_server():
                print('You are now connected to the chatroom.\nType "exit" to leave the chatroom.')

                recThread = threading.Thread(target=self.receive)
                recThread.start()

                while not self.exit_run.is_set():
                    message = input(f"{self.client_name}: ")

                    if message.lower()=="exit":
                        self.send("exit")
                        self.exit_run.set()
                        self.exit_receive.set()
                        break
                    elif message=="":
                        continue
                    else: 
                        self.send(message)
                    
                recThread.join()
        except KeyboardInterrupt:
            self.send("exit")
            self.exit_receive.set()
        finally:
            self.client_socket.close()