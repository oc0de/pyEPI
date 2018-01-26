def n_queens(n):
    def helper(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row - i)
                for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                helper(row+1)
    result, col_placement = [], [0] * n
    helper(0)
    return result


result = n_queens(2)
assert 0 == len(result)

result = n_queens(3)
assert 0 == len(result)

result = n_queens(4)
assert 2 == len(result)

place1 = [1, 3, 0, 2]
place2 = [2, 0, 3, 1]
assert result[0] == place1 or result[0] == place2
assert result[1] == place1 or result[1] == place2
assert result[0] != result[1]
