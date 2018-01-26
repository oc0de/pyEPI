def palindrome_partitioning(S):
    def helper(offset, partial_partition):
        if offset == len(S):
            result.append(list(partial_partition))

        for i in range(offset+1, len(S)+1):
            prefix = S[offset:i]
            if prefix == prefix[::-1]:
                helper(i,partial_partition+[prefix])

    result = []
    helper(0, [])
    return result

result = palindrome_partitioning('abbbac')
v0 = ['a', 'b', 'b', 'b', 'a', 'c']
v1 = ['a', 'b', 'bb', 'a', 'c']
v2 = ['a', 'bb', 'b', 'a', 'c']
v3 = ['a', 'bbb', 'a', 'c']
v4 = ['abbba', 'c']
golden = [v0, v1, v2, v3, v4]
assert result == golden
