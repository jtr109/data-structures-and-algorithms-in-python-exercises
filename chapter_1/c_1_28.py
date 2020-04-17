from typing import List


def norm(v: List[int], p: int) -> float:
    return pow(sum(map(lambda i: pow(i, p), v)), 1 / p)
