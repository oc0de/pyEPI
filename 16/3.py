def number_of_ways(n, m):
    cache = {}
    def helper(x,y):
        if x == y == 0: return 1
        if (x,y) not in cache:
            ways_top = 0 if x == 0 else helper(x-1, y)
            ways_left = 0 if y == 0 else helper(x, y-1)
            cache[(x,y)] = ways_top + ways_left
        return cache[(x,y)]

    return helper(n-1, m-1)


print number_of_ways(5, 5)
