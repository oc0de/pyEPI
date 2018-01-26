def has_three_sum(A, t):
    def has_two_sum(A, d):
        left, right = 0, len(A)-1
        while left <= right:
            if A[left] + A[right] == d:
                return True
            elif A[left] + A[right] < d:
                left += 1
            else:
                right -= 1

        return False
    A.sort()
    return any(has_two_sum(A, t-a) for a in A)

A = [11, 2, 5, 7, 3]
assert has_three_sum(A, 21) == True
assert has_three_sum(A, 22) == False
