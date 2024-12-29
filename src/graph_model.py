import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv

class GNN(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GNN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

def create_data_object(graph):
    """Convert NetworkX graph to PyTorch Geometric Data object."""
    edge_index = torch.tensor(list(graph.edges)).t().contiguous()
    x = torch.tensor([[1.0] for _ in range(graph.number_of_nodes())], dtype=torch.float)
    return Data(x=x, edge_index=edge_index)
