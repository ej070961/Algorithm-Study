from collections import deque

n = int(input())
global graph
graph = []
global visited 
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(str,input())))

standard = ['R', 'G', 'B']
count = 0
count_blind = 0
def bfs(i, j, std):
    q = deque([])
    q.append((i,j))
    visited[i][j] = True
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] == std:
                visited[nx][ny] = True
                q.append((nx, ny))
        

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] in standard:
            bfs(i, j, graph[i][j])
            count += 1

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'


for i in range(n):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] in standard:
            bfs(i, j, graph[i][j])
            count_blind += 1

        
print(count, count_blind)
