import pandas as pd
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        """Load dataset from CSV file."""
        self.data = pd.read_csv(self.filepath)
        return self.data

    def clean_data(self):
        """Simple cleaning: remove rows with missing values."""
        self.data = self.data.dropna()
        return self.data

    def split(self, target="target", test_size=0.2, random_state=42):
        """Split dataset into train and test sets."""
        X = self.data.drop(columns=[target])
        y = self.data[target]
        return train_test_split(X, y, test_size=test_size, random_state=random_state)
