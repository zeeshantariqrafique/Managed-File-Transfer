
# Author : Zeeshan Tariq Rafique
# Example usage
#configObj = ConfigManager()
#config = configObj.get_config()
#port = config.listen_port

import yaml


class ConfigManager:
    def get_config(self, file_path: str) -> dict:
        '''
        file_path : The fully qualified config file path to be read
        Read the given file_path and return a key-value dictionary with all
        key values from config
        '''
        with open(file_path, encoding='utf-8') as file:
            data = yaml.full_load(file)
        config_dict = {**data['socketserver'], **data['transfer']} 
        config_dict = { str(k).strip() : str(v).strip() for k ,v in config_dict.items() }
        return dict(config_dict.items())
