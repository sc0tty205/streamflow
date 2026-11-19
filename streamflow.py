import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
from pathlib import Path


def load_streamflow(filename):
    """Read the streamflow CSV and return dates and flows in cfs."""
    data = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        dtype=str
    )

    dates = np.array([
        datetime.strptime(date, "%m/%d/%y %H:%M")
        for date in data[:, 0]
    ])
    flows = data[:, 1:].astype(float)

    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge."""
    fig, ax = plt.subplots(figsize=(7, 6))

    for index, site in enumerate(sites):
        ax.plot(dates, flows[:, index], label=site, linewidth=2)

    ax.set_title("Provo River Streamflow Data (June 2021)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Flowrate (cfs)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()



sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
csv_path = Path(__file__).with_name(
        "June-2021-Provo-River-Streamflow-Rates (2).csv"
    )
dates, flows = load_streamflow(csv_path)

# I used AI to help me write the summarize function. I made my own twerks and then used AI to clear it and fix any errors such as why the file was not being uploaded.
def summarize(dates, flows, sites):
# Gauge        Max (cfs)   Date of max      Min (cfs) Avg (cfs)
# 10163000      131.0    2021-06-01 08:15     35.6      57.0
    print(f"{'Gauge':<12}{'Max (cfs)':>10}   "
          f"{'Date of max':<16}{'Min (cfs)':>10}{'Avg (cfs)':>10}")

    for index, site in enumerate(sites):
        gauge_flows = flows[:, index]
        max_index = np.argmax(gauge_flows)
        max_flow = gauge_flows[max_index]
        max_date = dates[max_index]
        min_flow = np.min(gauge_flows)
        average_flow = np.mean(gauge_flows)

        print(f"{site:<12}{max_flow:>10.1f}   "
              f"{max_date.strftime('%Y-%m-%d %H:%M'):<16}"
              f"{min_flow:>10.1f}{average_flow:>10.1f}")


    with open("streamflow_summary.csv", "w", newline="") as file:
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

summarize(dates, flows, sites)

#I used AI to create the function for me because it was difficult for me to come up with it from the top of my mind. After AI created the code I reviewed it and connected it to the steps to make sure it aligns with the steps in the homework.
#Here is the setup for the flow threshold.
threshold = float(input("Enter a flow threshold in cfs: "))

#The print statement for reported hours above the threshold.
print(f"\nHours above {threshold:.1f} cfs:")

#The settings for the reading thresholds
for index, site in enumerate(sites):
    readings_above_threshold = flows[:, index] > threshold
    hours_above_threshold = np.sum(readings_above_threshold) * 0.25
    print(f"{site}: {hours_above_threshold:.2f} hours")

