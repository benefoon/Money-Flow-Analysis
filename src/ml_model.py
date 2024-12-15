import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

def load_data(file_path):
    """Loads preprocessed data for training."""
    data = pd.read_csv(file_path)
    return data

def prepare_data(data):
    """Prepares features and labels for model training."""
    X = data[['amount', 'transaction_type', 'time']]  # Add relevant features
    y = data['is_suspicious']  # Binary classification: 0 or 1
    return X, y

def train_model(X, y):
    """Trains a RandomForest model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    return model

def save_model(model, file_path):
    """Saves the trained model to a file."""
    joblib.dump(model, file_path)

if __name__ == "__main__":
    data = load_data("data/processed/transactions_normalized.csv")
    X, y = prepare_data(data)
    model = train_model(X, y)
    save_model(model, "models/suspicious_transaction_model.pkl")
