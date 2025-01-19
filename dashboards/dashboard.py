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
def main():
    st.set_page_config(page_title="Money Flow Analysis Dashboard", layout="wide")
    st.title("Money Flow Analysis Dashboard")

    # File Upload
    uploaded_file = st.file_uploader("Upload Transaction Data (CSV)", type=['csv'])
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.success("Data loaded successfully!")

        # Display data
        st.subheader("Transaction Data")
        st.dataframe(data)

        # Anomaly Visualization
        st.subheader("Anomaly Detection Visualization")
        anomaly_col = st.selectbox("Select Anomaly Column", options=data.columns)
        st.plotly_chart(plot_anomalies(data, anomaly_column=anomaly_col))

        # Column Histogram
        st.subheader("Column Histogram")
        hist_col = st.selectbox("Select Column for Histogram", options=data.columns)
        st.plotly_chart(plot_histogram(data, column=hist_col))
    else:
        st.warning("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
