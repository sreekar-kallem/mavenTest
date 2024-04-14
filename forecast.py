from dataset import *

# Splitting data into train and test sets
train_size = int(len(data) * 0.8)
train_data, test_data = data.iloc[:train_size], data.iloc[train_size:]

# Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(np.array(range(train_size)).reshape(-1, 1), train_data['Closing Rate'])
lr_pred = lr_model.predict(np.array(range(train_size, len(data))).reshape(-1, 1))

# Random Forest Regression Model
rf_model = RandomForestRegressor(n_estimators=100)
rf_model.fit(np.array(range(train_size)).reshape(-1, 1), train_data['Closing Rate'])
rf_pred = rf_model.predict(np.array(range(train_size, len(data))).reshape(-1, 1))

# Evaluation
test_size = len(test_data)
test_range = range(train_size, train_size + test_size)

plt.figure(figsize=(10, 6))
plt.plot(data.index[:train_size], train_data['Closing Rate'], label='Train Data')
plt.plot(data.index[test_range], test_data['Closing Rate'], label='Test Data')
plt.plot(data.index[test_range], lr_pred, label='Linear Regression Forecast', linestyle='--')
plt.plot(data.index[test_range], rf_pred, label='Random Forest Forecast', linestyle='--')
plt.title('Stock Price Forecast')
plt.xlabel('Date')
plt.ylabel('Closing Rate')
plt.legend()
plt.show()

# Calculate RMSE for evaluation
lr_rmse = mean_squared_error(test_data['Closing Rate'], lr_pred, squared=False)
rf_rmse = mean_squared_error(test_data['Closing Rate'], rf_pred, squared=False)

print(f"Linear Regression RMSE: {lr_rmse}")
print(f"Random Forest RMSE: {rf_rmse}")
