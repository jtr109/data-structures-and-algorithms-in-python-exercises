from typing import Dict


def count_vowel(text: str) -> Dict[str, int]:
    vowel_letters = ('a', 'e', 'i', 'o', 'u')
    summary = {v: 0 for v in vowel_letters}
    for c in text.lower():
        if c not in vowel_letters:
            continue
        summary[c] += 1
    return summary
