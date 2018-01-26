import collections

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def flip_color_dfs(x, y, A):
    color = A[x][y]
    A[x][y] ^= 1
    for d in (0,1),(0,-1),(1,0),(-1,0):
        next_x, next_y = x + d[0], y + d[1]
        if (0 <= next_x < len(A) and
                0 <= next_y < len(A[0]) and
                    A[next_x][next_y] == color):
            flip_color_dfs(next_x, next_y, A)


def flip_color_bfs(x, y, A):
    q = [Coordinate(x,y)]
    color = A[x][y]
    A[x][y] ^= 1
    while q:
        curr = q.pop(0)
        for d in (0,1),(0,-1),(1,0),(-1,0):
            next_x, next_y = x + d[0], y + d[1]
            if (0 <= next_x < len(A) and
                    0 <= next_y < len(A[0]) and
                        A[next_x][next_y] == color):
                A[next_x][next_y] ^= 1
                q += Coordinate(next_x, next_y)


#Test

maze = [[1] * 4 for i in range(4)]
maze[0][0], maze[0][1], maze[0][2] = 0,0,0
maze[2][1], maze[3][1], maze[2][2] = 0,0,0
for i in maze:
    print i
print
flip_color_dfs(2,1,maze)
for i in maze:
    print i
