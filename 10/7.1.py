import heapq

class Queue:
    def __init__(self):
        self._timestamp = 0
        self._min_heap = []

    def enqueue(self, x):
        heapq.heappush(self._min_heap, (self._timestamp, x))
        self._timestamp += 1

    def dequeue(self):
        if not self._min_heap:
            raise IndexError('empty queue')
        return heapq.heappop(self._min_heap)[1]

    def head(self):
        return self._min_heap[0][1]

q = Queue()
q.enqueue(1)
q.enqueue(2)
assert q.head() == 1
q.dequeue()
assert q.head() == 2
q.dequeue()
