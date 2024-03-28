from carPricePrediction.components.data_ingestion import DataIngestion
from carPricePrediction.config.configuration import ConfigurationManager
from carPricePrediction.logging import logger
from carPricePrediction.constants import STAGE_DATA_INGESTION

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
        except Exception as e:
            raise e 

if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_DATA_INGESTION} started.")  
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_DATA_INGESTION} completed.")
    except Exception as e:
        raise e
    