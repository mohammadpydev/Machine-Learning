# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv("data/tvmarketing.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1:].values

# Spliting the dataset into thetraining set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,
                                                   random_state=0)

# Training the simple Linear Regression model on training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting The Test set results
y_pred = regressor.predict(x_test)

# Coefficients Calculation
# Getting the final linear regression equation with the values of the coefficients
print(regressor.coef_)
print(regressor.intercept_)

# y = regressor.coef_ * x + regressor.intercept_


# Visualsing the Training set results
plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.title("sales based on 'TV' marketing budget (Training set)")
plt.xlabel("TV")
plt.ylabel("salary")
plt.show()

# Visualsing the Test set results
plt.scatter(x_test, y_test, color="red")
plt.plot(x_train, regressor.predict(x_train), color="blue")
plt.title("sales based on 'TV' marketing budget (Test set)")
plt.xlabel("TV")
plt.ylabel("salary")
plt.show()


c = np.array([i for i in range(1,41,1)]).reshape(-1, 1)   
plt.plot(c,y_test, color="blue", linewidth=2.5, linestyle="-")
plt.plot(c,y_pred, color="red",  linewidth=2.5, linestyle="-")
plt.show()






