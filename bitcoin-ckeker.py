import requests

price = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
data = requests.get(price).json()
price_in_usd = data["bpi"]["USD"]["rate"]
print(f"Bictoin price is currently: {price_in_usd}💲")

