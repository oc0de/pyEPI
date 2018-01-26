import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(paragraph, keywords):
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_subarray_length = [float('inf')] * len(keywords)

    shortest_distance = float('inf')
    result = Subarray(-1,-1)

    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx-1] != float('inf'):
                distance_to_previous_keyword = i - latest_occurrence[keyword_idx-1]
                shortest_subarray_length[keyword_idx] = (distance_to_previous_keyword +
                            shortest_subarray_length[keyword_idx-1])

            latest_occurrence[keyword_idx] = i


            if (keyword_idx == len(keywords)-1 and
                    shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i-shortest_distance+1, i)

    return result

A3 = list('01234567892461010103210')
subseq4 = list('02946')
rr = find_smallest_sequentially_covering_subset(A3, subseq4)
assert (rr.start, rr.end) == (0, 12)
