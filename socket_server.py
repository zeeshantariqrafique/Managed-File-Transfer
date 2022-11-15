# Author : Zeeshan Tariq Rafique

from array import array
from distutils.command.config import config
import socketserver
import traceback
from config_manager import ConfigManager
from core_file_transfer import PythonFileTransfer
data_port_server_obj = None
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
            from main import handle_request , handle_data_request
            self.data = self.request.recv(self.BUFFER_SIZE).strip()
            (host, port) = self.server.server_address
            PythonFileTransfer.print_log(f'Recieved request from IP address {self.client_address[0]} , Data {self.data} , Port {port}')
            
            CONTROL_PORT = int(ConfigManager.get_instance().get_config()['controlport'])
            PythonFileTransfer.print_log(CONTROL_PORT)
            if int(port) == CONTROL_PORT:
                recv_str = self.data.decode('utf-8')
                handle_request(recv_str)
            else:
                handle_data_request(self.data)
        except ValueError:
            traceback.print_exc()
        except Exception:
            traceback.print_exc()

    
def serve(host: str,port: int) -> None:
    global data_port_server_obj
    PythonFileTransfer.print_log(f'Create the server, binding to {host} on port {str(port)}')
    server = socketserver.TCPServer((host, port), SocketServer)
    if port == int(ConfigManager.get_instance().get_config()['dataport']):
        data_port_server_obj = server
    server.serve_forever()

def close():
    PythonFileTransfer.print_log('Attempting shut down of data socket')
    global data_port_server_obj
    data_port_server_obj.server_close()
    data_port_server_obj.shutdown()
    PythonFileTransfer.print_log('Data Socket shut down success')