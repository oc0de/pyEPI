import collections

Interval = collections.namedtuple('Interval', ('left', 'right'))

def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    while (i < len(disjoint_intervals) and
            new_interval.left > disjoint_intervals[i].right):
        result += disjoint_intervals[i],
        i += 1

    while (i < len(disjoint_intervals) and
            new_interval.right >= disjoint_intervals[i].left):
        new_interval = Interval(min(new_interval.left, disjoint_intervals[i].left),
                                    max(new_interval.right, disjoint_intervals[i].right))
        i += 1

    return result + [new_interval] + disjoint_intervals[i:]


disjoint_intervals = [Interval(-4,-1), Interval(0,2), Interval(3,6),
                        Interval(7,9), Interval(11,12), Interval(14,17)]

new_interval = Interval(1,8)
res = add_interval(disjoint_intervals, new_interval)
assert res == [Interval(-4,-1), Interval(0,9), Interval(11,12), Interval(14,17)]
