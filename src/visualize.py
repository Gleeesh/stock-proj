import matplotlib.pyplot as plt

def plot_price(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["Close"], label="Close Price")
    plt.title("Stock Closing Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
