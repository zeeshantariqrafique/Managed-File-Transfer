from encodings.utf_8 import decode
import os
import sys
from threading import Thread
import traceback
from config_manager import ConfigManager
from core_file_transfer import PythonFileTransfer
from socket_client import SocketClient
from socket_server import serve , close
import random

job_id = None
file_name = None
file_path = None


def send(request_array : list)-> None:
    try:
        jobid = request_array[1]
        src_file = request_array[2]
        data_port = request_array[3]
        dest_ip = request_array[4]
        PythonFileTransfer.print_log(f'''In Send request 
                job_id = {job_id}
                src_file = {src_file} 
                dest_ip = {dest_ip}
                data_port = {data_port}''')
        #Check if src file xists
        if not os.path.exists(src_file):
            raise FileNotFoundError(f'Source  => {src_file} not found')
    
        sock_client = SocketClient()
        sock_client.connect(dest_ip,int(data_port))
        #read src file 
        f = open(src_file,mode='rb')
        data_in_bytes = f.read()
        sock_client.transfer(bytearray(data_in_bytes))
        PythonFileTransfer.print_log(f'From Send Function , Sent : {str(data_in_bytes)}')
    except Exception as e:
        raise e 
    finally:
        sock_client.close()


def receive(request_array : list)->None:
    try:
        global job_id
        global dest_file
        global dest_folder
        job_id = request_array[1]
        src_file = request_array[2]
        src_ip = request_array[3]
        src_control_port = request_array[4]
        dest_ip = request_array[5]
        dest_file = request_array[6]
        dest_folder = request_array[7]
        config = ConfigManager.get_instance().get_config()
        PythonFileTransfer.print_log(f'''In Recieve request 
            job_id = {job_id}
            src_file = {src_file} 
            src_ip = {src_ip}
            src_control_port = {src_control_port}
            dest_ip = {dest_ip}
            dest_file = {dest_file}
            dest_folder = {dest_folder}''')
        #Check if destination folder exists
        if not os.path.exists(dest_folder):
            raise FileNotFoundError(f'Dest Folder => {dest_folder} not found')

        #Start Socket Server on data port 
        dataport = int(config['dataport'])
        Thread(
        target=serve,
        args=('localhost',
        int(dataport)
        )).start()
        PythonFileTransfer.print_log(f'Completed starting of socket on {dataport}')
        #Send request to source file server to send file
        #(SEND|JOBID|SRCFILE|DATAPORT|DESTIP)
        sock_client = SocketClient()
        sock_client.connect(src_ip,int(src_control_port))
        send_command = f'S|{job_id}|{src_file}|{dataport}|{dest_ip}'
        sock_client.transfer(bytearray(send_command,encoding='utf-8'))
        PythonFileTransfer.print_log(f'Sent : {send_command}')

    except FileNotFoundError as fnf:
        raise fnf
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sock_client.close()


def ack(request_array : list)->None:
    jobid = request_array[1]
    status = request_array[2]


def data(data_in_bytes: bytes)->None:
    PythonFileTransfer.print_log(f'In data()..')
    #Read the byte array and store in file 
    dest_fqfn = os.path.join(dest_folder,dest_file)
    PythonFileTransfer.print_log(f'Destination file to created  : {dest_fqfn}')
    f = open(dest_fqfn,mode='wb')
    f.write(data_in_bytes)
    f.close()
    PythonFileTransfer.print_log(f'Wrote {dest_file}')
    #close data port
    PythonFileTransfer.print_log('Attempting to close socket')
    close()
    
def complete(equest_array: list)-> None:
    pass

def handle_request(
    request: str
    ) -> None:
    try:
        global job_id
        global file_name
        global file_path
        request_execute = { 
        'R' : receive,
        'S' : send,
        'D' : data,
        'C' : complete,
        'A' : ack
        }
        request_array = request.split('|')
        request_type=request_array[0]
        try:
            request_execute[request_type](request_array)
        except KeyError as ke:
            PythonFileTransfer.print_log(f'Incorrect request : {request_array}')
            raise ke
    except ValueError:
            traceback.print_exc()
    except Exception:
        traceback.print_exc()

def handle_data_request(request_bytes : bytes) -> None:
    PythonFileTransfer.print_log('In handle_data_request...')
    PythonFileTransfer.print_log(request_bytes)
    data(request_bytes)



def send_file():
    ''' main business function to read config (transfer.yml) and
        send the file to remote host using tcp socket'''
    PythonFileTransfer.print_log('Entered send_file() function')
    try:
        job_id = str(random.randint(1000, 9999))
        sock = SocketClient()
        pyft = PythonFileTransfer()
        compressed_file = pyft.compress_file(os.path.join(config['sourcefilepath'],config['sourcefilename']))
        src_filename = open(compressed_file,mode="r")
        data_to_send = bytearray(f'''{job_id}|{config['sourcefilename']}|{config['destinationfolder']}''',
                            'utf-8')
        sock.connect(config['destinationhost'], config['destinationport'])
        sock.transfer(data_to_send)
    except Exception as e:
        traceback.print_exc()
    finally:
        sock.close()

def main():
    global config
    config_file_path = 'transfer.yml'
    
    if len(sys.argv) > 1:
        config_file_path = sys.argv[1]
    
    config_obj = ConfigManager.get_instance()
    config = config_obj.get_config_from_file(config_file_path)
    PythonFileTransfer.print_log(f'config is => {config}')
    PythonFileTransfer.print_log(f'Using config file {config_file_path}')

    if len(sys.argv) > 2:
        PythonFileTransfer.print_log(f"Setting control port {config['controlport']} \
        and dataport {config['dataport']}")
        config['controlport'] = sys.argv[2]
        config['dataport'] = sys.argv[3]
    
    Thread(
        target=serve,
        args=('localhost',
        int(config['controlport'])
        )).start()

if __name__ == "__main__":
    main()