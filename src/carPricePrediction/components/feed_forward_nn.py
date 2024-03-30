import torch
import torch.nn as nn

class FeedForwardNN(nn.Module):

    def __init__(self, embedding_dim, n_cont, out_dim, layers, dout=0.5):
        super().__init__()
        # Create embedding layer
        self.embeds = nn.ModuleList([nn.Embedding(inp, out) for inp,out in embedding_dim])
        # Apply dropout (prevent overfitting)
        self.emb_drop = nn.Dropout(dout)
        # Apply batch normalization to numerical features
        self.bn_cont = nn.BatchNorm1d(n_cont)

        # Total dimension of embedding layers
        n_emb = sum((out for inp,out in embedding_dim))
        # Total input (embedding and continuous) 
        n_inp = n_emb + n_cont

        layerlist = []
        for i in layers:
            # Create Linear layer
            layerlist.append(nn.Linear(n_inp,i))
            # Add activation function
            layerlist.append(nn.ReLU(inplace=True))
            # Add batch normalization in the neurons
            layerlist.append(nn.BatchNorm1d(i))
            # Drop some neurons
            layerlist.append(nn.Dropout(dout))
            # The input for the next layer
            n_inp = i
        # Final layer - output layer
        layerlist.append(nn.Linear(layers[-1], out_dim))

        # Wrap the layers with Sequential
        self.layers = nn.Sequential(*layerlist)

    def forward(self, x_cat, x_cont): 
        # Create and concat embeddings
        embeddings = []
        for i,e in enumerate(self.embeds):
            embeddings.append(e(x_cat[:,i]))
        x_cat = torch.cat(embeddings, 1)
        # Dropout
        x_cat = self.emb_drop(x_cat)
        # Batch normalization
        x_cont = self.bn_cont(x_cont)
        # Concat all features
        x = torch.cat([x_cat, x_cont], 1)
        # Return layer with input x
        layer = self.layers(x)
        
        return layer
    