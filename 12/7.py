import collections

def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = (-1,-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == (-1,-1) or right-left < result[1]-result[0]:
                result = (left, right)

            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1

            left += 1

    return result


A = ['a', 'b', 'c', 'b', 'a', 'd', 'c', 'a', 'e', 'a', 'a', 'b', 'e']
d = ['b', 'c', 'e']
res = find_smallest_subarray_covering_set(A, set(d))
assert res == (3,8)
d = ['a', 'c']
res = find_smallest_subarray_covering_set(A, set(d))
assert res == (6,7)
A = ['a', 'b']
d = ['a', 'b']
res = find_smallest_subarray_covering_set(A, set(d))
assert res == (0,1)
A = ['a', 'b']
d = ['b', 'a']
res = find_smallest_subarray_covering_set(A, set(d))
assert res == (0,1)
