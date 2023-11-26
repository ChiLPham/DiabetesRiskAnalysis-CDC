import pandas as pd
from exploratory_data_analysis import calculate_correlations, demographic_analysis, plot_histograms
from predictive_analysis import perform_predictive_analysis
from utils import load_data
import os
import joblib

def main():
    X, y = load_data()

    calculate_correlations(X)
    demographic_analysis(X, y)
    plot_histograms(X)

    perform_predictive_analysis()

    # If a command-line argument is provided, use it as the file path for new data
    if len(sys.argv) > 1:
        predict_new_data(sys.argv[1])


if __name__ == '__main__':  
    main()