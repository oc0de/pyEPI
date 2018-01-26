
def find_nearest_repetition(paragraph):
    word_latest_index, nearest_repeated_distance = {}, float('inf')
    for i, v in enumerate(paragraph):
        if v in word_latest_index:
            latest_idx = word_latest_index[v]
            nearest_repeated_distance = min(nearest_repeated_distance, i - latest_idx)

        word_latest_index[v] = i

    return nearest_repeated_distance

A = ['foo', 'bar', 'widget', 'foo', 'widget', 'widget', 'adnan']
assert 1 == find_nearest_repetition(A)

A = ['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results']
assert 2 == find_nearest_repetition(A)
