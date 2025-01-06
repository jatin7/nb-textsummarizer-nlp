from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directory
from src.textSummarizer.entity import (DataIngestionConfig, DataValidationConfig)

class ConfiguartionManager:
    def __init__(self, config = CONFIG_FILE_PATH, param = PARAMS_FILE_PATH):
        self.config = read_yaml(config)
        self.params = read_yaml(param)
        create_directory([self.config.artifacts_root])
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directory([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )
        return data_validation_config