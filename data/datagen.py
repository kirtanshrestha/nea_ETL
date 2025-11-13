import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

provinces = ["Bagmati", "Gandaki", "Koshi", "Lumbini", "Madhesh", "Karnali", "Sudurpashchim"]

os.makedirs("raw", exist_ok=True)

# Start and end dates (last 90 days)
end_date = datetime.now()
start_date = end_date - timedelta(days=90)

# Generate daily files
for i in range(91):
    date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
    data = []
    for province in provinces:
        base_consumption = np.random.uniform(100, 400)
        variation = np.random.uniform(-20, 20)
        consumption = round(base_consumption + variation, 2)
        peak_load = round(consumption * np.random.uniform(0.6, 1.5), 2)
        outages = np.random.randint(0, 4)
        data.append([date, province, consumption, peak_load, outages])

    df = pd.DataFrame(
        data,
        columns=["date", "province", "consumption_mwh", "peak_load_mw", "outages"]
    )

    file_path = f"data/raw/nea_data_{date}.csv"
    df.to_csv(file_path, index=False)

print("Generated!")
