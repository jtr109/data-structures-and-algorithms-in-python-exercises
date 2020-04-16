from typing import List


def separate_odd_product_exists(data: List[int]) -> bool:
    return len(list(filter(lambda i: i % 2 == 1, set(data)))) > 1
