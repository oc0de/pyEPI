import sys

def buy_sell_stock_once(prices):
    min_price, max_profit = float('inf'), 0.0

    for p in prices:
        max_profit = max(max_profit, p - min_price)
        min_price = min(min_price, p)

    return max_profit


def main():
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    result = buy_sell_stock_once(prices)

    print result


if __name__ == '__main__':
    main()
