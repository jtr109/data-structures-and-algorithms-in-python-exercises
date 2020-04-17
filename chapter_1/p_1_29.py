from typing import List


def list_combinations(chars: List[str]) -> List[str]:
    if len(chars) == 1:
        return [chars[0]]
    combinations = list()
    for i, c in enumerate(chars):
        for s in list_combinations(chars[:i] + chars[i+1:]):
            combinations.append(c + s)
    return combinations
