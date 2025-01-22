import os
import logging
import pandas as pd
import networkx as nx

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("graph_modeling.log"),
        logging.StreamHandler()
    ]
)

def load_cleaned_data(file_path):
    """
    Load cleaned transaction data from a CSV file.
    
    Args:
        file_path (str): Path to the cleaned data CSV file.
    
    Returns:
        pd.DataFrame: Loaded transaction data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Cleaned data successfully loaded from {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def build_graph(data):
    """
    Build a directed graph from transaction data.
    
    Args:
        data (pd.DataFrame): Transaction data containing sender, receiver, and amount.
    
    Returns:
        nx.DiGraph: Directed graph representing transactions.
    """
    try:
        G = nx.DiGraph()
        for _, row in data.iterrows():
            G.add_edge(row['sender'], row['receiver'], amount=row['amount'])
        logging.info("Graph successfully built with %d nodes and %d edges", G.number_of_nodes(), G.number_of_edges())
        return G
    except KeyError as e:
        logging.error(f"Missing required column in data: {e}")
        raise
    except Exception as e:
        logging.error(f"Error building graph: {e}")
        raise

def analyze_graph(G):
    """
    Analyze the directed graph and compute centrality metrics.
    
    Args:
        G (nx.DiGraph): Directed graph to analyze.
    
    Returns:
        dict: Centrality metrics for each node.
    """
    try:
        logging.info(nx.info(G))
        centrality = nx.degree_centrality(G)
        top_central_nodes = sorted(centrality.items(), key=lambda x: -x[1])[:5]
        logging.info("Top 5 central nodes: %s", top_central_nodes)
        return centrality
    except Exception as e:
        logging.error(f"Error analyzing graph: {e}")
        raise

def save_graph(G, output_path):
    """
    Save the graph to a file in GraphML format.
    
    Args:
        G (nx.DiGraph): Directed graph to save.
        output_path (str): Path to save the graph file.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        nx.write_graphml(G, output_path)
        logging.info(f"Graph successfully saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving graph: {e}")
        raise

def main(input_file, graph_output_file):
    """
    Main function to execute the graph modeling pipeline.
    
    Args:
        input_file (str): Path to the cleaned transaction data CSV file.
        graph_output_file (str): Path to save the graph in GraphML format.
    """
    logging.info("Starting graph modeling process")
    try:
        data = load_cleaned_data(input_file)
        G = build_graph(data)
        analyze_graph(G)
        save_graph(G, graph_output_file)
        logging.info("Graph modeling process completed successfully")
    except Exception as e:
        logging.error(f"Graph modeling process failed: {e}")

if __name__ == "__main__":
    # Define file paths
    INPUT_FILE = "../data/processed/transactions_cleaned.csv"
    GRAPH_OUTPUT_FILE = "../graphs/transaction_graph.graphml"
    
    # Run the graph modeling pipeline
    main(INPUT_FILE, GRAPH_OUTPUT_FILE)
