class GraphVertex:
    def __init__(self):
        self.status = -1
        self.edges = []

    def __repr__(self):
        return 'Status~>%d:%d:%s' % (self.status, id(self),
                    ','.join(str(x.id) for x in self.edges))


def is_any_placement_feasible(G):
    def bfs(s):
        s.status = 0
        q = [s]
        while q:
            curr = q.pop(0)
            for e in curr.edges:
                if e.status == -1:
                    e.status = curr.status + 1
                    q += e,
                elif e.status == curr.status:
                    return False

        return True

    return all(bfs(v) for v in G if v.status == -1)


G = [GraphVertex() for _ in range(4)]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[0])
G[2].edges.append(G[3])

assert is_any_placement_feasible(G) == True
