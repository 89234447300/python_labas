def transpose(mat):
    if mat == []:
        return []

    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError("Рваная матрица")

    result = []
    for j in range(cols):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        result.append(new_row)

    return result


def row_sums(mat):
    if mat == []:
        return []

    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError("Рваная матрица")

    sums = []
    for row in mat:
        total = 0
        for num in row:
            total += num
        sums.append(total)

    return sums


def col_sums(mat):
    if mat == []:
        return []

    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError("Рваная матрица")

    sums = []
    for j in range(cols):
        total = 0
        for i in range(len(mat)):
            total += mat[i][j]
        sums.append(total)

    return sums

print("transpose:")
print(transpose([[1, 2, 3]]))  # [[1], [2], [3]]
print(transpose([[1], [2], [3]]))  # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([]))  # []

print("row_sums:")
print(row_sums([[1, 2, 3], [4, 5, 6]]))  # [6, 15]
print(row_sums([[-1, 1], [10, -10]]))  # [0, 0]
print(row_sums([[0, 0], [0, 0]]))  # [0, 0]

print("col_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))  # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))  # [9, -9]
print(col_sums([[0, 0], [0, 0]]))  # [0, 0]