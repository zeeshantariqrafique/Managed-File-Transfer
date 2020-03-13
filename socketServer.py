#Author : Zeeshan Tariq Rafique

import socketserver

class socketServer(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        try:
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            self.request.sendall(self.data.upper())
        except socketserver.Error as err:
            print("Error while handling : {}".format(err))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), socketServer)
    server.serve_forever()