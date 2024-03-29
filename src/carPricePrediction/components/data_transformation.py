import os
import joblib
import pickle

import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder

from carPricePrediction.logging import logger
from carPricePrediction.config.configuration import DataTransformationConfig

class DataTransfomration:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def transform_data(self):
        ### Read interim data
        file = os.listdir(self.config.interim_dataset_dir)
        interim_data = os.path.join(self.config.interim_dataset_dir, file[0])
        df = pd.read_csv(interim_data)

        # Get features type
        target_feature = 'Price'
        num_features = df.drop(['Price'], axis=1).select_dtypes(include='number').columns
        cat_features = df.select_dtypes(include='object').columns

        # Label encoding for categorical features
        lbl_encoders={}
        for feature in cat_features:
            lbl_encoders[feature] = LabelEncoder()
            df[feature] = lbl_encoders[feature].fit_transform(df[feature])

        # Convert categorical data into tensor
        cat_arr = df[cat_features].to_numpy()
        cat_tensor = torch.tensor(cat_arr, dtype=torch.int64)
        cat_tensor

        # Convert numerical data into tensor
        num_arr = df[num_features].to_numpy()
        num_tensor = torch.tensor(num_arr, dtype=torch.float)
        num_tensor

        # Convert target into tensor
        target_arr = df[target_feature].to_numpy()
        y_tensor = torch.tensor(target_arr, dtype=torch.float).reshape(-1,1)

        # Create the embedding size for categorical features
        cat_dims = [len(df[feature].unique()) for feature in cat_features]
        # Rule of thumb for embedding dim (by fastai)
        embedding_dim = [(x, min(50, (x+1)//2)) for x in cat_dims]

        ### Save Label Encoders
        for feature, encoder in lbl_encoders.items():
            encoder_file_path = os.path.join(self.config.label_encoder_dir, f'LE_{feature}.pkl')
            joblib.dump(encoder, encoder_file_path)
        logger.info("Label encoders saved successfully.")
        
        ### Save embedding dimensions 
        emb_dim_file_path = os.path.join(self.config.embed_dim_dir, 'embedding_dim.pkl')
        with open(emb_dim_file_path, 'wb') as f:
            pickle.dump(embedding_dim, f)
        logger.info("Embedding dimensions saved successfully.")

        ### Save torch tensors
        cat_tensor_file_path = os.path.join(self.config.dataset_dir,"cat_tensor.pt")
        num_tensor_file_path = os.path.join(self.config.dataset_dir,"num_tensor.pt")
        y_tensor_file_path = os.path.join(self.config.dataset_dir,"y_tensor.pt")
        
        torch.save(cat_tensor, cat_tensor_file_path)
        torch.save(num_tensor, num_tensor_file_path)
        torch.save(y_tensor, y_tensor_file_path)

        logger.info("Tensors saved successfully.")
