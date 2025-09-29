'''
HARSHTYAGI (c) 2025
Stock Visualizer V1.0

This is the very first prototype and the code is not very clean
Also there may be a couple of bugs
A lot of exceptions are not handled
'''

# Imports
from tkinter import *
from tkinter import messagebox
import datetime as dt
import pandas as pd
import numpy as np

try:
    from tkcalendar import DateEntry
except ImportError:
    messagebox.showerror("Error", "tkcalendar not installed. Please install it with: pip install tkcalendar")
    exit()

import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

'''
Function for visualizing stock data
Using Candlestick Charts
'''
def visualize():
    try:
        # Get ticker symbol and validate
        ticker = text_ticker.get().strip().upper()
        if not ticker:
            messagebox.showerror("Error", "Please enter a ticker symbol")
            return

        # Get Dates From DateEntry and Convert It To Datetime
        from_date = cal_from.get_date()
        to_date = cal_to.get_date()

        # Validate date range
        if from_date >= to_date:
            messagebox.showerror("Error", "Start date must be before end date")
            return

        start = dt.datetime(from_date.year, from_date.month, from_date.day)
        end = dt.datetime(to_date.year, to_date.month, to_date.day)

        # Download data with error handling
        try:
            data = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)
        except Exception as e:
            messagebox.showerror("Download Error", f"Failed to download data for {ticker}: {str(e)}")
            return

        # Check if data is empty
        if data.empty:
            messagebox.showerror("Error", f"No data found for {ticker} in the specified date range")
            return

        # Check if required columns exist
        required_columns = ['Open', 'High', 'Low', 'Close']
        if not all(col in data.columns for col in required_columns):
            messagebox.showerror("Error", f"Missing required columns in data for {ticker}")
            return

        # Handle MultiIndex columns from yfinance
        if isinstance(data.columns, pd.MultiIndex):
            # Try to flatten by taking the first level (column name)
            if len(data.columns.levels) > 1:
                data.columns = data.columns.get_level_values(0)

        # Restructure Data Into OHLC Format and clean data
        data = data[required_columns].copy()
        
        # Remove any rows with NaN values
        data = data.dropna()
        
        # Convert to numeric, coercing errors to NaN
        for col in required_columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        
        # Remove any remaining NaN values
        data = data.dropna()
        
        if data.empty:
            messagebox.showerror("Error", f"No valid numeric data found for {ticker}")
            return

        # Ensure all data is float type
        for col in required_columns:
            data[col] = data[col].astype(float)
        
        # Verify data types
        for col in required_columns:
            if not pd.api.types.is_numeric_dtype(data[col]):
                messagebox.showerror("Error", f"Column {col} contains non-numeric data")
                return
        
        # Ensure index is datetime
        if not isinstance(data.index, pd.DatetimeIndex):
            data.index = pd.to_datetime(data.index)
        
        # Debug: Print data info
        print(f"Data shape: {data.shape}")
        print(f"Data types: {data.dtypes}")
        print(f"Data head:\n{data.head()}")
        
        # Set up the plot style
        plt.style.use('dark_background')

        # Plot The Candlestick Chart
        mpf.plot(data,
             type='candle',
             style='charles',
             title=f'{ticker} Share Price',
             volume=False,
             show_nontrading=False)
             
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Define Main Window
root = Tk()
root.title("Harshtyagi Stock Visualizer V1.0")
root.geometry("400x300")

# Add Components And Link Function
label_from = Label(root, text="From:")
label_from.pack()
cal_from = DateEntry(root, width=50, year=2010, month=1, day=1)
cal_from.pack(padx=10, pady=10)

label_to = Label(root, text="To:")
label_to.pack()
cal_to = DateEntry(root, width=50)
cal_to.pack(padx=10, pady=10)

label_ticker = Label(root, text="Ticker Symbol:")
label_ticker.pack()
text_ticker = Entry(root)
text_ticker.pack()
text_ticker.insert(0, "AAPL")  # Default ticker

btn_visualize = Button(root, text="Visualize", command=visualize)
btn_visualize.pack(pady=20)

# Add some helpful text
help_text = Label(root, text="Enter a stock ticker symbol (e.g., AAPL, MSFT, GOOGL)", 
                  font=("Arial", 8), fg="gray")
help_text.pack(pady=10)

root.mainloop()