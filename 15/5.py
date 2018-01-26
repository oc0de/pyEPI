def find_k_subset(n,k):
    def helper(k, idx):
        if k == 0:
            yield []

        for i in range(idx,n+1):
            for p in helper(k-1, i+1):
                yield [i] + p

    return list(helper(k,1))


assert find_k_subset(3, 1) == [[1],[2],[3]]
