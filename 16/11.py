def minimum_messiness(words, line_length):
    num_remaining_blanks = line_length - len(words[0])
    min_messiness = ([num_remaining_blanks**2] +
                         [float('inf')] * (len(words)-1))

    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i-1] + num_remaining_blanks**2
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0: break

            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
            current_line_messiness = num_remaining_blanks ** 2
            min_messiness[i] = min(min_messiness[i],
                                    current_line_messiness + first_j_messiness)

    return min_messiness[-1]

assert (minimum_messiness(('aaa', 'bbb', 'c', 'd', 'ee', 'ff', 'gggggg'),
                          11) == 45)
assert minimum_messiness(('a', 'b', 'c', 'd'), 5) == 8
