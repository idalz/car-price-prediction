from carPricePrediction.logging import logger
from carPricePrediction.constants import *
from carPricePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# Data ingestion
try:
    logger.info(f"Stage: {STAGE_DATA_INGESTION} started.")  
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage: {STAGE_DATA_INGESTION} completed.")
except Exception as e:
    raise e
