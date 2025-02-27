import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('housing_price.csv')

print(df.head())  # 'View the first few rows'
print(df.describe())  # 'Get basic statistics of the dataset'
print(df.info())  # 'Check for missing values and data types'


# 'Checking for missing values'
print(df.isnull().sum())

# 'Fill missing values or drop them'
df.fillna(df.mean(), inplace=True)


# 'Convert the ocean_proximity column into numerical format using LabelEncoder'
le = LabelEncoder()
df['ocean_proximity'] = le.fit_transform(df['ocean_proximity'])


X = df.drop('median_house_value', axis=1)  # Features (independent variables)
y = df['median_house_value']  # Target variable (dependent variable)

#  'Split the dataset into training and testing sets (80% train, 20% test)'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 'Train the Linear Regression model'
model = LinearRegression()
model.fit(X_train, y_train)

#  'Make predictions'
y_pred = model.predict(X_test)

# Evaluate the model
# Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# R-squared (R²) value
r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2}')

# Plot actual vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()


# You can check the coefficients (importance) of each feature
coef_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coef_df)
