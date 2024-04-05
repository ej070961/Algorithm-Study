from collections import deque


# 1을 미리 queue에 넣어야 됨 
m, n = map(int, input().split())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

q = deque([])
is_not_zero = True
for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            is_not_zero = False
        if li[i][j] == 1:
            q.append((i,j))
            
def bfs(i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            if li[nx][ny] == 0:
                li[nx][ny] = li[x][y] + 1
                q.append((nx, ny))

if is_not_zero:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                bfs(i, j)
    max_cnt = 0
    is_still_zero = False
    for i in range(n):
        for j in range(m):
            if li[i][j] == 0:
                is_still_zero = True
            if li[i][j] > max_cnt:
                max_cnt = li[i][j]
    
    if is_still_zero:
        print(-1)
    else:
        print(max_cnt-1)