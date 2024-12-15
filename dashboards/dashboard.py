from flask import Flask, render_template, request
import pandas as pd
import networkx as nx
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_data():
    file = request.files['file']
    data = pd.read_csv(file)
    
    # Example visualization
    G = nx.DiGraph()
    for _, row in data.iterrows():
        G.add_edge(row['sender'], row['receiver'], amount=row['amount'])
    info = nx.info(G)
    
    return render_template('dashboard.html', graph_info=info)

if __name__ == '__main__':
    app.run(debug=True)
