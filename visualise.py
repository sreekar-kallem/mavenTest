import matplotlib.pyplot as plt
from dataset import *

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label='Closing Rate')
plt.title('Stock Closing Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Rate')
plt.legend()
plt.show()
