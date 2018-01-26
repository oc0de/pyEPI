import heapq

def k_largest_in_binary_heap(A, k):
    if k <= 0: return []

    max_heap, result = [], []
    max_heap += (-A[0], 0),

    for _ in range(k):
        idx = max_heap[0][1]
        result += -(heapq.heappop(max_heap)[0]),

        left_child_idx = 2 * idx + 1
        if left_child_idx < len(A):
            heapq.heappush(max_heap, (-A[left_child_idx], left_child_idx))

        right_child_idx = 2 * idx + 2
        if right_child_idx < len(A):
            heapq.heappush(max_heap, (-A[right_child_idx], right_child_idx))

    return result

max_heap = [10, 2, 9, 2, 2, 8, 8, 2, 2, 2, 2, 7, 7, 7, 7]
result = k_largest_in_binary_heap(max_heap, 3)
expected_result = [10, 9, 8]
assert result == expected_result
