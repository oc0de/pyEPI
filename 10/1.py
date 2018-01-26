import heapq
import itertools

def merge_sorted_arrays(sorted_arrays):
    sorted_arrays_iters = [ iter(x) for x in sorted_arrays]
    min_heap, result = [], []

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    while min_heap:
        smallest_entry, smallest_array_idx = heapq.heappop(min_heap)
        result += smallest_entry,
        next_element = next(sorted_arrays_iters[smallest_array_idx], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_idx))

    return result

def main():
    sorted_arrays = [[3,5,7], [0,6], [0,6,28]]
    print merge_sorted_arrays(sorted_arrays)



if __name__ == '__main__':
    main()
