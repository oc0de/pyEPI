stack = __import__('1')

class QueueWithMax:
    def __init__(self):
        self._enqueue = stack.Stack()
        self._dequeue = stack.Stack()

    def enqueue(self, x):
        self._enqueue.push(x)

    def dequeue(self):
        if self._dequeue.empty():
            while not self._enqueue:
                self._dequeue.push(self._enqueue.pop())
        if not self._dequeue.empty():
            return self._dequeue.pop()
        raise IndexError('Empty queue')

    def max(self):
        if not self._enqueue.empty():
            return self._enqueue.max() if self._dequeue.empty() else max(self._enqueue.max(), self._dequeue.max())
        if not self._dequeue.empty():
            return self._dequeue.max()

        raise IndexError('empty queue')




q = QueueWithMax()
