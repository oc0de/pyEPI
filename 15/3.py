def permute(nums):
    def helper(nums):
        if not nums:
            yield []
        for i, n in enumerate(nums):
            for p in helper(nums[:i] + nums[i+1:]):
                yield [n] + p

    return list(helper(nums))

A = [0, 1, 2]
result = permute(A)
golden_result = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1],
                 [2, 1, 0]]
assert result == golden_result
