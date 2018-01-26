def test_collatz_conjecture(n):
    verified_numbers = set()
    for i in range(3, n+1, 2):
        local_sequence = set()
        temp = i
        while temp >= i:
            if temp in local_sequence: return False
            local_sequence.add(temp)
            if temp % 2: #odd number
                if temp in verified_numbers: break
                verified_numbers.add(temp)
                temp = temp * 3 + 1
            else: #even number
                temp //= 2
    return True



print test_collatz_conjecture(10)
