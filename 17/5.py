def majority_search(input_stream):
    candidate, candidate_count = None, 0
    for it in input_stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1

    return candidate

# input_stream = ['b','a','c','a','a','b','a','a','c','a']
input_stream = ['b','a','b','b','c','c', 'b']
print majority_search(input_stream)
