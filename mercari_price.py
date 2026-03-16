import requests
import statistics

def get_price(model):

    url = f"https://api.mercari.com/items/search?keyword={model}&status=on_sale"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    try:
        data = r.json()
    except:
        return None

    prices = []

    for item in data.get("data", [])[:20]:

        price = item.get("price")

        if price:
            prices.append(price)

    if len(prices) < 5:
        return None

    median_price = statistics.median(prices)

    return median_price