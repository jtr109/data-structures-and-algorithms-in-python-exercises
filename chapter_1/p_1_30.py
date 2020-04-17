def flat_division(dividend: int, divisor: int = 2) -> int:
    counter = 0
    while dividend >= divisor:
        dividend /= divisor
        counter += 1
    return counter
