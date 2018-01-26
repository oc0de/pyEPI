def get_ips(s):
    def is_correct_format(p):
        if len(p) > 1 and p[0] == '0': return False
        if int(p) > 255: return False
        return True

    res = []
    for i in range(1, min(4, len(s))):
        first = s[:i]
        if is_correct_format(first):
            for j in range(1, min(4, len(s)-i)):
                second = s[i:i+j]
                if is_correct_format(second):
                    for k in range(1, min(4, len(s)-i-j)):
                        third = s[i+j:i+j+k]
                        fourth = s[i+j+k:]
                        if is_correct_format(third) and is_correct_format(fourth):
                            res += first+'.'+second+'.'+third+'.'+fourth,
    return res

s = "192168110"
print get_ips(s)
