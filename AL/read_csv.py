import pandas as pd, numpy as np
from matplotlib import pyplot as plt
filepath = 'Vitals/pulse.csv'
data = pd.read_csv(filepath)

#number of bars
n = 2308

fig, ax = plt.subplots()
ax.bar(np.arange(n),data.value.iloc[:n])

ax.set_xticks(np.arange(n))
#ax.set_xticklabels(data.timestamp.iloc[:n], rotation=90)
ax.set(xlabel = 'timestamp', ylabel = 'value', title = 'Pulse')

plt.tight_layout()
plt.show()
