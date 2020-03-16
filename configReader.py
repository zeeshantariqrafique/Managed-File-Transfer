
#Author : Zeeshan Tariq Rafique
# Example usage 
#configObj = ConfigPyFiTransfer()
#configObj.getPyFiTransferConfig()
#port = configObj.listen_port

import yaml

class ConfigPyFiTransfer:
    listen_port = 0000
    destination_host = None
    destination_port = None
    destination_folder = None
    source_file_name = None
    source_file_path = None
    source_file_pattern = None
    real_time_flag = None

    #This function popualates the calling object with the configuration present in transfer.yml
    #TODO : avoid hard coding file name 
    def getPyFiTransferConfig(self):
    
        with open(r'transfer.yml') as file:
            data = yaml.full_load(file)
        
        for k, v in data["socketserver"].items():
            if k == "listenport" and v is not None:
                self.listen_port = v

        for k, v in data["transfer"].items():
            if k == "destinationhost" and v is not None:
                self.destination_host = v
            if k == "destinationport" and v is not None:
                self.destination_port = v
            if k == "destinationfolder" and v is not None:
                self.destination_folder = v
            if k == "sourcefilename" and v is not None:
                self.source_file_name = v
            if k == "sourcefilepath" and v is not None:
                self.source_file_path = v
            if k == "sourcefilepattern" and v is not None:
                self.source_file_pattern = v
            if k == "realtimeflag" and v is not None:
                self.real_time_flag = v
            


        
