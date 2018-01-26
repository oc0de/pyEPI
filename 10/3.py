import heapq

def sort_almost_sorted_array(seq, k):
    min_heap, result, idx = seq[:k], [], k
    heapq.heapify(min_heap)

    while min_heap:
        if idx < len(seq):
            heapq.heappush(min_heap, seq[idx])
            idx += 1
        result += heapq.heappop(min_heap),

    return result

A = [2, 1, 5, 4, 3, 9, 8, 7, 6]
assert sort_almost_sorted_array(A, 3) == sorted(A)
