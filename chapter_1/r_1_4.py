def sum_of_square(n: int) -> int:
    s = 0
    while n > 0:
        s += n * n
        n -= 1
    return s
