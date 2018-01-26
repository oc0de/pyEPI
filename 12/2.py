import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_frequency_for_letter = collections.Counter(letter_text)

    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True

    return not char_frequency_for_letter

assert not is_letter_constructible_from_magazine('123', '12222222')
assert is_letter_constructible_from_magazine('123', '1123')
assert is_letter_constructible_from_magazine('GATTACA','A AD FS GA T ACA TTT')
