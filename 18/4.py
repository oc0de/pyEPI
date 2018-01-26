class GraphVertex:
    white, gray, black = range(3)

    def __init__(self):
        self.color = GraphVertex.white
        self.edges = []


    def __repr__(self):
        return 'color:%d id:(%d) edges~>%s' % (self.color, id(self),
                    ','.join(str(id(x)) for x in self.edges))


def is_deadlocked(G):
    def has_cycle(cur):
        if cur.color == GraphVertex.gray: return True
        cur.color = GraphVertex.gray

        if any(next_g.color != GraphVertex.black and has_cycle(next_g)
                for next_g in cur.edges): return True

        cur.color = GraphVertex.black
        return False

    return any(vertex.color == GraphVertex.white and has_cycle(vertex)
                for vertex in G)


G = [GraphVertex() for _ in range(2)]
G[0].edges.append(G[1])
G[1].edges.append(G[0])
result = is_deadlocked(G)
print(result)


G = [GraphVertex() for _ in range(3)]
G[0].edges.append(G[1])
G[1].edges.append(G[2])
G[2].edges.append(G[0])
result = is_deadlocked(G)
print(result)


G = [GraphVertex() for _ in range(4)]
G[0].edges.append(G[1])
G[0].edges.append(G[2])
G[0].edges.append(G[3])
result = is_deadlocked(G)
print(result)
