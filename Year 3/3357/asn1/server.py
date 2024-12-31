import socket
import threading
import time

class Server:
    def __init__(self,addr,port,timeout):
        self.addr = addr            # server IP address/hostname
        self.port = port            # port number that server will listen on
        self.timeout = timeout      # time (s) before server closes due to inactivity
        self.sessions = {}
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.addr,self.port))
        self.server.listen()
        self.server.settimeout(self.timeout)
        self.lastCon = None

    def start_server(self):
        try:
            self.lastCon = time.time()
            while True:
                if time.time() - self.lastCon > self.timeout:
                    print("Server timeout due to inactivity.")
                    break
                try: 
                    self.conSock, con_addr = self.server.accept()  # server waits on accept() for incoming requests
                    self.lastCon = time.time()

                    threading.Thread(target=self.handle_request, args=(self.conSock,)).start()

                except socket.timeout:
                    print("Server timeout due to inactivity.")
                    continue  # Break the loop when server times out
                except Exception as e:
                    print(f"Error during connection: {e}")
                    break
        finally:
            self.stop_server()

    def stop_server(self):
        self.server.close()

    def parse_request(self, request_data):
        parts = request_data.split("\r\n")

        request = parts[0]
        headers = {}
        bparts = []
        bi = 0

        for i, line in enumerate(parts[1:],1):
            if line=="":
                bi +=1
                continue
            else:
                headers[i] = line

            if bi>0:
                bparts.append(line)

        body = "\n".join(bparts)

        return request, headers, body

    def handle_request(self, client_socket):
        request_data = b""
    
        while True:
            sentence = client_socket.recv(4096)
            if not sentence:
                break
            request_data += sentence

            if b"\r\n\r\n" in request_data:  # End of HTTP headers
                break

        if request_data:
            print(request_data.decode('utf-8'))

            conRequest, conHeaders, conBody = self.parse_request(request_data.decode('utf-8'))
            rparts = conRequest.split(" ")
            if rparts[1]=="/":
                rparts[1] = "assets/index.html"
            if rparts[0].__contains__("GET"):
                self.handle_get_request(client_socket, rparts[1])
            elif rparts[0].__contains__("POST"):
                self.handle_post_request(client_socket, rparts[1], conHeaders, conBody)
            else:
                self.handle_unsupported_method(client_socket,rparts[0])

        else:
            print("No data received, client closed connection.")

    def handle_unsupported_method(self, client_socket, method):
        rbody =  f"""\
            <html>
                <body>
                    <h1>405 Method Not Allowed</h1>
                    <p>The following method is not allowed: {method}</p>
                </body
            </html>"""          

        rheaders = f"Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(rbody)}\r\nConnection: close\r\n\r\n"

        rstatus = "405 Method Not Allowed\r\n"

        response = rstatus + rheaders + rbody
        client_socket.sendall(response.encode('utf-8'))
    
    def handle_get_request(self, client_socket, file_path):
        client_addr = client_socket.getpeername()

        while True:
            try:
                fp = open(file_path, "r")
                rbody = fp.read()
                fp.close()

                if not self.sessions.get(client_addr[0]):
                    rbody = rbody.replace("{{name}}", "Guest")
                else:
                    rbody = rbody.replace("{{name}}", self.sessions[client_addr[0]])

                rheaders = f"Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(rbody)}\r\nConnection: close\r\n\r\n"

                response = "HTTP/1.1 200 OK\r\n" + rheaders + rbody
                break
            except FileNotFoundError:
                response = "HTTP/1.1 404 Not Found"
                rbody =  """\
                    <html>
                        <body>
                            <h1>404 Not Found</h1>
                            <p>The requested file was not found.</p>
                        </body
                    </html>"""   
                rheaders = f"Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(rbody)}\r\nConnection: close\r\n\r\n"             
                response += rheaders + rbody
                break
            except Exception as e:
                response = f"HTTP/1.1 400 Error: {e}\r\n"
                rbody =  f"""\
                    <html>
                        <body>
                            <h1>400 Error</h1>
                            <p>{e}.</p>
                        </body
                    </html>"""
                rheaders = f"Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(rbody)}\r\nConnection: close\r\n\r\n"
                response += rheaders + rbody
                break
        
        client_socket.sendall(response.encode('utf-8'))
    
    def handle_post_request(self, client_socket, path, headers, body):
        client_addr = client_socket.getpeername()
        form_data = body.split("=")

        while True:
            try:
                if path=="/change_name":
                    self.sessions[client_socket.getpeername()[0]] = form_data[1]
                
                    rbody =  f"""\
                        <html>
                            <body>
                                <h1>200 OK</h1>
                                <p>Client Name update: {form_data[1]}</p>
                            </body
                        </html>"""          

                    rheaders = f"Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(rbody)}\r\nConnection: close\r\n\r\n"

                    rstatus = "HTTP/1.1 200 OK\r\n"
                else:
                    raise Exception()
            except Exception as e:
                rstatus = f"HTTP/1.1 404 Not Found"
                rbody =  f"""\
                    <html>
                        <body>
                            <h1>404 Not Found</h1>
                            <p>Method Not Found: {e}</p>
                        </body
                    </html>"""    
                rheaders = f"Content-Type: text/html; charset=utf-8\r\nContent-Length: {len(rbody)}\r\nConnection: close\r\n\r\n"            
            finally:
                response = rstatus + rheaders + rbody
                client_socket.sendall(response.encode('utf-8'))
                break

# Test Code below:
addr = '127.0.0.1'
port = 8080
stest = Server(addr,port,60)

sthread = threading.Thread(target = stest.start_server)
sthread.start()

cSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSock.connect((addr,port))

cSock.sendall(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
response = cSock.recv(4096)


cSock.close()
