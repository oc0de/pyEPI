def apply_permutation(perm, A):
    for i in range(len(A)):
        next_idx = i
        while perm[next_idx] >= 0:
            tmp = perm[next_idx]
            A[tmp], A[i] = A[i], A[tmp]
            perm[next_idx] -= len(perm)
            next_idx = tmp

    perm[:] = [a + len(perm) for a in perm]


A = ['a','b','c','d']
P = [2,0,1,3]
apply_permutation(P,A)
assert A == ['b','c','a','d']
