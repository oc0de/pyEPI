import functools

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    result = []
    while True:
        result.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(result))


def string_to_int(s):
    return functools.reduce(lambda r, c: r * 10 + ord(c)-ord('0'), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


def main():
    assert("13" == int_to_string(13))
    assert("-45321" == int_to_string(-45321))
    assert(15 == string_to_int("15"))
    assert(-8765 == string_to_int("-8765"))



if __name__ == '__main__':
    main()
