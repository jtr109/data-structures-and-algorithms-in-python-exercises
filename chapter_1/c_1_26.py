def calculative(a: int, b: int, c: int) -> bool:
    return (
        a + b == c or
        a - b == c or
        a * b == c or
        a / b == c or
        a == b + c or
        a == b - c or
        a == b * c or
        a == b / c
    )
