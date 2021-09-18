from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_profit_each_day = [0] * len(prices)
    min_price = float('inf')
    max_prof_so_far = 0
    for i,v in enumerate(prices):
        min_price = min(min_price, v)
        max_profit_each_day[i] = max(prices[i] - min_price, max_prof_so_far)
        max_prof_so_far = max_profit_each_day[i]

    max_sell_price = float('-inf')
    max_prof = 0
    for i in reversed(range(len(prices))):
        max_sell_price = max(max_sell_price, prices[i])
        max_prof = max(max_prof, max_sell_price - prices[i] + max_profit_each_day[i])
    return max_prof



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
