import functools
import string

def decode_col_id(col):
    return functools.reduce(lambda x, y: x * 26 + string.letters.index(y.lower())+1, col, 0) - 1 #6.3.1

def main():
    col = 'AA'
    res = decode_col_id(col)
    print res
    # assert res == 27

    col = 'ZZ'
    res = decode_col_id(col)
    print res
    # assert res == 702

    col = 'XFD'
    res = decode_col_id(col)
    print res

if __name__ == '__main__':
    main()
