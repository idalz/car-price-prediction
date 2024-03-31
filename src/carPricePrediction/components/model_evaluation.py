import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from carPricePrediction.components.feed_forward_nn import FeedForwardNN
from carPricePrediction.config.configuration import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self):
        # Set device
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Load the entire model
        model = torch.load(self.config.model_file_path)
    
        # Set it to current device (not needed)
        model.to(device)
        
        # Load test data
        test_data = torch.load(self.config.data_file_path)
        # Create data loader
        test_loader = DataLoader(test_data, batch_size=self.config.batch_size, shuffle=True)

        # Set loss function
        loss_function = nn.MSELoss()

        model.eval()  # Set the model to evaluation mode
        test_loss = 0

        # Model Evaluation
        with torch.no_grad():
            for cat_data, num_data, target in test_loader:
                cat_data, num_data, target = cat_data.to(device), num_data.to(device), target.to(device)
                prediction = model(cat_data, num_data)
                loss = torch.sqrt(loss_function(prediction, target))
                test_loss += loss
            test_loss /= len(test_loader)

        # Save test loss
        with open(self.config.evaluation_results, 'w') as file:
            file.write(f'Test Loss (RMSE): {test_loss:.4f}')
            