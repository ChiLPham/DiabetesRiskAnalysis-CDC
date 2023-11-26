import pandas as pd

def load_data():
    # Load the data from CSV files
    X = pd.read_csv('data/diabetes_features.csv')
    y = pd.read_csv('data/diabetes_targets.csv')

    # Print the column names
    print("Features DataFrame column names:", X.columns)
    print("Targets DataFrame column names:", y.columns)

    return X, y