import torch
from carPricePrediction.components.data_to_tensors import DataToTensors
class PredictionPipeline:
    def __init__(self):
        self.obj = DataToTensors()      

    def predict(self, data):
        # Data to tensors
        cat_tensor, num_tensor = self.obj.convert_data_to_tensors(data)
        
        # Load and set the model
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = torch.load('artifacts/model/model.pth')
        model.to(device)
        model.eval()

        # Predict the value
        with torch.no_grad():
            results = model(cat_tensor, num_tensor)
            
        return results.item()
     