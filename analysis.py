import pandas as pd
import matplotlib.pyplot as plt

def analyze_trend(filename="data/stock_data_AAPL.csv"):
    print(f"[INFO] Reading data from: {filename}")
    df = pd.read_csv(filename)

    # Convert 'Datetime' to datetime object
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df.set_index("Datetime", inplace=True)

    # Print summary stats
    print("\n📊 Summary Statistics:")
    print(df[["Open", "High", "Low", "Close"]].describe())

    # Plot the Closing Price
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], marker='o', linestyle='-', color='blue')
    plt.title("AAPL Stock Closing Price (Last 7 Days)")
    plt.xlabel("Date & Time")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()

    # Save and show the plot
    plt.savefig("data/aapl_closing_price_trend.png")
    print("[📈] Graph saved to data/aapl_closing_price_trend.png")
    plt.show()

if __name__ == "__main__":
    analyze_trend()
