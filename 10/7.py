import heapq

class Stack:
    def __init__(self):
        self._timestamp = 0
        self._max_heap = []

    def push(self, x):
        heapq.heappush(self._max_heap, (-self._timestamp, x))
        self._timestamp += 1

    def pop(self):
        if not self._max_heap:
            raise IndexError('empty stack')

        return heapq.heappop(self._max_heap)[1]

    def peek(self):
        return self._max_heap[0][1]

s = Stack()
s.push(1)
s.push(2)
s.push(3)
assert s.peek() == 3
s.pop()
assert s.peek() == 2
s.pop()
s.push(4)
assert s.peek() == 4
