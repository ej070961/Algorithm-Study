from collections import deque
import copy

n, m = map(int, input().split())
global graph
graph = []
for _ in range(n):
    row = list(input())
    graph.append([1 if cell == "L" else 0 for cell in row])


def bfs(x, y):
    q = deque([(x,y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                tmp_graph[nx][ny] = tmp_graph[x][y] + 1
    max_cnt.append(max(map(max, tmp_graph)))
max_cnt = []
global visited
global tmp_graph
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            tmp_graph=copy.deepcopy(graph)
            tmp_graph[i][j] = 0
            visited[i][j] = True
            bfs(i, j)
            visited = [[False] * m for _ in range(n)]

print(max(max_cnt))


