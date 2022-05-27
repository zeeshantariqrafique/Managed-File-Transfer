#Author : Zeeshan Tariq Rafique
#Usage : Utility socket client class 
#Example : 
#          socketcli = SocketClient()
#          socketcli.connect("www.google.com",80)

import socket
import traceback

class SocketClient:
    connected = False
    def __init__(self):
        '''default constructor'''
        try:
            self.socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("Socket client instance created ")
        except socket.error as err:
            print("creation of socket failed due to : {}".format(err))

    def connect(self,host,port):
        '''connect using tcp socket to the given host and port'''
        try:
            self.socketClient.connect((host,port))
            self.connected = True
            print ("Connected to {} through port {} ".format(host,port))
            return True
        except socket.error as err:
            print("Error while connecting to host {} and port {} with : {}".format(host,port,err))
            return False

    def transfer(self,data):
        '''Sends the byte array (data) over socket to connected server'''
        if not self.connected:
            print("Not Conncted to any host")
        else:
            try:
                self.socketClient.send(data)
            except socket.error as err:
                traceback.print_exc()

    def close(self):
        '''closes the tcp socket with the remote host'''
        self.socketClient.close()
