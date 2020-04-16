from random import randrange
from typing import Any, Iterable


def choice(data: Iterable[Any]) -> Any:
    return data[randrange(0, len(data))]
