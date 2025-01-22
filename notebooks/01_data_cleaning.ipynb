import os
import logging
import pandas as pd

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_cleaning.log"),
        logging.StreamHandler()
    ]
)

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data successfully loaded from {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def clean_data(data):
    """
    Clean the provided DataFrame.
    
    Steps:
        - Drop rows with missing values.
        - Convert negative values in the 'amount' column to positive.
    
    Args:
        data (pd.DataFrame): The DataFrame to clean.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    try:
        initial_rows = len(data)
        data.dropna(inplace=True)
        data['amount'] = data['amount'].apply(lambda x: abs(x))
        cleaned_rows = len(data)
        logging.info(f"Cleaned data: {initial_rows - cleaned_rows} rows dropped")
        return data
    except KeyError as e:
        logging.error(f"Missing required column: {e}")
        raise
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        raise

def save_data(data, output_path):
    """
    Save the cleaned DataFrame to a CSV file.
    
    Args:
        data (pd.DataFrame): The DataFrame to save.
        output_path (str): Destination file path.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_csv(output_path, index=False)
        logging.info(f"Cleaned data saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        raise

def main(input_path, output_path):
    """
    Main function to execute the data cleaning pipeline.
    
    Args:
        input_path (str): Path to the raw data CSV file.
        output_path (str): Path to save the cleaned data CSV file.
    """
    logging.info("Starting data cleaning process")
    try:
        data = load_data(input_path)
        cleaned_data = clean_data(data)
        save_data(cleaned_data, output_path)
        logging.info("Data cleaning process completed successfully")
    except Exception as e:
        logging.error(f"Data cleaning process failed: {e}")

if __name__ == "__main__":
    # Define file paths
    INPUT_FILE = "../data/raw/transactions.csv"
    OUTPUT_FILE = "../data/processed/transactions_cleaned.csv"
    
    # Run the cleaning pipeline
    main(INPUT_FILE, OUTPUT_FILE)
