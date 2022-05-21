
        #Author : Zeeshan Tariq Rafique
        # Example usage 
        #configObj = ConfigManager()
        #config = configObj.get_config()
        #port = config.listen_port

import yaml

class ConfigManager:
    def get_config(self, file_path):
        '''
        file_path : The fully qualified config file path to be read 
        Read the given file_path and return a key-value dictionary with all
        key values from config 
        '''
        with open(file_path) as file:
            data = yaml.full_load(file)
        config_dict = { **data['socketserver'] , **data['transfer'] }
        return { k : v for k ,v in  config_dict.items() }