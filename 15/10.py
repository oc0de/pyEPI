def gray_code(num_bits):
    if num_bits == 0: return [0]
    return [(x >> 1) ^ x for x in range(2 ** num_bits)]

print gray_code(10)
assert gray_code(3) == [0, 1, 3, 2, 6, 7, 5, 4]
