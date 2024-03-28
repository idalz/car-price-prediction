import os 
from kaggle.api.kaggle_api_extended import KaggleApi
from carPricePrediction.logging import logger
from carPricePrediction.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.dataset_dir):
            # Connect to Kaggle API
            api = KaggleApi()
            api.authenticate()

            # Download the dataset
            api.dataset_download_files(
                dataset=self.config.source_URL,
                path=self.config.dataset_dir,
                unzip=True
            )

            logger.info("Dataset downloaded successfully.")
        else:
            logger.info(f"Dataset already exists.")
