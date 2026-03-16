import requests
from bs4 import BeautifulSoup

def get_price(model):

    url = f"https://jp.mercari.com/search?keyword={model}&status=sold_out"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    prices = []

    try:

        r = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        for p in soup.select("span[data-testid='price']"):

            try:
                price = int(p.text.replace("¥","").replace(",",""))
                prices.append(price)
            except:
                pass

    except:
        return 0

    if len(prices) == 0:
        return 0

    prices.sort()

    avg = sum(prices[:10]) / min(len(prices),10)

    return int(avg)
