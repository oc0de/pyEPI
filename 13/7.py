import collections

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

class Interval:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __lt__(self, other):
        if self.start.val != other.start.val:
            return self.start.val < other.start.val
        return self.start.is_closed and not other.start.is_closed


def union_of_intervals(intervals):
    if not intervals: return
    intervals.sort()
    result = [intervals[0]]

    for i in intervals:
        if intervals and (i.start.val < result[-1].finish.val or
                            (i.start.val == result[-1].finish.val and
                                (i.start.is_closed or result[-1].finish.is_closed))):
            if (i.finish.val > result[-1].finish.val or
                    (i.finish.val == result[-1].finish.val and i.finish.is_closed)):
                    result[-1].finish = i.finish
        else:
            result += i,

    return result
