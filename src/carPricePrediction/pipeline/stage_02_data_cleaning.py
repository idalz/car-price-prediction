from carPricePrediction.components.data_cleaning import DataCleaning
from carPricePrediction.config.configuration import ConfigurationManager
from carPricePrediction.logging import logger
from carPricePrediction.constants import STAGE_DATA_CLEANING

class DataCleaningTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_cleaning_config = config.get_data_cleaning_config()
            data_cleaning = DataCleaning(config=data_cleaning_config)
            data_cleaning.clean_data()
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_DATA_CLEANING} started.")  
        obj = DataCleaningTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_DATA_CLEANING} completed.")
    except Exception as e:
        raise e
    