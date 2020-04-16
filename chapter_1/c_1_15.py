from typing import List


def separate(data: List[int]) -> bool:
    return len(data) == len(set(data))
