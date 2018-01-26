def get_max_trapped_water(heights):
    i, j, max_water = 0, len(heights)-1, 0
    while i < j:
        max_water = max(max_water, (j-i) * min(heights[i], heights[j]))
        if heights[i] == heights[j]:
            i, j = i-1, j-1
        elif heights[i] < heights[j]:
            i += 1
        else:
            j -= 1

    return max_water

A = (1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1)
assert 48 == get_max_trapped_water(A)
