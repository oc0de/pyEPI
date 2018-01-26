ARRAY = __import__('1')

def sort_k_increasing_decreasing_array(A):
    sorted_subarrays = []
    INCREASING = True
    start_idx = 0
    for i in range(1, len(A)+1):
        if ((i == len(A)) or (A[i] <= A[i-1] and INCREASING) or
                A[i] > A[i-1] and not INCREASING):
            sorted_subarrays += A[start_idx:i] if INCREASING else A[i-1:start_idx-1:-1],
            start_idx, INCREASING = i, not INCREASING

    return ARRAY.merge_sorted_arrays(sorted_subarrays)

A = [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1]
assert sorted(A) == sort_k_increasing_decreasing_array(A)
