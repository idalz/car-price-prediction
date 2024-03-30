from carPricePrediction.constants import *
from carPricePrediction.utils.common import read_yaml, create_directories
from carPricePrediction.entity import (
    DataIngestionConfig,
    DataCleaningConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig
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
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([
            config.root_dir, 
            config.dataset_dir,
            config.label_encoder_dir,
            config.tensors_dim_dir
        ])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            interim_dataset_dir = config.interim_dataset_dir,
            dataset_dir = config.dataset_dir,
            label_encoder_dir = config.label_encoder_dir,
            tensors_dim_dir = config.tensors_dim_dir            
        )

        return data_transformation_config
    
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([
            config.root_dir, 
            config.model_dir
        ])

        data_transformation_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            processed_dataset_dir = config.processed_dataset_dir,
            embed_dim_file_path = config.embed_dim_file_path,
            num_dim_file_path = config.num_dim_file_path,
            model_dir = config.model_dir,
            batch_size = params.batch_size,
            epochs = params.epochs,
            lr = params.lr,
            layers = params.layers,
            dropout = params.dropout       
        )

        return data_transformation_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.EvaluationArguments

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_file_path=config.model_file_path,
            model_state_file_path = config.model_state_file_path,
            embed_dim_file_path = config.embed_dim_file_path,
            num_dim_file_path = config.num_dim_file_path,
            data_file_path = config.data_file_path,
            evaluation_results = config.evaluation_results,
            batch_size = params.batch_size,
            layers = params.layers,
            dropout =  params.layers
        )

        return model_evaluation_config
    