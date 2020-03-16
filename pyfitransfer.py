import os
from socketClient import SocketClient
from configReader import ConfigPyFiTransfer


class PyFiTransfer:
    
    #Function to convert fully qualified file path into byte array (Socket transfer needs bytes)
    def getBytesfromFile(self,filename):
        fh = open(filename, 'rb')
        ba = bytearray(fh.read())
        return ba

# Correctly very naive approach will be changed later 
# populate the config object with the configuration in file transfer.yml (Look at configReader.py)
# From the config , get the source file path and file details and use the cofig destination details to transfer 
# file via socket 

configObj = ConfigPyFiTransfer()
configObj.getPyFiTransferConfig()
pft = PyFiTransfer()
input_file_ba=pft.getBytesfromFile(os.path.join(configObj.source_file_path,configObj.source_file_name))
sock = SocketClient()
sock.connect(configObj.destination_host,configObj.destination_port)
sock.transfer(input_file_ba)







