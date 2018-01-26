def compute_binomial_coefficient(n, k):
    cache = {}
    def helper(x, y):
        if y in (0, x): return 1

        if (x, y) not in cache:
            cache[(x, y)] = helper(x-1, y) + helper(x-1, y-1)

        return cache[(x,y)]


    return helper(n, k)

assert compute_binomial_coefficient(5,2) == 10
