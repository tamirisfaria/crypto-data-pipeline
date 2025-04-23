import requests
from config.config import SERVICE_CONFIG
from datetime import datetime

def fetch_cryptos(limit=10):
    api_key = SERVICE_CONFIG['api_key']
    url = f"https://rest.coincap.io/v3/assets?limit={limit}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()['data']
    timestamp = int(response.json()['timestamp']) / 1000

    cryptos = []
    prices = []

    for item in data:
        cryptos.append({
            'id': item['id'],
            'name': item['name'],
            'symbol': item['symbol'],
            'rank': int(item['rank']),
        })

        prices.append({
            'crypto_id': item['id'],
            'price_usd': float(item['priceUsd']),
            'market_cap': float(item['marketCapUsd']),
            'volume_24h': float(item['volumeUsd24Hr']),
            'timestamp': datetime.fromtimestamp(timestamp)
        })

    return cryptos, prices
