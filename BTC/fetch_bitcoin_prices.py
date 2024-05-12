import requests
import csv

def fetch_bitcoin_prices(urls):
    bitcoin_prices = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            timestamp = data[0][0]
            price = data[0][4]
            bitcoin_prices.append((timestamp, price))
        else:
            print("Error:", response.text)
    return bitcoin_prices

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Price'])
        for timestamp, price in data:
            writer.writerow([timestamp, price])

if __name__ == "__main__":
    urls = [
        "https://api.pro.coinbase.com/products/BTC-USD/candles?start=2024-04-22T19:37&end=2024-04-22T19:37&granularity=60",
        "https://api.pro.coinbase.com/products/BTC-USD/candles?start=2024-04-22T19:38&end=2024-04-22T19:38&granularity=60",
        "https://api.pro.coinbase.com/products/BTC-USD/candles?start=2024-04-22T19:39&end=2024-04-22T19:39&granularity=60",
        "https://api.pro.coinbase.com/products/BTC-USD/candles?start=2024-04-22T19:40&end=2024-04-22T19:40&granularity=60",
        "https://api.pro.coinbase.com/products/BTC-USD/candles?start=2024-04-22T19:41&end=2024-04-22T19:41&granularity=60",
        "https://api.pro.coinbase.com/products/BTC-USD/candles?start=2024-04-22T19:42&end=2024-04-22T19:42&granularity=60"
    ]
    
    bitcoin_prices = fetch_bitcoin_prices(urls)
    if bitcoin_prices:
        save_to_csv(bitcoin_prices, 'bitcoin_prices.csv')
        print("Bitcoin prices saved to bitcoin_prices.csv")
