import functools

def rabin_karp(t, s):
    if len(s) > len(t): return -1

    BASE = 26
    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE ** max(len(s)-1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i-len(s):i] == s:
            return i - len(s)

        t_hash -= ord(t[i-len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])


    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)

    return -1

assert rabin_karp('GACGCCA', 'CGC') == 2
assert rabin_karp('GATACCCATCGAGTCGGATCGAGT', 'GAG') == 10
assert rabin_karp('FOOBARWIDGET', 'WIDGETS') == -1
assert rabin_karp('A', 'A') == 0
assert rabin_karp('A', 'B') == -1
assert rabin_karp('A', '') == 0
assert rabin_karp('ADSADA', '') == 0
assert rabin_karp('', 'A') == -1
assert rabin_karp('', 'AAA') == -1
assert rabin_karp('A', 'AAA') == -1
assert rabin_karp('AA', 'AAA') == -1
assert rabin_karp('AAA', 'AAA') == 0
assert rabin_karp('BAAAA', 'AAA') == 1
assert rabin_karp('BAAABAAAA', 'AAA') == 1
assert rabin_karp('BAABBAABAAABS', 'AAA') == 8
assert rabin_karp('BAABBAABAAABS', 'AAAA') == -1
assert rabin_karp('FOOBAR', 'BAR') > 0
