def find_longest_contained_range(A):
    if not A: return 0

    unprocessed_entries = set(A)
    max_interval_size = 0

    while unprocessed_entries:
        current = unprocessed_entries.pop()
        lower_bound, upper_bound = current - 1, current + 1

        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)

    return max_interval_size

A = [10, 5, 3, 11, 6, 100, 4]
assert 4 == find_longest_contained_range(A)
