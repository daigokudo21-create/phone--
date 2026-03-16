from flask import Flask, render_template
from scraper_yahoo import get_yahoo_items
from damage_classifier import classify
from parts_db import get_part
from mercari_price import get_price
from profit_calc import calc

app = Flask(__name__)

def detect_model(title):

    t = title.lower()

    models = [
        "iphone15",
        "iphone14",
        "iphone13",
        "iphone12",
        "iphone11",
        "iphonex",
        "iphone8"
    ]

    for m in models:
        if m in t:
            return m

    return None


@app.route("/")
def home():

    auctions = get_yahoo_items()

    results = []

    for a in auctions:

        model = detect_model(a["title"])
        if not model:
            continue

        damage = classify(a["title"])
        if not damage:
            continue

        part_price = get_part(model, damage)
        if not part_price:
            continue

        mercari_price = get_price(model)
        if not mercari_price:
            continue

        profit = calc(a["price"], part_price, mercari_price)

        if profit > 2000:

            results.append({
                "title": a["title"],
                "profit": profit,
                "url": a["url"]
            })

    results.sort(key=lambda x: x["profit"], reverse=True)

    return render_template("index.html", items=results)


app.run(host="0.0.0.0", port=10000)