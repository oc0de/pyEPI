def search_entry_equal_to_its_index(A):
    left, right, = 0, len(A)-1
    while left <= right:
        mid = left + (right-left)/2
        if mid == A[mid]:
            return mid
        elif mid < A[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

A = [0, 1, 2, 3]
assert -1 != search_entry_equal_to_its_index(A)
A = [-2,0,2,3,6,7,9]
assert 3 == search_entry_equal_to_its_index(A)
