import requests
from bs4 import BeautifulSoup

def search_yahoo(keyword):

    url = f"https://auctions.yahoo.co.jp/search/search?p={keyword}&fixed_price=1"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    items = []

    try:

        r = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        listings = soup.select("li.Product")

        for item in listings[:10]:

            try:

                title = item.select_one("h3").text.strip()

                price = item.select_one(".Product__priceValue").text
                price = int(price.replace("円","").replace(",",""))

                link = item.select_one("a")["href"]

                items.append({
                    "title": title,
                    "price": price,
                    "url": link
                })

            except:
                pass

    except:
        pass

    return items
