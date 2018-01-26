def next_permutation(perm):
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and
            perm[inversion_point] >= perm[inversion_point+1]):
        inversion_point -= 1

    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point+1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break

    perm[inversion_point+1:] = reversed(perm[inversion_point+1:])
    return perm


perm = [1,0,3,2]
assert next_permutation(perm) == [1,2,0,3]
