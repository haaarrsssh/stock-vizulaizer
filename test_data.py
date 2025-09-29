import yfinance as yf
import pandas as pd
import datetime as dt

# Test data download
ticker = "AAPL"
start = dt.datetime(2024, 1, 1)
end = dt.datetime(2024, 12, 31)

print(f"Downloading data for {ticker}...")
data = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)

print(f"Data shape: {data.shape}")
print(f"Data columns: {data.columns.tolist()}")
print(f"Data types: {data.dtypes}")
print(f"Data head:\n{data.head()}")

# Check if it's a MultiIndex DataFrame
if isinstance(data.columns, pd.MultiIndex):
    print("\nMultiIndex DataFrame detected!")
    print(f"Column levels: {data.columns.levels}")
    print(f"Column names: {data.columns.names}")
    
    # Flatten the columns if needed
    if len(data.columns.levels) > 1:
        data.columns = data.columns.get_level_values(0)
        print(f"Flattened columns: {data.columns.tolist()}")

# Check for any non-numeric values
required_columns = ['Open', 'High', 'Low', 'Close']
for col in required_columns:
    if col in data.columns:
        print(f"\n{col} column:")
        print(f"  Type: {data[col].dtype}")
        print(f"  Sample values: {data[col].head().tolist()}")
        print(f"  Has NaN: {data[col].isna().any()}")
        print(f"  Has non-numeric: {pd.to_numeric(data[col], errors='coerce').isna().any()}")
    else:
        print(f"\n{col} column not found!")

# Test data cleaning
print("\n--- Testing data cleaning ---")
data_clean = data[required_columns].copy()
data_clean = data_clean.dropna()

for col in required_columns:
    data_clean[col] = pd.to_numeric(data_clean[col], errors='coerce')

data_clean = data_clean.dropna()

print(f"After cleaning - shape: {data_clean.shape}")
print(f"After cleaning - types: {data_clean.dtypes}")
print(f"After cleaning - head:\n{data_clean.head()}") 