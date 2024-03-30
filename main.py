from carPricePrediction.logging import logger
from carPricePrediction.constants import *
from carPricePrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from carPricePrediction.pipeline.stage_02_data_cleaning import DataCleaningTrainingPipeline
from carPricePrediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from carPricePrediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
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

# Data transformation
try:
    logger.info(f"Stage: {STAGE_DATA_TRANSFORMATION} started.")  
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"Stage: {STAGE_DATA_TRANSFORMATION} completed.")
except Exception as e:
    raise e

# Model Trainer
try :
    logger.info(f"Stage: {STAGE_MODEL_TRAINER} started.")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"Stage: {STAGE_MODEL_TRAINER} completed.")
except Exception as e:
    raise e
