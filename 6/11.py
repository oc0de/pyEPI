def get_snake_string(s):
    return s[1::4] + s[::2] + s[3::4]


def main():
    s = "Hello World!"
    assert get_snake_string(s) == "e lHloWrdlo!"

if __name__ == '__main__':
    main()
