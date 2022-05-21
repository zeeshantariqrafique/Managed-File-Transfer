import os
from socket_client import SocketClient
from config_manager import ConfigManager
import sys

class PythonFileTransfer:
    
    #Function to convert fully qualified file path into byte array (Socket transfer needs bytes)
    def getBytesfromFile(self,filename):
        try:
            fh = open(filename, 'rb')
            ba = bytearray(fh.read())
            return ba
        finally:
            fh.close()

    #TODO : Logic -> Sendcommand|DESTINATION_FILE_PATH|DESTINATION_FILE_NAME|DATA_OF_FILE_IN_BYTES
    #Example : FILE_KEY|/home/test/dest/path|thefileToBetransferred.txt|Thedatawithinthefileasbytes
    def create_transfer_command(self,destinationFullyQualifiedFileName,fileData):
        cmd = "FILE_KEY|"+destinationFullyQualifiedFileName+"|"+fileData
        return bytearray(cmd,'utf8')

# Correctly very naive approach will be changed later 
# populate the config object with the configuration in file transfer.yml (Look at configReader.py)
# From the config , get the source file path and file details and use the cofig destination details to transfer 
# file via socket 
def main():
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




