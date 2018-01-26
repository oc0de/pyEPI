def phone_mnemonic(digit):
    # MAPPING = [['0'],['1'],['ABC'],['DEF'],['GHI'],['JKL'],['MNO'],['PQRS'],['TUV'],['WXYZ']]
    MAPPING = [['0'],['1'], ['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'],
                ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]
    res, partial_res = [],[]
    for d in digit:
        s = MAPPING[int(d)]
        partial_res += [r + w for w in s for r in res] or s
        res = partial_res
        partial_res = []

    return res


print phone_mnemonic("79")
