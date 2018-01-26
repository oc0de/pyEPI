def is_roman_number(num):
    MAPPING = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    count = 0
    for i in reversed(range(len(num)-1)):
        if num[i] not in MAPPING.keys(): return False
        if MAPPING[num[i]] < MAPPING[num[i+1]]:
            count += 1
        if count > 1: return False

    return True


def main():
    assert is_roman_number("LIXI") == True
    assert is_roman_number("LIX") == True
    assert is_roman_number("LVIIII") == True
    assert is_roman_number("XXXXXIIIIIIIII") == True
    assert is_roman_number("LIXIC") == False
    assert is_roman_number("IXC") == False
    assert is_roman_number("CDM") == False

if __name__ == '__main__':
    main()
