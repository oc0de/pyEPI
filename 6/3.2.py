def id2num(num):
    return ('' if num == 0 else id2num((num-1) // 26) + chr((num-1) % 26 + ord('A')))

print id2num(702)
