import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def calculate_correlations(X):
    # Calculate correlations and round to 2 decimal places
    correlation_matrix = np.around(X.corr(), decimals=2)

    # Plot heatmap of correlation matrix
    plt.figure(figsize=(20, 20))  # Increase figure size
    sns.heatmap(correlation_matrix, annot=True, cmap=plt.cm.Reds, linewidths=0.5)

    # Name the axes
    plt.xlabel('Features')
    plt.ylabel('Features')

    plt.show()

def demographic_analysis(X, y):
    # Get column names in the DataFrame
    demographics = ['Age', 'Sex', 'Income']

    # Combine features and target into a single DataFrame for demographic analysis
    df = pd.concat([X, y], axis=1)

    for demo in demographics:
        print(df.groupby(demo)['Diabetes_binary'].mean())  # target column name

def plot_histograms(X):
    # Plot histogram of each feature
    fig = X.hist(figsize=(20, 20))  # Increase figure size

    # Loop through each axes (histogram)
    for ax in fig.ravel():
        # Set title
        ax.set_title(ax.get_title(), fontsize=10)

        # Set x and y axes labels
        ax.set_xlabel("Value", fontsize=8)
        ax.set_ylabel("Frequency", fontsize=8)

        # Rotate x-axis labels for better readability
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)

    plt.tight_layout()
    plt.show()
