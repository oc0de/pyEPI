
def find_kth_largest(k, arr):
    def partition_around_pivot(left, right):
        pivot_value = arr[right]
        new_pivot_idx = left
        for i in range(left, right):
            if arr[i] > pivot_value:
                arr[i], arr[new_pivot_idx] = arr[new_pivot_idx], arr[i]
                new_pivot_idx += 1

        arr[right], arr[new_pivot_idx] = arr[new_pivot_idx], arr[right]

        return new_pivot_idx

    left, right = 0, len(arr) - 1
    while left <= right:
        pivot_idx = partition_around_pivot(left, right)
        if pivot_idx == k - 1:
            return arr[pivot_idx]
        elif pivot_idx > k - 1:
            right = pivot_idx - 1
        else:
            left = pivot_idx + 1



A = [3, 1, -2, 10, -4, 16, 5]
assert 16 == find_kth_largest(1, A)
assert 10 == find_kth_largest(2, A)
assert 5  == find_kth_largest(3, A)
assert -2 == find_kth_largest(6, A)
assert -4 == find_kth_largest(7, A)

A = [3, 1, 2, 0, 4, 6, 5]
assert 6 == find_kth_largest(1, A)
assert 5 == find_kth_largest(2, A)
assert 4 == find_kth_largest(3, A)
assert 3 == find_kth_largest(4, A)
assert 2 == find_kth_largest(5, A)
assert 1 == find_kth_largest(6, A)
assert 0 == find_kth_largest(7, A)
