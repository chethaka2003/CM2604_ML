import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo

# Adjust display options
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows (use with caution for large DataFrames)
pd.set_option('display.width', None)        # Adjust console width to fit all columns
pd.set_option('display.max_colwidth', None) # Show full content of each column

# Check the file path
file_path = r"D:\IIT\2nd Year\CM2604 ML\Coursework\bank.csv"
print(f"File path: {file_path}")  # Debug the file path

# Ensure the file path is correct and the file exists
try:
    data = pd.read_csv(file_path, delimiter=';', quotechar='"')
    print("Data loaded successfully!")
    print(data.head())  # Display the first few rows
except FileNotFoundError:
    print("Error: File not found. Check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

data = pd.read_csv(file_path, delimiter=';', quotechar='"')

# Step 2: Save the cleaned data (optional)
output_path = "cleaned_dataset.csv"
data.to_csv(output_path, index=False)

print("Data cleaned successfully!")
print(data.head())  # Display the first few rows of the cleaned data
