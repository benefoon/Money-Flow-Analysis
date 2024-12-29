from torch_geometric.loader import DataLoader
from src.graph_model import GNN

def train_model(data, epochs=50, lr=0.01):
    """Train GNN model."""
    model = GNN(input_dim=1, hidden_dim=16, output_dim=2)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=5e-4)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        out = model(data)
        loss = F.nll_loss(out, torch.tensor([0, 1, 0]))
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')
    return model
