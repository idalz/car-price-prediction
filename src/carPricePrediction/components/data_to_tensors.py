import joblib
import pandas as pd
import torch

class DataToTensors:
    def __init__(self):
        self.lbl_encoders = joblib.load('artifacts/encoders/LE_dict.pkl')
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    def json_to_tensors(self, json_string):
        # Load JSON file into a DataFrame
        df = pd.read_json(json_string)

        # Convert data to tensors
        # Numerical tensor
        num_features = df.select_dtypes(include='number').columns
        num_arr = df[num_features].to_numpy()
        num_tensor = torch.tensor(num_arr, dtype=torch.float).to(self.device)
        
        # Categorical tensor
        cat_features = df.select_dtypes(include='object').columns
        for feature in cat_features:
            df[feature] = self.lbl_encoders[feature].transform(df[feature])
        cat_arr = df[cat_features].to_numpy()
        cat_tensor = torch.tensor(cat_arr, dtype=torch.int64).to(self.device)

        # return tensors
        return cat_tensor, num_tensor
