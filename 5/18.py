def matrix_in_spiral_order(square_matrix):
    def matrix_layer_in_clockwise(offset):
        if offset == matrix_size - offset:
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset: -1 - offset])
        spiral_ordering.extend(list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset: offset:-1])
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    matrix_size = len(square_matrix) - 1
    spiral_ordering = []
    for offset in range((len(square_matrix)+1) // 2):
        matrix_layer_in_clockwise(offset)

    return spiral_ordering


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert matrix_in_spiral_order(A) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
