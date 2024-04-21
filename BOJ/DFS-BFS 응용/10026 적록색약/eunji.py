import sys
from collections import deque

n = int(sys.stdin.readline())

area = [] 

for _ in range(n):
    area.append(list(sys.stdin.readline().rstrip()))

global visited

def bfs(color, x, y):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        a, b = queue.popleft()
     
        #상하좌우 체크 
        for ta, tb in ((-1, 0), (1,0), (0,-1), (0,1)):
            ta = ta+a
            tb = tb+b

            #범위체크 
            if ta < 0 or ta >= n or tb < 0 or tb >= n:
                continue

            if not visited[ta][tb] and area[ta][tb] in color:
                visited[a][b] = True
                queue.append((ta, tb))



#rgb 구역 계산
visited = [[False]*n for _ in range(n)]

count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if area[i][j] == 'R' :
                count1+= 1
                bfs(['R'], i, j)
            elif area[i][j] == 'G':
                count1+= 1
                bfs(['G'], i, j)
            elif area[i][j] == 'B':
                count1 += 1
                bfs( ['B'], i, j)


visited = [[False]*n for _ in range(n)]

#적록색약 구역 계산
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if area[i][j] == 'G' or area[i][j] == 'R':
                count2 += 1
                bfs(['R', 'G'] , i, j)
            elif area[i][j] == 'B':
                count2 += 1
                bfs(['B'], i, j)

print(count1, count2)

