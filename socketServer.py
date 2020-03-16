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
            #decode() was required to make b'xyz -> xyz
            recvStr = str(self.data.decode('utf-8'))
            #If the first 8 chars are "FILE_KEY" then this is a valid request
            if recvStr[:8] == "FILE_KEY":
                #Only pass destination path | file data to createFile function
                self.createFile(recvStr[9:])
            else:
                raise ValueError('Not supported request')         

            self.request.sendall(self.data.upper())
        except ValueError as err:
            print("Value Error while handling request: {}".format(err))
        except Exception as e:
            print("Error while handling {}".format(e))

    #This function creates the file on the path recived by the socket server
    def createFile(self,recvStr):
        x = recvStr.split('|')
        dest_file_path = x[0]
        f = open(dest_file_path,'w+')
        f.write(x[1])
        f.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), socketServer)
    server.serve_forever()