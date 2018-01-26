import functools

def convert_from_roman_decimal(roman):
    MAPPING = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = MAPPING[roman[-1]]
    for i in reversed(range(len(roman)-1)):
        if MAPPING[roman[i]] < MAPPING[roman[i+1]]:
            result -= MAPPING[roman[i]]
        else:
            result += MAPPING[roman[i]]

    return result

def roman_to_integer(s):
    MAPPING = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    return functools.reduce(lambda res, i: res + (-MAPPING[s[i]] if MAPPING[s[i]] < MAPPING[s[i+1]] else MAPPING[s[i]]),
                                reversed(range(len(s)-1)), MAPPING[s[-1]])

def main():
    assert convert_from_roman_decimal("LIX") == 59
    assert convert_from_roman_decimal("LVIIII") == 59
    assert convert_from_roman_decimal("XXXXXIIIIIIIII") == 59

    assert roman_to_integer("LIX") == 59
    assert roman_to_integer("LVIIII") == 59
    assert roman_to_integer("XXXXXIIIIIIIII") == 59

if __name__ == '__main__':
    main()
