import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

class IsolationForestAnomalyDetector:
    def __init__(self, contamination=0.01, random_state=42):
        self.model = IsolationForest(contamination=contamination, random_state=random_state)

    def fit(self, data):
        """Fits the Isolation Forest model on the given data."""
        self.model.fit(data)

    def predict(self, data):
        """
        Predicts anomalies on the given data.
        Returns:
            -1: Anomaly
             1: Normal
        """
        return self.model.predict(data)

    def score_samples(self, data):
        """Returns the anomaly scores for the given data."""
        return self.model.score_samples(data)

# Example usage
if __name__ == "__main__":
    # Example DataFrame
    df = pd.DataFrame({
        'amount': [100, 150, 200, 100000, 120, 180],
        'frequency': [10, 12, 14, 1, 11, 13]
    })
    
    detector = IsolationForestAnomalyDetector(contamination=0.1)
    detector.fit(df)
    df['anomaly'] = detector.predict(df)
    print(df)
