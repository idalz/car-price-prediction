from carPricePrediction.components.model_trainer import ModelTrainer
from carPricePrediction.config.configuration import ConfigurationManager
from carPricePrediction.logging import logger
from carPricePrediction.constants import STAGE_MODEL_TRAINER

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_MODEL_TRAINER} started.")  
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_MODEL_TRAINER} completed.")
    except Exception as e:
        raise e
    