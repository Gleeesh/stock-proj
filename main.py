from src.data_fetcher import fetch_stock_data
from src.feature_engineering import add_features
from src.model_train import train_model
from src.model_predict import predict_next
from src.visualize import plot_price
import pandas as pd

def main():
    df = fetch_stock_data()
    df = add_features(df)
    df.to_csv("data/processed/stock_data.csv", index=False)
    plot_price(df)
    train_model()
    predict_next(df)

if __name__ == "__main__":
    main()
