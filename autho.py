import pandas as pd

# Load data
df = pd.read_csv("hvac_dataset.csv", parse_dates=['Local Time (Timezone : GMT+8h)'])
df = df.set_index('Local Time (Timezone : GMT+8h)')
df = df.sort_index()

# CRITICAL: For energy in kWh → you must SUM over the hour, NOT mean
# Because each row is energy consumed in 30 minutes → two rows = one full hour
target_hourly = df['Chiller Energy Consumption (kWh)'].resample('h').sum()

# Remove any incomplete hours (e.g. last partial hour)
target_hourly = target_hourly.dropna()

print(f"Final hourly series: {len(target_hourly)} points")
print(f"Date range: {target_hourly.index.min()} → {target_hourly.index.max()}")

print("\n" + "="*50)
print("FINAL CORRECT HOURLY AUTOCORRELATION (kWh)")
print("="*50)
for lag in [1, 6, 12, 24, 48, 72]:
    ac = target_hourly.autocorr(lag=lag)
    print(f"Lag {lag:2d}h → {ac:.3f}")