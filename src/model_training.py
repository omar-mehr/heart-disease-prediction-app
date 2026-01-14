from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class ModelTrainer:
    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)

    def train(self, X_train, y_train):
        """Train the logistic regression model."""
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """Evaluate model performance."""
        predictions = self.model.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        cm = confusion_matrix(y_test, predictions)
        report = classification_report(y_test, predictions)
        return acc, cm, report

    def predict(self, input_data):
        """Predict using the trained model."""
        return self.model.predict(input_data)[0]
