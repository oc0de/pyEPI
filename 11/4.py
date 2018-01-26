def square_root(k):
    left, right = 0, k
    while left <= right:
        mid = left + (right-left)/2
        mid_squared = mid ** 2
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1

assert square_root(121) == 11
assert square_root(64) == 8
assert square_root(300) == 17
