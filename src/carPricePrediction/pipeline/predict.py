import torch

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, cat_tensor, num_tensor):
        # Load and set the model
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = torch.load('artifacts/model/model.pth')
        model.to(device)
        model.eval()

        # Predict the value
        with torch.no_grad():
            results = model(cat_tensor, num_tensor)

        return results.item()
     