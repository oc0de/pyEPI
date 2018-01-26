def smallest_nonconstructible_value(A):
    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1: break
        max_constructible_value += a

    return max_constructible_value + 1


A = [1, 1, 1, 1, 1, 5, 10, 25]
print smallest_nonconstructible_value(A)
