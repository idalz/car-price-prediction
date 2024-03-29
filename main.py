from carPricePrediction.logging import logger
from carPricePrediction.constants import *
from carPricePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from carPricePrediction.pipeline.stage_02_data_cleaning import DataCleaningTrainingPipeline

# Data ingestion
try:
    logger.info(f"Stage: {STAGE_DATA_INGESTION} started.")  
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage: {STAGE_DATA_INGESTION} completed.")
except Exception as e:
    raise e

# Data cleaning
try:
    logger.info(f"Stage: {STAGE_DATA_CLEANING} started.")  
    obj = DataCleaningTrainingPipeline()
    obj.main()
    logger.info(f"Stage: {STAGE_DATA_CLEANING} completed.")
except Exception as e:
    raise e