from typing import Any, List


def get(data: List[Any], index: int) -> Any:
    try:
        return data[index]
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
