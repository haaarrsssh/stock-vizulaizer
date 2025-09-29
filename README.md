# Stock Visualizer V1.0

A simple stock price visualization tool that creates candlestick charts using Python and Tkinter.

## Features

- Interactive GUI with date pickers
- Real-time stock data from Yahoo Finance
- Candlestick chart visualization
- Error handling and validation
- Dark theme charts

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python stock_visualizer.py
```

2. Enter a stock ticker symbol (e.g., AAPL, MSFT, GOOGL)
3. Select start and end dates
4. Click "Visualize" to generate the candlestick chart

## Recent Fixes

### Data Type Errors
- **Problem**: The original code had issues with non-numeric data in OHLC columns
- **Solution**: Added proper data cleaning with `pd.to_numeric()` and `dropna()` to handle NaN values and convert data to proper numeric types

### Error Handling
- **Problem**: No validation for empty tickers, failed downloads, or invalid date ranges
- **Solution**: Added comprehensive error handling with user-friendly message boxes for:
  - Empty ticker symbols
  - Invalid date ranges
  - Failed data downloads
  - Missing or invalid data columns
  - Empty datasets

### Dependencies
- **Problem**: Missing dependency checks
- **Solution**: Added try-catch for `tkcalendar` import with helpful error message

### User Experience
- **Problem**: No default values or helpful guidance
- **Solution**: Added:
  - Default ticker symbol (AAPL)
  - Helpful text with examples
  - Better window sizing
  - Improved layout with proper spacing

## Requirements

- Python 3.7+
- yfinance
- matplotlib
- mplfinance
- pandas
- numpy
- tkcalendar

## Troubleshooting

### Common Issues

1. **"tkcalendar not installed" error**
   - Solution: Run `pip install tkcalendar`

2. **"No data found" error**
   - Check if the ticker symbol is correct
   - Try a different date range
   - Some stocks may not have data for certain periods

3. **Chart not displaying**
   - Ensure you have a valid internet connection
   - Check if the stock symbol exists on Yahoo Finance

## Example Usage

```
Ticker: AAPL
Start Date: 2024-01-01
End Date: 2024-12-31
```

This will generate a candlestick chart showing Apple's stock price for 2024.

## Technical Details

The application uses:
- **yfinance**: For downloading stock data from Yahoo Finance
- **mplfinance**: For creating professional candlestick charts
- **tkcalendar**: For date selection widgets
- **pandas**: For data manipulation and cleaning
- **matplotlib**: For chart styling and display

## Future Improvements

- Add volume charts
- Include technical indicators
- Support for multiple stocks comparison
- Export functionality
- Real-time updates
- More chart types (line, bar, etc.)

---

HARSHTYAGI (c) 2025