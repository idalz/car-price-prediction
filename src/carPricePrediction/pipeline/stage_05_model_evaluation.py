from carPricePrediction.components.model_evaluation import ModelEvaluation
from carPricePrediction.config.configuration import ConfigurationManager
from carPricePrediction.logging import logger
from carPricePrediction.constants import STAGE_MODEL_EVALUATION

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.evaluate_model()
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"Stage: {STAGE_MODEL_EVALUATION} started.")  
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"Stage: {STAGE_MODEL_EVALUATION} completed.")
    except Exception as e:
        raise e
    