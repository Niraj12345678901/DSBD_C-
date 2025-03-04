import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('student_performance.csv')

# display data frame 
print('DATA Frame : Student Performance')
print(dataset)
print()

# check null values in data frame
print('Checking null values in data frame')
print(dataset.isnull())
print()

# To create a series true for NaN values for specific columns
print(dataset[pd.isnull(dataset['math_score'])])
print()
print(dataset[pd.isnull(dataset['reading_score'])])
print()
print(dataset[pd.isnull(dataset['writing_score'])])
print()
print(dataset[pd.isnull(dataset['palcement_score'])])
print()
print(dataset[pd.isnull(dataset['club_join_year'])])
print()
print(dataset[pd.isnull(dataset['placement_offer_count'])])
print()

# checking for missing values using notnull()
print('Checking for missing values using notnull()')
print(dataset.notnull())
print()

# replacing missing values
print('Replacing missing values')
missing_vals = ['NaN','Na','na']
dataset2 = pd.read_csv('student_performance.csv', na_values = missing_vals)
print(dataset2)
print()

# filling missing values with 0
print('Filling missing values with 0')
ndf = dataset2
print(ndf.fillna(0))
print()

# filling missing values using mean, median and standard deviation of that column
print('Filling missing values using mean, median and standard deviation of that column ')
ndf['math_score'] = ndf['math_score'].fillna(ndf['math_score'].mean())
print()
ndf['reading_score'] = ndf['reading_score'].fillna(ndf['reading_score'].median())
print()
ndf['writing_score'] = ndf['writing_score'].fillna(ndf['writing_score'].std())
print()
ndf['club_join_year'] = ndf['club_join_year'].fillna(ndf['club_join_year'].median())
print()
ndf['mpalcement_scoreath_score'] = ndf['palcement_score'].fillna(ndf['palcement_score'].mean())
print()
ndf['placement_offer_count'] = ndf['placement_offer_count'].fillna(ndf['placement_offer_count'].median())
print()

# drop rows with at least 1 null value
print('Drop rows with at least 1 null value')
print(dataset.dropna())
print()

# Drop rows if all values in that row are missing
print('Drop rows if all values in that row are missing')
print(dataset.dropna(how = 'all'))
print()

# Drop columns with at least 1 null value
print('Drop columns with at least 1 null value') 
print(ndf.dropna(axis = 1))
print()


# Detecting outliers using Boxplot:
print('Detecting outliers using Boxplot')
col = ['math_score','reading_score','writing_score','palcement_score','club_join_year','placement_offer_count']
print(dataset.boxplot(col))
print()

# print the outliers for each column with reference to the box plot.
print('Printing the outliers for each column with reference to the box plot.')
print(np.where(dataset['math_score']>90))
print(np.where(dataset['reading_score']<25))
print(np.where(dataset['writing_score']<30))
print()




