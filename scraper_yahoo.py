import requests
from bs4 import BeautifulSoup

def get_yahoo_items():

    url = "https://auctions.yahoo.co.jp/search/search?p=iphone+ジャンク"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    items = []

    listings = soup.select("li.Product")

    for item in listings:

        title_tag = item.select_one("h3.Product__title")
        price_tag = item.select_one("span.Product__priceValue")
        link_tag = item.select_one("a")

        if not title_tag or not price_tag:
            continue

        title = title_tag.text.strip()

        price = price_tag.text.replace("円", "").replace(",", "")

        try:
            price = int(price)
        except:
            continue

        url = "https://auctions.yahoo.co.jp" + link_tag["href"]

        items.append({
            "title": title,
            "price": price,
            "url": url
        })

    return items