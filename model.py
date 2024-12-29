import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# Adjust display options
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows (use with caution for large DataFrames)
pd.set_option('display.width', None)        # Adjust console width to fit all columns
pd.set_option('display.max_colwidth', None) # Show full content of each column


file_path = r"D:\IIT\2nd Year\CM2604 ML\Coursework\bank-full.csv"

# Create the CSV file data into correct columns
data = pd.read_csv(file_path, delimiter=';', quotechar='"')
print("Data loaded successfully!")
print(data.head(20))

# get the columns and rows available
print(data.shape)

# check weather data is balance or not
no_count = (data['y'] == 'no').sum()
print(f"Number of values which has no = {no_count}")

yes_count = (data['y'] == 'yes').sum()
print(f"Number of values which has yes = {yes_count}")

# According to above information we can see that dataset is Unbalance

# check if null values are available or not
print(data.info())

# plot the data unbalance
y = [yes_count,no_count]
x = ['yes','no']
inBlncFig,inBlncPlt = plt.subplots()
inBlncPlt.bar(x, y, color=['green', 'red'])
inBlncPlt.set_title('Unbalance dataset')
inBlncFig.show()
plt.pause(5)

# Data Preprocess

# check the unique values in each column
for col in data.columns:
    print(col)
    print(data[col].unique())

