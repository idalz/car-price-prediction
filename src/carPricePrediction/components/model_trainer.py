import os
import pickle

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from carPricePrediction.components.feed_forward_nn import FeedForwardNN
from carPricePrediction.entity import ModelTrainerConfig
from carPricePrediction.logging.model_logger import ModelLogger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def get_shuffled_batches(self, train_data, val_data, batch_size):
        train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
        val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=True)
        return train_loader, val_loader

    def train(self):
        # Choose device
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load train and validation data
        train_filepath = os.path.join(self.config.processed_dataset_dir, "train.pth")
        train_data = torch.load(train_filepath)

        val_filepath = os.path.join(self.config.processed_dataset_dir, "val.pth")
        val_data = torch.load(val_filepath)

        # Load dimensions
        with open(self.config.num_dim_file_path, 'rb') as f:
            num_dim = pickle.load(f)

        with open(self.config.embed_dim_file_path, 'rb') as f:
            embedding_dim = pickle.load(f)
        
        # Set batches
        batch_size = self.config.batch_size
        train_loader, val_loader = self.get_shuffled_batches(train_data, val_data, batch_size)
        
        # Create model
        torch.manual_seed(100)
        model = FeedForwardNN(
            embedding_dim=embedding_dim, 
            n_cont=num_dim, 
            out_dim=1, 
            layers=self.config.layers, 
            dout=self.config.dropout
        ).to(device)

        # Choose loss funciton and optimizer
        loss_function = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=self.config.lr)

        # Create the model logger
        model_logger_file_path = os.path.join(self.config.model_dir, 'model_training.log')
        modelLogger = ModelLogger(model_logger_file_path)

        # Set epochs
        num_epochs = self.config.epochs 

        # Train model
        for epoch in range(num_epochs):
            total_loss = 0
            model.train()
            for batch_idx, (cat_data, num_data, target) in enumerate(train_loader):
                cat_data, num_data, target = cat_data.to(device), num_data.to(device), target.to(device)
                optimizer.zero_grad()
                prediction = model(cat_data, num_data)
                loss = torch.sqrt(loss_function(prediction, target))
                total_loss += loss
                loss.backward()
                optimizer.step()
            total_loss /= len(train_loader)
            
            # Get validation loss
            val_loss = 0
            model.eval()
            with torch.no_grad():
                for cat_data, num_data, target in val_loader:
                    cat_data, num_data, target = cat_data.to(device), num_data.to(device), target.to(device)
                    prediction = model(cat_data, num_data)
                    val_loss += torch.sqrt(loss_function(prediction, target))
                val_loss /= len(val_loader)

            # Add to log file
            message = f'Epoch {epoch+1}/{num_epochs}, train_Loss: {total_loss:.4f}, val_Loss: {val_loss:.4f}'
            modelLogger.log_message(message)

        # Save the entire model
        model_file_path = os.path.join(self.config.model_dir, 'model.pth')
        torch.save(model, model_file_path)

        # Save model's state
        model_state_file_path = os.path.join(self.config.model_dir, 'model_state_dict.pth')
        torch.save(model.state_dict(), model_state_file_path)
   