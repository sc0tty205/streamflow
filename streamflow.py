import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
from pathlib import Path

csv_path = Path(__file__).with_name(
    "June-2021-Provo-River-Streamflow-Rates (2).csv"
)

data = np.genfromtxt(
    csv_path,
    delimiter=",",
    skip_header=1,
    dtype=str
)

x = np.array([
    datetime.strptime(date, "%m/%d/%y %H:%M")
    for date in data[:, 0]
])

y_1 = data[:, 1].astype(float)  
y_2 = data[:, 2].astype(float)  
y_3 = data[:, 3].astype(float)  
y_4 = data[:, 4].astype(float)  
y_5 = data[:, 5].astype(float)  

import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(7, 6))


ax.plot(x, y_1, label="10163000", linewidth=2)
ax.plot(x, y_2, label="10155200", linewidth=2)
ax.plot(x, y_3, label="10155500", linewidth=2)
ax.plot(x, y_4, label="10154200", linewidth=2)
ax.plot(x, y_5, label="10155000", linewidth=2)

ax.set_title("Provo River Streamflow Data (June 2021)")
ax.set_xlabel("Date")
ax.set_ylabel("Flowrate (cfs)")
ax.legend()
ax.grid(True, alpha=0.3)

ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

