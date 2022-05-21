#Author : Zeeshan Tariq Rafique

from array import array
import socketserver

class socketServer(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for socket server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    BUFFER_SIZE = 1024
    def handle(self):
        try:
            self.data = self.request.recv(self.BUFFER_SIZE).strip()
            print(f'Recieved request from IP address {self.client_address[0]} ')
            #decode() was required to make b'xyz -> xyz
            recvStr = str(self.data.decode('utf-8'))
            #If the first 8 chars are "FILE_KEY" then this is a valid request
            request_array = recvStr.split('|')
            if request_array[0] == "FILE_KEY":
                #Only pass destination path | file data to createFile function
                self.createFile(request_array[1],request_array[2])
            else:
                raise ValueError('Not supported request')         

            self.request.sendall(self.data.upper())
        except ValueError as err:
            print("Value Error while handling request: {}".format(err))
        except Exception as e:
            print("Error while handling {}".format(e))

    
    def createFile(self,file_full_name,file_data_in_bytes):
        '''This function creates the file on the path recived by the socket server'''
        try:
            f = open(file_full_name,'w+')
            f.write(file_data_in_bytes)
            print(f'Successfully wrote to destination path {file_full_name}')
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            f.close()

def main():
    #TODO : Read port from config
    HOST, PORT = "localhost", 9999
    print('Create the server, binding to localhost on port 9999')
    server = socketserver.TCPServer((HOST, PORT), socketServer)
    server.serve_forever()

if __name__ == "__main__":
    main()
    
