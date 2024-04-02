import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

d = [(0,1), (0, -1), (1,0), (-1,0)]

def dfs(x, y):

    visited[x][y] = True
    color = grid[x][y]

    for dx, dy in d:
        X, Y = x + dx, y + dy
        if (0 <= X < N) and (0 <= Y < N):
            if not visited[X][Y] and grid[X][Y] == color:
                dfs(X,Y)
    return 

cnt, cnt2 = 0, 0

for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            dfs(x,y)
            cnt += 1

for x in range(N):
    for y in range(N):
        if grid[x][y] == 'G':
            grid[x][y] = 'R'

visited = [[False] * N for _ in range(N)]

for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            dfs(x,y)
            cnt2 += 1

print(cnt, cnt2)