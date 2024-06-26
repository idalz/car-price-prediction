from pathlib import Path

# File paths
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

# Pipeline stages
STAGE_DATA_INGESTION = "Data Ingestion"
STAGE_DATA_CLEANING = "Data Cleaning"
STAGE_DATA_TRANSFORMATION = "Data Transformation"
STAGE_MODEL_TRAINER = "Model Trainer"
STAGE_MODEL_EVALUATION = "Model Evaluation"

NUM_FEATURES = ['Cylinders', 'Airbags', 'EngineVolume', 'Mileage_km', 'years']
CAT_FEATURES = ['Manufacturer', 'Category', 'Leather interior', 'Fuel type',
       'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color', 'Turbo']