def minimum_path_weight(triangle):
    if not triangle: return 0
    prev_row = triangle[0]
    for i in range(1, len(triangle)):
        curr_row = triangle[i]
        curr_row[0] += prev_row[0]
        for j in range(1, len(triangle[i])-1):
            curr_row[j] += min(prev_row[j-1], prev_row[j])

        curr_row[-1] += prev_row[-1]
        prev_row = curr_row

    return min(prev_row)

A = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
assert 11 == minimum_path_weight(A)
