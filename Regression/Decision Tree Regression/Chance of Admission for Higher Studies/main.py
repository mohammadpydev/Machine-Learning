# Decision Tree Regression

# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv("Admission Chance.csv")
x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

# Training the Decision Tree Regression model on the whole dataset 
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(x_train, y_train)

# Predicting a new result
y_pred = regressor.predict(x_test)

# r square
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)


