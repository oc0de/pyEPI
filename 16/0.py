def find_maximum_subarray(A):
    current_sum, max_sum = A[0], A[0]
    for num in A[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


A = [-2,1,-3,4,-1,2,1,-5,4]
assert find_maximum_subarray(A) == 6
