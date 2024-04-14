from statsmodels.tsa.arima.model import ARIMA
from dataset import *

model = ARIMA(data['Closing Rate'], order=(5, 1, 0))
arima_results = model.fit()

forecast = arima_results.forecast(steps=1)

print(forecast)
