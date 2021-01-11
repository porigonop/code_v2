import socket
import signal


class HttpServer:
    run = True
    listening_socket = None
    def handle_sigint(self, *args):
        self.run = False

    def __init__(self, address='127.0.0.1', port=4242):
        signal.signal(signal.SIGINT, self.handle_sigint)
        self.listening_socket = socket.socket()
        self.listening_socket.bind((address, port))
        self.listening_socket.listen(10)


    def handle_request(self, socket):
        input_ = socket.recv(4096)
        split = input_.split(b'\r\n')
        request_line = split[0].split()
        headers = split[1:]

        method = request_line[0]
        ressource = request_line[1]
        version = request_line[2]

        print(method, ressource, version)
        status_line = b'HTTP/1.0 200 OK'
        headers = {
                'Content-Length': 0
                }
        try:
            ressource_file = open('.' + ressource.decode('ascii'), 'rb')
        except FileNotFoundError:
            socket.close()
            return
        content = ressource_file.read()
        headers['Content-Length'] = len(content)
        socket.send(status_line + b'\r\n' + b'Content-Length: ' + bytes(str(headers['Content-Length']), 'ascii') + b'\r\n\r\n')
        socket.sendfile(ressource_file)
        ressource_file.close()
        # socket.close()
    def run(self):
        while self.run:
            r = self.listening_socket.accept()
            self.handle_request(r[0])
        self.listening_socket.close()
server = None
for i in range(4242, 4262):
    try:
        server = HttpServer(port=i)
        print(i)
        break
    except Exception as e:
        print(e)
        pass
if server:
    server.run()
