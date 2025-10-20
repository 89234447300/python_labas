def min_max(mms: list) -> tuple:

    if not mms:
        raise ValueError

    return (min(mms), max(mms))


test_cases = [
    [3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [],
    [1.5, 2, 2.0, -3.1]
]

for i, test_data in enumerate(test_cases, 1):
    try:
        result = min_max(test_data)
        print(f"{i}: {test_data} -> {result}")
    except ValueError as e:
        print(f"{i}: {test_data} -> {e}")


