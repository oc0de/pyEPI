import itertools

def look_and_say(num, digit):
    res = []
    for i in range(num):
        j = 0
        while j < len(digit):
            d, count = digit[j], 0
            while j < len(digit) and digit[j] == d:
                j += 1
                count += 1
            res += str(count) + d

        digit = ''.join(res)
        res = []

    return digit

def look_and_say_version2(num, digit):
    for _ in range(num-1):
        digit = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(digit))
    return digit

def main():
    assert look_and_say(1, "1211") == "111221"
    assert look_and_say_version2(2, "1") == "11"

if __name__ == '__main__':
    main()
    # If you want to return the nth from the given digit the loop should be n-1
