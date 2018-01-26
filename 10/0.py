import itertools
import heapq

def top_k(k, stream):
    min_heap = [(len(s), s) for s in stream[:k]]
    heapq.heapify(min_heap)
    for next_string in stream[k:]:
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return min_heap

stream = ['a','bddd','cd','ada','bb','ccc','d','dddd']
k = 4
print top_k(k, stream)
