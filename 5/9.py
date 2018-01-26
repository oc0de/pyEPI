def generate_primes(n):
    primes = []
    is_prime = set()
    for p in range(2, n):
        if p not in is_prime:
            primes.append(p)
            for i in range(p, n+1, p):
                is_prime.add(i)

    return primes


n = 30
print generate_primes(n)
