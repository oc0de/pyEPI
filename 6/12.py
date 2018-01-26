import itertools

def encode_to_RLE(s):
    return ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))

def decode_from_RLE_to_str(s):
    res = ""
    for i in range(0,len(s), 2):
        res += int(s[i]) * s[i+1]
    return res

def main():
    assert encode_to_RLE('aaaabcccaa') == '4a1b3c2a'
    assert decode_from_RLE_to_str('4a1b3c2a') == 'aaaabcccaa'


if __name__ == '__main__':
    main()
