import os
import traceback
import zlib
from inspect import currentframe, stack


class PythonFileTransfer:
    @staticmethod
    def compress_file(file: str) -> str:
        '''Compress the file passed to the function to .gz format.'''
        try:
            print(f'Trying to compress file ==> {file}')
            with open(file, 'rb') as f:
                data = f.read()
            compressed_data = zlib.compress(data, 9)
            compressed_file_name = file + ".gz"
            print(f"Compressed file name ==> {compressed_file_name}")
            with open(compressed_file_name, 'wb') as of:
                of.write(compressed_data)
            print("File successfully compressed")
            return compressed_file_name
        except Exception as e:
            raise e

    @staticmethod
    def decompress_file(src_file: str, dest_file: str) -> None:
        '''Decompress the file name passed as a parameter to this function.'''
        try:
            with open(src_file, 'rb') as f:
                data_in_bytes = f.read()
                data = zlib.decompress(data_in_bytes)
            with open(dest_file, 'wb') as f:
                f.write(data)
        except Exception as e:
            raise e

    @staticmethod
    def create_file(file_name: str, file_path: str, file_data_in_bytes: bytes) -> bool:
        '''Create the file on the path received by the socket server.'''
        try:
            compressed_file_name = os.path.join(file_path, file_name + '.gz')
            original_file_name = os.path.join(file_path, file_name)
            print(type(file_data_in_bytes))
            print(file_data_in_bytes)
            with open(compressed_file_name, 'wb+') as f:
                f.write(file_data_in_bytes)
            pyft = PythonFileTransfer()
            pyft.decompress_file(compressed_file_name, original_file_name)
            print(f'Successfully wrote to destination path {original_file_name}')
            return True
        except Exception:
            traceback.print_exc()
            return False

    @staticmethod
    def create_transfer_command(src_file_name: str, dest_file_path: str, file_data: str) -> bytearray:
        '''Create a single socket command including metadata
        and actual file data to be transferred to destination
        remote host in bytes over TCP sockets.'''
        cmd = f'FILE_KEY|{src_file_name}|{dest_file_path}|{file_data}'
        return bytearray(cmd, 'utf8')

    @staticmethod
    def print_log(value: str) -> None:
        function = stack()[1][3]
        filename = os.path.splitext(os.path.basename(stack()[1].filename))[0]
        print(f'{filename}::{function}::{currentframe().f_back.f_lineno} => {value}')