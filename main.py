import pandas as pd 
import numpy as np
import plotly.express as px 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('data_set.csv')

scatter_plot = px.scatter(data, x='total_bill', y='tip', title='Total Bill vs Tip Amount')
scatter_plot.show()

pie_chart = px.pie(data, names='day', title='Distribution of Days')
pie_chart.show()

X = pd.get_dummies(data.drop(columns=['tip']))
Y = data['tip']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

mse = mean_squared_error(Y_test, predictions)

print("Mean Squaewd Error:", mse)

