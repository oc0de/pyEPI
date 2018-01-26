def add_two_bit_strings(a,b):
    len_a = len(a)
    len_b = len(b)
    maxLen = max(len_a, len_b)

    if len_a < len_b:
        a = list((len_b - len_a) * "0") + a
    elif len_b < len_a:
        b = list((len_a - len_b) * "0") + b

    c = 0
    result = []
    for i in reversed(range(maxLen)):
        aa, bb= int(a[i]), int(b[i])
        s = aa ^ bb ^ c
        c = (aa and bb) or (aa and c) or (bb and c)
        result.insert(0,str(s))

    result.insert(0,"1") if c else _
    return result


def main():
    a = ["1","0","1","1"]
    b = ["1","0","1"]
    result = add_two_bit_strings(a, b)

    assert result == ['1','0','0','0','0']


if __name__ == '__main__':
    main()
