from typing import Iterable, Tuple


def minmax(data: Iterable[int]) -> Tuple[int]:
    first = data[0]
    minimum = first
    maximum = first
    for d in data[1:]:
        if d < minimum:
            minimum = d
        if d > maximum:
            maximum = d
    return (minimum, maximum)
