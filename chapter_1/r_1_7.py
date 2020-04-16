def sum_of_odd_square(n: int) -> int:
    return sum(map(lambda x: x * x, range(1, n + 1, 2)))
