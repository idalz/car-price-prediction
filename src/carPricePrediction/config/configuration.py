from carPricePrediction.constants import *
from carPricePrediction.utils.common import read_yaml, create_directories
from carPricePrediction.entity import (
    DataIngestionConfig,
    DataCleaningConfig
)

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            dataset_dir = config.dataset_dir,
            source_URL = config.source_URL
        )

        return data_ingestion_config
    
    def get_data_cleaning_config(self)-> DataCleaningConfig:
        config = self.config.data_cleaning

        create_directories([config.root_dir, config.dataset_dir])

        data_cleaning_config = DataCleaningConfig(
            root_dir = config.root_dir,
            raw_dataset_dir = config.raw_dataset_dir,
            dataset_dir = config.dataset_dir
            
        )

        return data_cleaning_config
    