import sys


def reverse_lines(text: str) -> str:
    return '\n'.join(reversed(text.splitlines()))


if __name__ == "__main__":
    text = sys.stdin.read()
    print(reverse_lines(text))
