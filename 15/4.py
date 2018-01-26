def generate_power_set(S):
    power_set, n = [], len(S)

    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i >> j & 1:
                subset += S[j],

        power_set += subset,

    return power_set


assert generate_power_set(
    [0, 1, 2]) == [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]
