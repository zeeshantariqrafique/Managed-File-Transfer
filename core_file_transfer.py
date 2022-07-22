import os
import sys
import traceback
from inspect import currentframe
from threading import Thread
import zlib

class PythonFileTransfer:

    def compress_file(
        self,
        file: str
        ) -> str:
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


    def decompress_file(
        self,
        src_file: str,
        dest_file: str
        ) -> None:
        '''Decompress the file name passed as parameter to this function'''
        try:
            with open(src_file,'rb') as f:
                data = zlib.decompress(f)
            with open(dest_file,'wb') as f:
                f.write(bytes(data))
        except Exception as e:
            raise e

    def create_file(
        self,
        file_name: str,
        file_path: str,
        file_data_in_bytes: bytes
        ) -> bool:
        '''This function creates the file on the path recived by the socket server'''
        try:
            compressed_file_name = os.path.join(file_path,file_name+'.gz')
            original_file_name = os.path.join(file_path,file_name)
            print(type(file_data_in_bytes))
            print(file_data_in_bytes)
            f = open(compressed_file_name, 'wb+')
            f.write(file_data_in_bytes)
            pyft = PythonFileTransfer()
            pyft.decompress_file(compressed_file_name,original_file_name)
            print(f'Successfully wrote to destination path {original_file_name}')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            f.close()

    def create_transfer_command(
        self,
        src_file_name: str,
        dest_file_path: str,
        file_data: str
        ) -> bytearray:
        '''creates a single socket command including metadata
        and actual file data to be transferred to destination
        remote host in bytes over tcp sockets'''

        cmd = f'''FILE_KEY|{src_file_name}|{dest_file_path}|{file_data}'''
        return bytearray(cmd, 'utf8')
    
    def print_log(value : str)-> None:
        print(f'ManagedFileTransfer : {currentframe().f_back.f_lineno} => {value}')
