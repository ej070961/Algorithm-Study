import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

max_num = max(map(max, graph))
res_cnt = 0
def bfs(x, y):
    q = deque([(x,y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] >= boundary and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                
        

for i in range(max_num+1): #비가 오지 않을 때도 고려 해야 됨, 따라서 0부터 시작 
    boundary = i
    tmp_cnt = 0
    # 새로운 boundary일 때마다 visited 다시 초기화 해줌 
    global visited
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] >= boundary and visited[j][k] == False:
                visited[j][k] = True
                bfs(j, k)
                tmp_cnt += 1

    res_cnt = max(res_cnt, tmp_cnt)

print(res_cnt)