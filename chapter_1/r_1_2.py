def is_even(k: int) -> bool:
    # all even bit and with 1 is 0
    return not(k & 1)
