import math
import itertools

def solve_sudoku(partial_assignment):
    def solve_partial_sudoku(i,j):
        if i == len(partial_assignment):
            i = 0
            j += 1
            if j == len(partial_assignment[i]):
                return True

        if partial_assignment[i][j] != EMPTY_ENTRY:
            return solve_partial_sudoku(i+1, j)

        def valid_to_add(i, j, val):
            if any(val == partial_assignment[k][j]
                            for k in range(len(partial_assignment))):
                return False

            if val in partial_assignment[i]:
                return False

            region_size = int(math.sqrt(len(partial_assignment)))
            I, J = i // region_size, j // region_size
            return not any(
                val == partial_assignment[region_size * I + a][region_size * J + b]
                    for a, b in itertools.product(range(region_size), repeat=2))

        for val in range(1, len(partial_assignment[0]) + 1):
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True

        partial_assignment[i][j] = EMPTY_ENTRY
        return False

    EMPTY_ENTRY = 0
    return solve_partial_sudoku(0,0)


def main():
    A = [[0, 2, 6, 0, 0, 0, 8, 1, 0], [3, 0, 0, 7, 0, 8, 0, 0, 6],
         [4, 0, 0, 0, 5, 0, 0, 0, 7], [0, 5, 0, 1, 0, 7, 0, 9, 0],
         [0, 0, 3, 9, 0, 5, 1, 0, 0], [0, 4, 0, 3, 0, 2, 0, 5, 0],
         [1, 0, 0, 0, 3, 0, 0, 0, 2], [5, 0, 0, 2, 0, 4, 0, 0, 9],
         [0, 3, 8, 0, 0, 0, 4, 6, 0]]
    solve_sudoku(A)
    golden_A = [[7, 2, 6, 4, 9, 3, 8, 1, 5], [3, 1, 5, 7, 2, 8, 9, 4, 6],
                [4, 8, 9, 6, 5, 1, 2, 3, 7], [8, 5, 2, 1, 4, 7, 6, 9, 3],
                [6, 7, 3, 9, 8, 5, 1, 2, 4], [9, 4, 1, 3, 6, 2, 7, 5, 8],
                [1, 9, 4, 8, 3, 6, 5, 7, 2], [5, 6, 7, 2, 1, 4, 3, 8, 9],
                [2, 3, 8, 5, 7, 9, 4, 6, 1]]
    assert A == golden_A


if __name__ == '__main__':
    main()
