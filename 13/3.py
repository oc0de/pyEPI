class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
        return (self.first_name < other.first_name if self.first_name != other.first_name else
                    self.last_name < other.last_name)


def eliminate_duplicate(A):
    A.sort()
    write_idx = 1
    for cand in A[1:]:
        if cand.first_name != A[write_idx-1].first_name:
            A[write_idx] = cand
            write_idx += 1

    del A[write_idx:]


A = [Name('Foo', 'Bar'), Name('ABC', 'XYZ'), Name('Foo', 'Widget')]
eliminate_duplicate(A)
assert len(A) == 2
