import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

data = pd.read_csv('/TRADING2023/STOCKA/A.csv')  

data['Date'] = pd.to_datetime(data['Date'])

data.set_index('Date', inplace=True)

data['Closing Rate'] = data['Closing Rate'].interpolate(method='time')