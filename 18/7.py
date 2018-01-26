import collections
import string

def transform_string(D, s, t):
    Node = collections.namedtuple(
        'Node', ('label','distance'))
    q = [Node(s, 0)]
    D.remove(s)

    while q:
        f = q.pop(0)
        if f.label == t: return f.distance

        for i in range(len(f.label)):
            for c in string.ascii_lowercase:
                cand = f.label[:i] + c + f.label[i+1:]
                if cand in D:
                    D.remove(cand)
                    q += Node(cand, f.distance + 1),

    return -1

s = set(["bat", "cot", "dog", "dag", "dot", "cat"])
assert transform_string(s, "cat", "dog") == 3
