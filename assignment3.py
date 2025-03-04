import pandas as  pd


# Q1: Write a Python script to download or load the dataset into a Pandas DataFrame.
csv_file = pd.read_csv("ODI_Match_Results.csv")
print(csv_file)
print()

# Q2: Load the dataset into a Pandas DataFrame and display the first five rows. What initial insights can you gather from this data?
print('Display the first five rows : ')
print(csv_file.head())
print()

# Q3: Check the number of rows and columns in the dataset using Pandas functions.
print('Number of rows and columns in the dataset : ',end = '')
print(csv_file.shape)
print()

# Q4: Identify missing values in the dataset using the isnull() function. Which columns have missing values, and how many?
print('mMissing values in the dataset : ',end='')
print(csv_file.isnull().sum())
print()

# Q5: Generate summary statistics of the dataset using the describe() function. Explain what insights you derive from the statistical summary.
print('Summary statistics of the dataset : ')
print(csv_file.describe())
print()

# Q6: List all the variable names and their data types. Provide a brief description of each variable and its significance in evaluating player performance.
print('List of all the variable names and their data types : ')
print(csv_file.dtypes)
print()

# Q7: Identify variables with incorrect data types (e.g., numerical values stored as strings). Write a Python script to convert these variables into the correct format.
print(csv_file.dtypes)
print(csv_file.head())  # Preview first few rows

# Convert numerical columns to int/float
csv_file["Margin"] = pd.to_numeric(csv_file["Margin"], errors='coerce')
csv_file["BR"] = pd.to_numeric(csv_file["BR"], errors='coerce')
csv_file["Match_ID"] = pd.to_numeric(csv_file["Match_ID"], errors='coerce')
csv_file["Country_ID"] = pd.to_numeric(csv_file["Country_ID"], errors='coerce')

# Convert 'Start Date' to datetime
csv_file["Start Date"] = pd.to_datetime(csv_file["Start Date"], errors='coerce')

# Verify changes
print(csv_file.dtypes)




