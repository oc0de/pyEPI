import collections

def can_string_be_a_palindrome(s):
    print collections.Counter(s)
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


s = 'edified'
print can_string_be_a_palindrome(s)
