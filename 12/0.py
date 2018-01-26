import collections

def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for word in dictionary:
        sorted_string_to_anagrams[''.join(sorted(word))] += word,

    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]


D = [
    'debit card', 'bad credit', 'the morse code', 'here come dots',
    'the eyes', 'they see', 'THL'
]
result = find_anagrams(D)
assert len(result) == 3
