import collections

Item = collections.namedtuple('Item', ('weight','value'))

def optimum_subjec_to_capacity(items, capacity):
    def helper(idx, curr_cap):
        if idx < 0: return 0

        if (idx, curr_cap) not in cache:
            without_curr_item = helper(idx-1, curr_cap)
            with_curr_item = (0 if items[idx].weight > curr_cap
                                else helper(idx-1, curr_cap - items[idx].weight) + items[idx].value)

            cache[(idx, curr_cap)] = max(without_curr_item, with_curr_item)

        return cache[(idx, curr_cap)]

    cache = {}
    return helper(len(items)-1, capacity)

items = [
    Item(w, v)
    for w, v in ((20, 65), (8, 35), (60, 245), (55, 195), (40, 65), (
        70, 150), (85, 275), (25, 155), (30, 120), (65, 320), (75, 75), (
            10, 40), (95, 200), (50, 100), (40, 220), (10, 99))
]
assert 695 == optimum_subjec_to_capacity(items, 130)

items = (Item(5, 60), Item(3, 50), Item(4, 70), Item(2, 30))
assert 80 == optimum_subjec_to_capacity(items, 5)
