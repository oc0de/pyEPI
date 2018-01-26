def search_first_of_k(A, k):
    left, right, result = 0, len(A)-1, -1

    while left <= right:
        mid = left + (right-left)/2

        if A[mid] == k:
            result = mid
            right = mid - 1

        elif A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return result

A = [0, 1, 2, 3, 4, 5, 6, 7]
assert 0 == search_first_of_k(A, 0)
assert 1 == search_first_of_k(A, 1)
assert 4 == search_first_of_k(A, 4)
assert 6 == search_first_of_k(A, 6)
assert 7 == search_first_of_k(A, 7)
