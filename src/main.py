from data_processing import DataProcessor
from model_training import ModelTrainer
from app import AppInterface

def main():
    processor = DataProcessor("data/heart.csv")
    processor.load_data()
    processor.clean_data()
    X_train, X_test, y_train, y_test = processor.split()
    trainer = ModelTrainer()
    trainer.train(X_train, y_train)
    acc, cm, report = trainer.evaluate(X_test, y_test)
    app = AppInterface(trainer)
    app.run()
main()