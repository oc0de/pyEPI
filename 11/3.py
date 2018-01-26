def search_smallest(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = left + (right-left)/2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid

    return left

A = [3, 1, 2]
assert 1 == search_smallest(A)
A = [0, 2, 4, 8]
assert 0 == search_smallest(A)
