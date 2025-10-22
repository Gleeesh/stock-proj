import os
import yfinance as yf
import pandas as pd
from .config import TICKER, START_DATE, END_DATE, DATA_PATH

def fetch_stock_data():
    print(f"📈 Downloading data for {TICKER} from {START_DATE} to {END_DATE}")
    df = yf.download(TICKER, start=START_DATE, end=END_DATE)

    # ✅ Auto-create the folder if missing
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    df.to_csv(DATA_PATH)
    print(f"✅ Data saved to {DATA_PATH}")
    return df

if __name__ == "__main__":
    fetch_stock_data()
