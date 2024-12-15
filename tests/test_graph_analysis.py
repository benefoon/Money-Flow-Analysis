import pytest
import pandas as pd
import networkx as nx
from src.graph_analysis import build_graph, analyze_graph

def test_build_graph():
    """Tests the graph-building function."""
    data = pd.DataFrame({
        'sender': ['A', 'B', 'C'],
        'receiver': ['B', 'C', 'A'],
        'amount': [100, 150, 200],
        'time': ['2024-12-15', '2024-12-16', '2024-12-17']
    })
    G = build_graph(data)
    assert len(G.nodes) == 3, "Graph should have 3 nodes."
    assert len(G.edges) == 3, "Graph should have 3 edges."

def test_analyze_graph():
    """Tests the graph analysis functionality."""
    G = nx.DiGraph()
    G.add_edge('A', 'B', amount=100)
    G.add_edge('B', 'C', amount=150)
    centrality, communities = analyze_graph(G)
    assert len(centrality) == 3, "Centrality should have 3 nodes."
    assert len(communities) == 1, "There should be one community."
