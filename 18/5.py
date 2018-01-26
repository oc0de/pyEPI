class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []


    def __repr__(self):
        return ('label~> %d edges~> %s' %
                    (self.label, ','.join(str(x.label) for x in self.edges)))



def clone_graph(G):
    if not G: return None

    vertex_map = {G: GraphVertex(G.label)}
    q = [G]
    while q:
        v = q.pop(0)
        for e in v.edges:
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)

            vertex_map[v].edges.append(vertex_map[e])

    return vertex_map[G]

def print_result(g):
    q = [g]
    seen = set()
    while q:
        v = q.pop(0)
        seen.add(v)
        print v
        for e in v.edges:
            if e not in seen:
                q += e,


G = [GraphVertex(i) for i in range(3)]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[0])
result = clone_graph(G[0])
print_result(result)
