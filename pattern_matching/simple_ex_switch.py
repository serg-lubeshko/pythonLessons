def calculate(a: int, b: int, operation: str) -> int | str:
    """
    _ wildcard
    """
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "/":
            return a // b
        case "*":
            return a * b
        case _:
            return f"Operation not available {operation}"


if __name__ == '__main__':
    print(calculate(5, 3, "+"))
    print(calculate(5, 5, "*"))
    print(calculate(5, 1, "/"))
