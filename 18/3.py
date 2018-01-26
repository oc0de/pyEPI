import collections

def fill_surrounded_regions(board):
    n, m = len(board), len(board[0])
    q = ([(i,j) for k in range(n) for i,j in ((k, 0), (k, m-1))] +
            [(i,j) for k in range(m) for i,j in ((0, k), (n-1, k))])
    while q:
        x, y = q.pop(0)
        if (0 <= x < n and 0 <= y < m and
                board[x][y] == 'W'):
            board[x][y] = 'T'
            q += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]



A = [['B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'],
     ['B', 'B', 'B', 'B']]

fill_surrounded_regions(A)
golden = [['B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'],
          ['B', 'B', 'B', 'B']]

assert A == golden
