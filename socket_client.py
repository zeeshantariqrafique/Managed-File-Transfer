# Author : Zeeshan Tariq Rafique
# Usage : Utility socket client class
# Example :
#          socketcli = SocketClient()
#          socketcli.connect("www.google.com",80)

import socket
import traceback
from core_file_transfer import PythonFileTransfer
 
class SocketClient:
    connected = False

    def __init__(self):
        '''default constructor'''
        try:
            self.socketClient = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            PythonFileTransfer.print_log("Socket client instance created ")
        except socket.error as err:
            PythonFileTransfer.print_log("creation of socket failed due to : {}".format(err))

    def connect(
        self,
        host: str,
        port: int
        ) -> bool:
        '''connect using tcp socket to the given host and port'''
        try:
            self.socketClient.connect((str(host), int(port)))
            self.connected = True
            PythonFileTransfer.print_log("Connected to {} through port {} ".format(host, port))
            return True
        except socket.error as err:
            PythonFileTransfer.print_log(
                "Error while connecting to host {} and port {} with : {}".format(
                    host, port, err))
            return False

    def transfer(
        self,
        data: bytearray
        ) -> None:
        '''Sends the byte array (data) over socket to connected server'''
        if not self.connected:
            PythonFileTransfer.print_log("Not Conncted to any host")
        else:
            try:
                self.socketClient.send(data)
            except socket.error:
                traceback.print_exc()

    def close(self):
        '''closes the tcp socket with the remote host'''
        self.socketClient.close()
