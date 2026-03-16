def calc(buy_price, part_price, mercari_price):

    sell_price = mercari_price * 0.9

    mercari_fee = sell_price * 0.10

    shipping = 300

    profit = sell_price - mercari_fee - shipping - buy_price - part_price

    return int(profit)