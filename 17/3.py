import collections

Interval = collections.namedtuple('Interval', ('left', 'right'))
def find_minimum_visits(intervals):
    if not intervals: return []

    intervals.sort(key=lambda x: x.right)
    visits = []
    last_visit_time = float('-inf')
    for interval in intervals:
        if interval.left > last_visit_time:
            last_visit_time = interval.right
            visits.append(last_visit_time)

    return visits



intervals = [
    Interval(1, 4), Interval(2, 8), Interval(3, 6), Interval(3, 5),
    Interval(7, 10), Interval(9, 11)
]
assert find_minimum_visits(intervals) == [4, 10]
intervals = [
    Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(4, 5),
    Interval(5, 6), Interval(6, 7)
]
assert find_minimum_visits(intervals) == [2, 4, 6]
intervals = [Interval(1, 5), Interval(2, 3), Interval(3, 4)]
assert find_minimum_visits(intervals) == [3]

intervals = [Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6,9)]
assert find_minimum_visits(intervals) == [3,9]
