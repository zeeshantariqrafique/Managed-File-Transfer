# Author : Zeeshan Tariq Rafique

from array import array
import socketserver
import traceback
import os


class SocketServer(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for socket server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    BUFFER_SIZE = 1024

    def handle(self) -> None:
        try:
            self.data = self.request.recv(self.BUFFER_SIZE).strip()
            print(
                f'Recieved request from IP address {self.client_address[0]} ')
            # decode() was required to make b'xyz -> xyz
            recv_str = self.data.decode('utf-8')
            # If the first 8 chars are "FILE_KEY" then this is a valid request
            request_array = recv_str.split('|')
            if request_array[0] == "FILE_KEY":
                # Only pass destination path | file data to create_file function
                self.create_file(request_array[1],request_array[2],request_array[3])
                pass
            else:
                raise ValueError('Not supported request')

            self.request.sendall(self.data.upper())
        except ValueError:
            traceback.print_exc()
        except Exception:
            traceback.print_exc()

    
    def serve(self,host: str,port: int) -> None:
        print('Create the server, binding to localhost on port 9999')
        server = socketserver.TCPServer((host, port), SocketServer)
        server.serve_forever()

def main():
    # TODO : Read port from config
    HOST, PORT = "localhost", 9999
    SocketServer().serve(HOST,PORT)

if __name__ == "__main__":
    main()
