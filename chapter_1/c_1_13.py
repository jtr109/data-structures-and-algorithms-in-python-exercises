from typing import List, Any


def my_reverse(data: List[Any]):
    length = len(data)
    for i in range(length // 2):
        j = - i - 1
        data[i], data[j] = data[j], data[i]
