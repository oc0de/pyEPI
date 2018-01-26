import collections

Event = collections.namedtuple('Event', ('start', 'finish'))
Point = collections.namedtuple('Point', ('time', 'is_start'))

def find_max_simultaneous_events(A):
    E = ([Point(event.start, True) for event in A] +
            [Point(event.finish, False) for event in A])

    E.sort(key=lambda e: (e.time, not e.is_start))
    local_max, res = 0, 0
    for e in E:
        if e.is_start:
            local_max += 1
            res = max(res, local_max)
        else:
            local_max -= 1

    return res

A = [
    Event(1, 5), Event(2, 7), Event(5, 6), Event(6, 7), Event(7, 9),
    Event(9, 17), Event(11, 13), Event(12, 15), Event(14, 15)
]
assert find_max_simultaneous_events(A) == 3

A = [
    Event(1, 5), Event(2, 7), Event(4, 5), Event(6, 10), Event(8, 9),
    Event(9, 17), Event(11, 13), Event(12, 15), Event(14, 15), Event(9, 10)
]
assert find_max_simultaneous_events(A) == 4
