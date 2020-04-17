from typing import List


def return_change(paid: int, price: int, denominations: List[int] = [1, 2, 5, 10, 20, 50, 100]) -> List[int]:
    change = paid - price
    ret = list()
    for d in reversed(sorted(denominations)):
        while change >= d:
            change -= d
            ret.append(d)
    return ret
