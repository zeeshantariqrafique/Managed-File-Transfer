import os
from socketClient import SocketClient
from configReader import ConfigPyFiTransfer


class PyFiTransfer:
    

    def getBytesfromFile(self,filename):
        fh = open(filename, 'rb')
        ba = bytearray(fh.read())
        return ba

configObj = ConfigPyFiTransfer()
configObj.getPyFiTransferConfig()
pft = PyFiTransfer()
input_file_ba=pft.getBytesfromFile(os.path.join(configObj.source_file_path,configObj.source_file_name))
sock = SocketClient()
sock.connect(configObj.destination_host,configObj.destination_port)
sock.transfer(input_file_ba)







