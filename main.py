import os
import sys
from threading import Thread
import traceback
from config_manager import ConfigManager
from core_file_transfer import PythonFileTransfer
from socket_client import SocketClient
from socket_server import SocketServer


def main():
    ''' main business function to read config (transfer.yml) and
        send the file to remote host using tcp socket'''

    try:
        config_file_path = sys.argv[1]
        sock = SocketClient()
        pyft = PythonFileTransfer()
        config = ConfigManager().get_config(config_file_path)
        compressed_file = pyft.compress_file(os.path.join(config['sourcefilepath'],
            config['sourcefilename']))
        src_filename = open(compressed_file,mode="r")
        data_to_send = bytearray(f'''FILE_KEY|{config['sourcefilename']}|{config['destinationfolder']}|{src_filename.read()}''',
                            'utf-8')
        sock.connect(config['destinationhost'], config['destinationport'])
        sock.transfer(data_to_send)
    except Exception as e:
        traceback.print_exc()
    finally:
        sock.close()


if __name__ == "__main__":
    Thread(target=SocketServer().serve('localhost',9000)).start()
    main()
