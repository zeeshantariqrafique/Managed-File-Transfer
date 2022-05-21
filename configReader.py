
        #Author : Zeeshan Tariq Rafique
        # Example usage 
        #configObj = ConfigPyFiTransfer()
        #configObj.getPyFiTransferConfig()
        #port = configObj.listen_port

import yaml

class ConfigPyFiTransfer:
    #This function popualates the calling object with the configuration present in transfer.yml
    #TODO : avoid hard coding file name 
    def getPyFiTransferConfig(self):
        with open(r'transfer.yml') as file:
            data = yaml.full_load(file)
                
        for k, v in data["socketserver"].items():
            setattr(ConfigPyFiTransfer,k,v)
                
        for k , v in data['transfer'].items():
            setattr(ConfigPyFiTransfer,k,v)
