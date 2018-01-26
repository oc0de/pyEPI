def levenshtein_distance(A, B):
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            return B_idx + 1
        if B_idx < 0:
            return A_idx + 1

        if (A_idx, B_idx) not in distance_between_prefixes:
            if A[A_idx] == B[B_idx]:
                distance_between_prefixes[(A_idx, B_idx)] = (
                    compute_distance_between_prefixes(A_idx-1, B_idx-1))
            else:
                substitute_last = compute_distance_between_prefixes(A_idx-1, B_idx-1)
                add_last = compute_distance_between_prefixes(A_idx-1, B_idx)
                delete_last = compute_distance_between_prefixes(A_idx, B_idx-1)
                distance_between_prefixes[(A_idx, B_idx)] = (
                    1 + min(substitute_last, add_last, delete_last))

        return distance_between_prefixes[(A_idx, B_idx)]

    distance_between_prefixes = {}
    return compute_distance_between_prefixes(len(A)-1, len(B)-1)


A, B = 'k', 'sitt'
assert 4 == levenshtein_distance(A, B)
A, B = 'Saturday', 'Sunday'
assert 3 == levenshtein_distance(A, B)
A, B = 'kitten', 'sitting'
assert 3 == levenshtein_distance(A, B)
