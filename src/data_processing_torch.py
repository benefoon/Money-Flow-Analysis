import pandas as pd
import networkx as nx

def load_data(file_path):
    """Load transaction data from CSV file."""
    return pd.read_csv(file_path)

def create_graph(data):
    """Create a graph from transaction data."""
    G = nx.from_pandas_edgelist(data, 'source', 'target', edge_attr=True)
    return G

def preprocess_data(data):
    """Clean and preprocess the data."""
    data = data.dropna()  # حذف مقادیر گمشده
    data = data[data['amount'] > 0]  # حذف تراکنش‌های غیرمعتبر
    return data
