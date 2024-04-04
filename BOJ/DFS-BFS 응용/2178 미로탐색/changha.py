from collections import deque

n ,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs():
    q = deque([])
    q.append((0, 0))
    
    while q: 
        x,y = q.popleft()
        dx = [0, 0, -1 , 1]
        dy = [-1, 1, 0, 0]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
bfs()
print(graph[n-1][m-1])