import pytest
import pandas as pd
from src.data_processing import clean_data, normalize_data

def test_clean_data():
    """Tests the cleaning functionality."""
    data = pd.DataFrame({
        'sender': ['A', 'B', None],
        'receiver': ['C', 'D', 'E'],
        'amount': [100, -50, 200],
        'time': ['2024-12-15', '2024-12-16', '2024-12-17']
    })
    cleaned_data = clean_data(data)
    assert cleaned_data.isnull().sum().sum() == 0, "Null values should be removed."
    assert all(cleaned_data['amount'] >= 0), "Amounts should be absolute."

def test_normalize_data():
    """Tests the normalization functionality."""
    data = pd.DataFrame({'amount': [100, 200, 300]})
    normalized_data = normalize_data(data)
    assert normalized_data['amount'].max() == 1.0, "Normalized maximum should be 1.0."
