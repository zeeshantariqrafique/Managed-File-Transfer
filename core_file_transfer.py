import os
from socket_client import SocketClient
from config_manager import ConfigManager
import sys
import traceback
import zlib

class PythonFileTransfer:

    def compress_file(self,file):
        '''compress the file passed to the function to gz format '''
        try:
            print(f'Trying to compress file ==> {file}')
            with open(file,'rb') as f:
                data = f.read()
            compressed_data=zlib.compress(data,9)
            compressed_file_name = str(file) + ".gz"
            print(f"Compressed file name ==> {compressed_file_name}")
            with open(compressed_file_name,'wb') as of:
                of.write(compressed_data)
            print("File successfully compressed")
            return compressed_file_name
        except Exception as e:
            raise e


    def decompress_file(self,file):
        '''Decompress the file name passed as parameter to this function'''
        with open(file,'rb') as f:
            data = zlib.decompress(f)
        print(data)

    def create_transfer_command(
            self,
            destinationFullyQualifiedFileName,
            fileData):
        '''creates a single socket command including metadata
        and actual file data to be transferred to destination
        remote host in bytes over tcp sockets'''

        cmd = "FILE_KEY|" + destinationFullyQualifiedFileName + "|" + fileData
        return bytearray(cmd, 'utf8')


def main():
    ''' main business function to read config (transfer.yml) and
        send the file to remote host using tcp socket'''

    try:
        config_file_path = sys.argv[1]
        python_file_transfer = PythonFileTransfer()
        sock = SocketClient()
        config = ConfigManager().get_config(config_file_path)
        src_filename = os.path.join(
            config['sourcefilepath'],
            config['sourcefilename'])
        dest_filename = os.path.join(
            config['destinationfolder'],
            config['sourcefilename'])
        srcfile = open(src_filename, encoding='utf-8', mode="r")
        data_to_send = python_file_transfer.create_transfer_command(
            dest_filename, srcfile.read())
        sock.connect(config['destinationhost'], config['destinationport'])
        sock.transfer(data_to_send)
    except Exception as e:
        traceback.print_exc()
    finally:
        sock.close()


if __name__ == "__main__":
    main()
