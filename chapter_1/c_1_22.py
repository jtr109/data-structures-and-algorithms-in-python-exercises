from typing import List


def dot_product(a: List[int], b: List[int]) -> List[int]:
    return [i * j for i, j in zip(a, b)]
