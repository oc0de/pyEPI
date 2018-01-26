import string
import functools

def convert_base(num, b1, b2):
    def construct_from_base(num, b):
        return ('' if num == 0 else
                construct_from_base(num // b, b) +
                string.hexdigits[num % b].upper())

    is_negative = num[0] == '-'
    num = functools.reduce(lambda x,y: x * b1 + string.hexdigits.index(y.lower()),
                           num[is_negative:], 0)

    return ('-' if is_negative else '' + '0' if num == 0 else construct_from_base(num, b2))


def main():
    num = '615'
    b1 = 7
    b2 = 13
    res = convert_base(num, b1, b2)
    assert res == '1A7'



if __name__ == '__main__':
    main()
