from random import choice, sample
from string import ascii_letters


def make_mistake(text: str) -> str:
    i = choice(range(len(text)))
    c = choice(ascii_letters)
    return ''.join(text[:i] + c + text[i+1:])


def repeat():
    text = 'I will never spam my friends again.'
    times = 100
    mistake_times = 8
    mistake_lines = sample(range(times), mistake_times)
    for i in range(times):
        data = make_mistake(text) if i in mistake_lines else text
        yield data


if __name__ == "__main__":
    for l in repeat():
        print(l)
