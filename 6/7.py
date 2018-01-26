def phone_mnemonic(digit):
    MAPPING = [[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],
                   ['T','U','V'],['W','X','Y','Z']]
    def helper(digit):
        if not digit: return ""
        res, words = [], MAPPING[int(digit[0])]
        for w in words:
            p = helper(digit[1:])
            res += [w + wi for wi in p] or w
        return res

    return helper(digit)

print phone_mnemonic("2276696")
