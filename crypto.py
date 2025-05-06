import requests

# Replace 'your_api_key_here' with your actual Polygon.io API key
api_key = "your_api_key_here"
url = f"https://api.polygon.io/v2/aggs/ticker/X:BTC-USD/previous?apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    prices = response.json()

    symbol = prices.get("symbol")
    open_price = prices.get("open")
    close_price = prices.get("close")
    high_price = prices.get("high")
    low_price = prices.get("low")
    volume = prices.get("volume")

    print(f"Symbol: {symbol}")
    stock_info = (symbol, open_price, close_price, high_price, low_price, volume)
else:
    print(f"Failed to fetch data: {response.status_code}, {response.text}")
