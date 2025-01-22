import os
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("ml_training.log"),
        logging.StreamHandler()
    ]
)

def load_data(file_path):
    """
    Load normalized transaction data from a CSV file.
    
    Args:
        file_path (str): Path to the normalized data file.
    
    Returns:
        pd.DataFrame: Loaded DataFrame.
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

def prepare_data(data, feature_columns, label_column):
    """
    Prepare features and labels for model training.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        feature_columns (list): List of column names to use as features.
        label_column (str): The name of the label column.
    
    Returns:
        tuple: Features (X) and labels (y) as separate DataFrames.
    """
    try:
        X = data[feature_columns]
        y = data[label_column]
        logging.info(f"Features and labels prepared with {X.shape[0]} samples")
        return X, y
    except KeyError as e:
        logging.error(f"Missing required columns: {e}")
        raise
    except Exception as e:
        logging.error(f"Error preparing data: {e}")
        raise

def train_model(X_train, y_train, n_estimators=100, random_state=42):
    """
    Train a Random Forest Classifier.
    
    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training labels.
        n_estimators (int): Number of trees in the forest.
        random_state (int): Random state for reproducibility.
    
    Returns:
        RandomForestClassifier: Trained model.
    """
    try:
        model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        model.fit(X_train, y_train)
        logging.info("Model training completed")
        return model
    except Exception as e:
        logging.error(f"Error during model training: {e}")
        raise

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model and log performance metrics.
    
    Args:
        model: Trained model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test labels.
    """
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        logging.info(f"Model Accuracy: {accuracy}")
        logging.info(f"Classification Report:\n{report}")
    except Exception as e:
        logging.error(f"Error during model evaluation: {e}")
        raise

def save_model(model, output_path):
    """
    Save the trained model to a file.
    
    Args:
        model: Trained model.
        output_path (str): Path to save the model file.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        joblib.dump(model, output_path)
        logging.info(f"Model successfully saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving model: {e}")
        raise

def main(data_file, model_output_path):
    """
