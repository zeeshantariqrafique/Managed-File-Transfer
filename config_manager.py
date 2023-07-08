import yaml
from collections import defaultdict


class ConfigManager:
    __shared_config = defaultdict(lambda: 'MFT')
    __shared_instance = None

    @staticmethod
    def get_instance():
        """Static Access Method"""
        if not ConfigManager.__shared_instance:
            ConfigManager()
        return ConfigManager.__shared_instance

    def __init__(self):
        """Virtual private constructor"""
        if ConfigManager.__shared_instance:
            raise Exception("This class is a ConfigManager class!")
        else:
            ConfigManager.__shared_instance = self

    def get_config(self):
        return self.__shared_config

    def get_config_from_file(self, file_path: str) -> dict:
        """
        Read the given file_path and return a key-value dictionary with all
        key values from the config
        """
        with open(file_path, encoding='utf-8') as file:
            data = yaml.full_load(file)
        config_dict = {**data['socketserver'], **data['transfer']}
        config_dict = {str(k).strip(): str(v).strip() for k, v in config_dict.items()}
        self.__shared_config.update(config_dict)
        return dict(config_dict.items())