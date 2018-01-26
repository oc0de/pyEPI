def longest_nondecreasing_subsequence_length(A):
    max_length = [1] * len(A)
    for i in range(1, len(A)):
        max_length[i] = max(1 + max(max_length[j] for j in range(i)
                                    if A[i] >= A[j]), max_length[i])

    return max(max_length)
# @exclude

A = [1,2,3,4,5,6,6]
longest_nondecreasing_subsequence_length(A)
