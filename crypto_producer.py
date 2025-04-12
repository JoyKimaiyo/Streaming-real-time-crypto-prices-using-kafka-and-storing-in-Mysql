import requests
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_coincap():
    try:
        response = requests.get("https://api.coincap.io/v2/assets?ids=bitcoin,ethereum")
        response.raise_for_status()
        data = response.json()
        if isinstance(data.get("data"), list):
            return {asset['id']: {'usd': float(asset['priceUsd'])} for asset in data["data"]}
    except Exception as e:
        print("CoinCap Error:", e)
    return None

def fetch_coingecko():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd")
        response.raise_for_status()
        data = response.json()
        return {coin: {'usd': price['usd']} for coin, price in data.items()}
    except Exception as e:
        print("CoinGecko Error:", e)
    return None

while True:
    prices = fetch_coincap() or fetch_coingecko()
    
    if prices:
        producer.send('crypto-data', value=prices)
        print("Sent:", prices)
    else:
        print("Failed to fetch prices from all APIs")

    time.sleep(10)

