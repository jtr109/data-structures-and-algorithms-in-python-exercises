import string


def excluding_symbols(text: str) -> str:
    return ''.join(filter(lambda c: c not in string.punctuation, text))
