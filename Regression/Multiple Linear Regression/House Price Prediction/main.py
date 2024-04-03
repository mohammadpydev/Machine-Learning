# Linear Regression for House Price Prediction 

# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv("Boston.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values


# Spliting the dataset into thetraining set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

# Trainig te Multiple Linear Regression mode on the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting The Test set results
y_pred = regressor.predict(x_test)


c = np.array([i for i in range(1,103,1)]).reshape(-1, 1)   
plt.plot(c,y_test, color="blue", linewidth=2.5, linestyle="-")
plt.plot(c,y_pred, color="red",  linewidth=2.5, linestyle="-")
plt.show()
