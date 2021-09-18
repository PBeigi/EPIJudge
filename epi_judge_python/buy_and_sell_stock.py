from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price = float('inf')
    max_prof = 0
    for i,v in enumerate(prices):
        max_prof = max(max_prof, v - min_price)
        min_price = min(min_price, v)
    return max_prof


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
