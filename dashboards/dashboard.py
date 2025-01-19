import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(file_path):
    """Loads transaction data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def plot_anomalies(data, anomaly_column='anomaly'):
    """Plots anomalies and normal transactions."""
    fig = px.scatter(
        data,
        x='amount',
        y='frequency',
        color=anomaly_column,
        title='Transaction Anomalies',
        labels={'color': 'Anomaly'},
        template='plotly_dark'
    )
    return fig

def plot_histogram(data, column):
    """Plots a histogram for a specific column."""
    fig = px.histogram(
        data,
        x=column,
        nbins=50,
        title=f'{column} Distribution',
        template='plotly_dark'
    )
    return fig

# Streamlit App
