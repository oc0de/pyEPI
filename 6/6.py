def reverse_words(s):
    return ' '.join(s.split()[::-1])


s = "ehsan is good"
print reverse_words(s)
