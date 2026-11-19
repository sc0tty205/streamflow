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
plot_streamflow(dates, flows, sites)