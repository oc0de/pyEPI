def is_well_formed(s):
    left_chars, lookup = [], {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in lookup: left_chars += c,
        elif not left_chars or lookup[left_chars.pop()] != c: return False

    return not left_chars

assert is_well_formed('[()[]]{}')
assert is_well_formed('(()[]{()[]{}{}})')
