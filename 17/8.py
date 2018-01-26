def calculate_largest_rectangel(heights):
    s, max_area = [], -1
    for i, h in enumerate(heights+[0]):
        while s and h <= heights[s[-1]]:
            height = heights[s.pop()]
            width = i if not s else i - s[-1] - 1
            max_area = max(max_area, width * height)

        s += i,

    return max_area


A = [2, 3, 4, 1, 2]
area = calculate_largest_rectangle(A)
assert 6 == area
A = [2, 2, 2]
assert 6 == calculate_largest_rectangle(A)
A = [1, 1, 2]
assert 3 == calculate_largest_rectangle(A)
