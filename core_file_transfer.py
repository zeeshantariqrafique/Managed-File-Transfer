import os
from socket_client import SocketClient
from config_manager import ConfigManager
import sys

class PythonFileTransfer:
    
    def create_transfer_command(self,destinationFullyQualifiedFileName,fileData):
        '''creates a single socket command including metadata 
        and actual file data to be transferred to destination 
        remote host in bytes over tcp sockets'''

        cmd = "FILE_KEY|"+destinationFullyQualifiedFileName+"|"+fileData
        return bytearray(cmd,'utf8')

 
def main():
    ''' main business function to read config (transfer.yml) and 
        send the file to remote host using tcp socket'''

    try:
        config_file_path = sys.argv[1]
        python_file_transfer = PythonFileTransfer()
        sock = SocketClient()
        config = ConfigManager().get_config(config_file_path)
        src_filename = os.path.join(config['sourcefilepath'],config['sourcefilename'])
        dest_filename = os.path.join(config['destinationfolder'],config['sourcefilename'])
        srcfile = open(src_filename,"r")
        data_to_send = python_file_transfer.create_transfer_command(dest_filename,srcfile.read())
        sock.connect(config['destinationhost'],config['destinationport'])
        sock.transfer(data_to_send)
    except Exception as e:
        print(e)
    finally:
        sock.close()


if __name__ == "__main__":
    main()




