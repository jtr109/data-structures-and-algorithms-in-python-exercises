from random import randint
from typing import Any, List


def shuffle(data: List[Any]):
    for i in range(len(data)):
        j = randint(i, len(data) - 1)
        data[i], data[j] = data[j], data[i]
