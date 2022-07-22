
# Author : Zeeshan Tariq Rafique
# Example usage
#configObj = ConfigManager()
#config = configObj.get_config()
#port = config.listen_port

from shutil import ExecError
import yaml
from collections import defaultdict


class ConfigManager:
    
    __shared_config = defaultdict(
        lambda: 'MFT',
        key='instance')

    __shared_instance = 'MFT'
 
    @staticmethod
    def get_instance():
        """Static Access Method"""
        if ConfigManager.__shared_instance == 'MFT':
            ConfigManager()
        return ConfigManager.__shared_instance
 
    def __init__(self):
 
        """virtual private constructor"""
        if ConfigManager.__shared_instance != 'MFT':
            raise Exception ("This class is a ConfigManager class !")
        else:
            ConfigManager.__shared_instance = self
            
    def get_config(self):
        return self.__shared_config

    def get_config_from_file(
        self,
        file_path: str
        ) -> dict:
        '''
        file_path : The fully qualified config file path to be read
        Read the given file_path and return a key-value dictionary with all
        key values from config
        '''
        with open(file_path, encoding='utf-8') as file:
            data = yaml.full_load(file)
        config_dict = {**data['socketserver'], **data['transfer']} 
        config_dict = { str(k).strip() : str(v).strip() for k ,v in config_dict.items() }
        self.__shared_config.update(config_dict)
        return dict(config_dict.items())