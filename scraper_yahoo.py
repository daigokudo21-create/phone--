import requests
from bs4 import BeautifulSoup

def search_yahoo(keyword):

    url = f"https://auctions.yahoo.co.jp/search/search?p={keyword}&fixed_price=1"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    items = []

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        listings = soup.select("li.Product")

        for item in listings:

            title_tag = item.select_one("h3")
            price_tag = item.select_one(".Product__priceValue")
            link_tag = item.select_one("a")

            if title_tag and price_tag and link_tag:

                title = title_tag.text.strip()

                price_text = price_tag.text.replace("円","").replace(",","")

                try:
                    price = int(price_text)
                except:
                    price = 0

                url = link_tag["href"]

                items.append({
                    "title": title,
                    "price": price,
                    "url": url
                })

        return items

    except:
        return []
