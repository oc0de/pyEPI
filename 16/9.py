def maximum_revenue(coins):
    def helper(a, b):
        if a > b: return 0

        if (a, b) not in cache:
            max_revenue_a = coins[a] + min(helper(a+2,b), helper(a+1, b-1))
            max_revenue_b = coins[b] + min(helper(a, b-2), helper(a+1, b-1))
            cache[(a,b)] = max(max_revenue_a, max_revenue_b)

        return cache[(a,b)]

    cache = {}
    return helper(0, len(coins) - 1)

coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10]
assert 140 == maximum_revenue(coins)
