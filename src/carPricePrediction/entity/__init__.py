from dataclasses import dataclass
from pathlib import Path

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
