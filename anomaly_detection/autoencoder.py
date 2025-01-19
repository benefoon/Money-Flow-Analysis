import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

class AutoEncoderAnomalyDetector:
    def __init__(self, input_dim, encoding_dim):
        input_layer = Input(shape=(input_dim,))
        encoded = Dense(encoding_dim, activation='relu')(input_layer)
        decoded = Dense(input_dim, activation='sigmoid')(encoded)

        self.autoencoder = Model(inputs=input_layer, outputs=decoded)
        self.autoencoder.compile(optimizer='adam', loss='mse')

    def fit(self, data, epochs=50, batch_size=32):
        """Trains the AutoEncoder model."""
        self.autoencoder.fit(data, data, epochs=epochs, batch_size=batch_size, shuffle=True, verbose=1)

    def reconstruct(self, data):
        """Reconstructs the input data."""
        return self.autoencoder.predict(data)

    def compute_anomaly_score(self, data):
        """Computes anomaly scores based on reconstruction error."""
        reconstructed = self.reconstruct(data)
        return np.mean(np.power(data - reconstructed, 2), axis=1)

# Example usage
if __name__ == "__main__":
    # Example DataFrame
    df = pd.DataFrame({
        'amount': [100, 150, 200, 100000, 120, 180],
        'frequency': [10, 12, 14, 1, 11, 13]
    })

    detector = AutoEncoderAnomalyDetector(input_dim=2, encoding_dim=1)
    detector.fit(df.values, epochs=20)
    df['anomaly_score'] = detector.compute_anomaly_score(df.values)
    print(df)
