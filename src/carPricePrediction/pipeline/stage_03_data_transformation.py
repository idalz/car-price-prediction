from carPricePrediction.components.data_transformation import DataTransfomration
from carPricePrediction.config.configuration import ConfigurationManager
from carPricePrediction.logging import logger
from carPricePrediction.constants import STAGE_DATA_TRANSFORMATION

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransfomration(config=data_transformation_config)
            data_transformation.transform_data()
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_DATA_TRANSFORMATION} started.")  
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_DATA_TRANSFORMATION} completed.")
    except Exception as e:
        raise e
    