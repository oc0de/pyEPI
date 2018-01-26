class Queue:
    def __init__(self):
        self._enq, self._deq = [], []

    def enqueue(self, x):
        self._enq += x,

    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq += self._enq.pop(),

        if not self._deq:
            raise IndexError('Empty Queue')

        return self._deq.pop()

Q = Queue()
Q.enqueue(1)
Q.enqueue(2)
assert 1 == Q.dequeue()  # 1
assert 2 == Q.dequeue()  # 2
Q.enqueue(3)
assert 3 == Q.dequeue()  # 3
