from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("data/small_version.csv")
print(data.head())


# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

time = data['Timestamp'].map(datetime.fromtimestamp)
open_price = data['Open']

fig, ax = plt.subplots()
ax.plot(time, open_price)

ax.set(xlabel='time (minutes)', ylabel='Opening price (USD)',
       title='TAK CO JE!!!')
ax.grid()
plt.show()