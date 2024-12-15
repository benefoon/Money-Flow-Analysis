import networkx as nx
import pandas as pd

def build_graph(data):
    """Builds a graph from transaction data."""
    G = nx.DiGraph()
    for _, row in data.iterrows():
        G.add_edge(row['sender'], row['receiver'], amount=row['amount'], time=row['time'])
    return G

def analyze_graph(G):
    """Analyzes graph properties."""
    centrality = nx.degree_centrality(G)
    communities = nx.algorithms.community.greedy_modularity_communities(G)
    return centrality, communities

if __name__ == "__main__":
    data = pd.read_csv("data/processed/transactions_normalized.csv")
    G = build_graph(data)
    centrality, communities = analyze_graph(G)
    print("Top central nodes:", sorted(centrality.items(), key=lambda x: -x[1])[:5])
