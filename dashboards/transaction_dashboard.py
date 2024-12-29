from dash import Dash, dcc, html
import plotly.graph_objs as go

def create_dashboard(graph):
    app = Dash(__name__)

    # Convert graph to Plotly data
    edge_x, edge_y = [], []
    pos = nx.spring_layout(graph)
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x, node_y = zip(*[pos[n] for n in graph.nodes])
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=list(graph.nodes),
        marker=dict(size=10, color="skyblue"),
        textposition="top center"
    )

    fig = go.Figure(data=[edge_trace, node_trace])

    app.layout = html.Div([
        dcc.Graph(figure=fig)
    ])

    app.run_server(debug=True)
