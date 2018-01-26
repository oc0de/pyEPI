def longest_subarray_with_distinct_entries(A):
    most_recent_occurrence = {}
    start_idx, result = 0, 0
    for i, a in enumerate(A):
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            if dup_idx >= start_idx:
                result = max(result, i - start_idx)
                start_idx = dup_idx + 1
        most_recent_occurrence[a] = i

    return max(result, len(A) - start_idx)

assert 1 == longest_subarray_with_distinct_entries([1, 1, 1])
assert 2 == longest_subarray_with_distinct_entries([1, 2, 1])
assert 3 == longest_subarray_with_distinct_entries([1, 2, 1, 3, 1, 2, 1])
assert 2 == longest_subarray_with_distinct_entries([1, 2, 2, 3, 3, 1, 1, 2, 1])
