from typing import Dict


def count_words(text: str) -> Dict[str, int]:
    ret = dict()
    for word in text.split(' '):
        ret[word] = ret.get(word, 0) + 1
    return ret
