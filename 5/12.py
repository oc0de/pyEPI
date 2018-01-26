import random

def random_sampling(k, A):
    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]

A = [3,7,5,11]
random_sampling(3, A)
