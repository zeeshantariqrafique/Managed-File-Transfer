#Author : Zeeshan Tariq Rafique
#Usage : Utility socket client class 
#Example : 
#          socketcli = SocketClient()
#          socketcli.connect("www.google.com",80)

import socket
class SocketClient:
    connected = False
    def __init__(self):
        try:
            self.socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("Socket is created ")
        except socket.error as err:
            print("creation of socket failed due to : {}".format(err))

    def connect(self,host,port):
        try:
            self.socketClient.connect((host,port))
            self.connected = True
            print ("Connected to {} through port {} ".format(host,port))
        except socket.error as err:
            print("Error while connecting to host {} and port {} with : {}".format(host,port,err))

    def transfer(self,data):
        if not self.connected:
            print("Not Conncted to any host")
        else:
            try:
                self.socketClient.send(data)
            except socket.error as err:
                print("Error while sending data")

