import collections

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))
def find_min_max(A):
    def min_max_helper(a,b):
        return MinMax(a, b) if a < b else MinMax(b, a)

    if len(A) <= 1:
        return MinMax(A[0], A[0])

    global_min_max = min_max_helper(A[0], A[1])
    for i in range(2, len(A)-1, 2):
        local_min_max = min_max_helper(A[i], A[i+1])
        global_min_max = min_max_helper(min(local_min_max.smallest, global_min_max.smallest),
                                        max(local_min_max.largest, global_min_max.largest))

    if len(A) % 2:
        global_min_max = min_max_helper(min(global_min_max.smallest, A[-1]),
                                        max(global_min_max.largest, A[-1]))

    return global_min_max

A = [-1, 3, -4, 6, 4, 10, 4, 4, 9]
res = find_min_max(A)
assert res == MinMax(-4, 10)
