from collections import deque

t = int(input())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    q = deque([(x, y)])
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0   
                q.append((nx, ny))

for _ in range(t):
    m, n, k =list(map(int, input().split()))
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)




