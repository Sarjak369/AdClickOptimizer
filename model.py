# Importing the libraries
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv(r'Dataset/advertising.csv')


X = dataset[['Daily Time Spent on Site', 'Age',
             'Area Income', 'Daily Internet Usage', 'Male']]
y = dataset['Clicked on Ad']

# Splitting Training and Test Set

regressor = LogisticRegression(max_iter=500)

# Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
# print(model.predict([[30, 45, 60000, 300, 1]]))


# Create input data with feature names
input_data = pd.DataFrame([[30, 45, 60000, 300, 1]], columns=[
                          'Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male'])

# Predict using the model
print(model.predict(input_data))
