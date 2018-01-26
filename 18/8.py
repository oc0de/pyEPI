class GraphVertex:
    def __init__(self):
        self.d = 0
        self.edges = []

    def __repr__(self):
        return ('*' if self.d else '') + '(%d)%d(%s)' % (
            self.d, id(self), ','.join(
                str(id(x)) for x in self.edges))

def find_largest_number_teams(G):
    def build_topological_ordering():
        def dfs(cur):
            cur.d = 1
            for e in cur.edges:
                if not e.d:
                    dfs(e)

            path.append(cur)

        path = []
        for g in G:
            if not g.d:
                dfs(g)
        return path

    def find_longest_path(path):
        max_distance = 0
        while path:
            cur = path.pop()
            max_distance = max(max_distance, cur.d)
            for e in cur.edges:
                e.d = max(e.d, cur.d+1)

        return max_distance

    return(find_longest_path(build_topological_ordering()))


G = [GraphVertex() for _ in range(3)]
G[0].edges.append(G[2])
G[1].edges.append(G[2])
assert 2 == find_largest_number_teams(G)
