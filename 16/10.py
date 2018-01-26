def number_of_ways_to_top(top, maximum_step):
    def helper(h):
        if h <= 1: return 1
        if h not in number_of_ways:
            number_of_ways[h] = sum(
                helper(h-i) for i in range(1, min(h, maximum_step) + 1))

        return number_of_ways[h]

    number_of_ways = {}
    return helper(top)


assert 5 == number_of_ways_to_top(4, 2)
assert 1 == number_of_ways_to_top(1, 2)
assert 1 == number_of_ways_to_top(0, 3)
