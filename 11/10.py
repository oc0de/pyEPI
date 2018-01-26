import collections
import functools

def find_duplicate_missing(A):
    DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                                ('duplicate', 'missing'))

    miss_XOR_dup = functools.reduce(lambda x,y: x ^ y[0] ^ y[1], enumerate(A), 0)
    differ_bit, miss_or_dup = miss_XOR_dup & ~(miss_XOR_dup - 1), 0
    for idx, value in enumerate(A):
        if idx & differ_bit:
            miss_or_dup ^= idx
        if value & differ_bit:
            miss_or_dup ^= value

    if any(e == miss_or_dup for e in A):
        return DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_XOR_dup)

    return DuplicateAndMissing(miss_or_dup ^ miss_XOR_dup, miss_or_dup)

A = [0, 1, 2, 4, 5, 6, 6]
ans = find_duplicate_missing(A)
assert ans.duplicate == 6 and ans.missing == 3

A = [0, 0, 1]
ans = find_duplicate_missing(A)
assert ans.duplicate == 0 and ans.missing == 2

A = [1, 3, 2, 5, 3, 4]
ans = find_duplicate_missing(A)
assert ans.duplicate == 3 and ans.missing == 0
