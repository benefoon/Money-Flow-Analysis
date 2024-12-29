import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(graph):
    """Plot a transaction graph."""
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray')
    plt.title("Transaction Graph")
    plt.show()
