def matrix_search(mat, k):
    row, col = 0, len(mat[0]) - 1

    while row < len(mat) and col >= 0:
        if mat[row][col] == k:
            return True
        elif mat[row][col] < k:
            row += 1
        else:
            col -= 1

    return False

A = [[1, 5], [2, 6]]
assert not matrix_search(A, 0)
assert matrix_search(A, 1)
assert matrix_search(A, 2)
assert matrix_search(A, 5)
assert matrix_search(A, 6)
assert not matrix_search(A, 3)
