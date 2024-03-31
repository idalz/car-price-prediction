from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    dataset_dir: Path
    source_URL: str

@dataclass(frozen=True)
class DataCleaningConfig:
    root_dir: Path
    raw_dataset_dir: Path
    dataset_dir: Path
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    interim_dataset_dir: Path
    dataset_dir: Path
    label_encoder_dir: Path
    tensors_dim_dir: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    processed_dataset_dir: Path
    embed_dim_file_path: str
    num_dim_file_path: str
    model_dir: Path
    batch_size: int
    epochs: int
    lr: float
    layers: List
    dropout: float

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_file_path: Path
    data_file_path: Path
    evaluation_results: Path
    batch_size: int
