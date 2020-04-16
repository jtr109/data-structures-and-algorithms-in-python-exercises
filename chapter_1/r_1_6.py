def sum_of_odd_square(n: int) -> int:
    s = 0
    while n > 0:
        if n % 2 != 0:
            s += n * n
        n -= 1
    return s
