import collections

# 1 -> Black 0 -> White
Coordinate = collections.namedtuple('Coordinate', ('x','y'))
def search_maze(maze, s, e):
    def helper(cur):
        if (not 0 <= cur.x < len(maze) or
                not 0 <= cur.y < len(maze[0]) or
                    maze[cur.x][cur.y]): return False
        path.append(cur)
        maze[cur.x][cur.y] = 1
        if cur == e: return True

        if any(map(helper, (Coordinate(cur.x-1, cur.y), Coordinate(cur.x+1, cur.y),
                Coordinate(cur.x, cur.y-1), Coordinate(cur.x, cur.y+1)))):
            return True

        del path[-1]
        return False

    path = []
    return [] if not helper(s) else path

maze = [[0] * 3 for _ in range(4)]
maze[1][0], maze[0][1], maze[3][1], maze[2][2] = 1, 1, 1, 1
print search_maze(maze, Coordinate(3,0), Coordinate(0,2))
