# main.py

import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def fetch_stock_data(ticker="AAPL"):
    print(f"[INFO] Fetching data for: {ticker}")
    stock = yf.Ticker(ticker)
    hist = stock.history(period="7d", interval="1h")  # last 7 days, hourly data

    # Reset index so Date becomes a column
    hist.reset_index(inplace=True)

    # Add a timestamp column for tracking when the data was fetched
    hist["Fetched_At"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Save the data
    filename = f"data/stock_data_{ticker}.csv"
    hist.to_csv(filename, index=False)

    print(f"[SUCCESS] Data saved to {filename}")
    return hist

if __name__ == "__main__":
    fetch_stock_data("AAPL")
