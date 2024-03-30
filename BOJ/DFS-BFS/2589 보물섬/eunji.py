import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

area = [[0]*m for _ in range(n)]

def bfs(li, x , y):

    dis = [[-1] * m for _ in range(n)]
    queue = deque([(x,y)])
    dis[x][y] = 0

    while queue:
        a, b = queue.popleft()

        for da, db in ((a+1, b), (a-1, b), (a, b-1), (a, b+1)):
            #범위 체크 
            if da < 0 or da >= n or db < 0 or db >= m:
                continue
            if li[da][db] == 0 or not dis[da][db]==-1:
                continue
            dis[da][db] = dis[a][b] + 1
            queue.append((da,db))

    return max(max(row) for row in dis) 



#W인 지점을 0, L인 지점을 1로 세팅 
for i in range(n):
    str = sys.stdin.readline().rstrip()
    for j in range(m):
        #j번째 인덱스가 L일 경우 
        if str[j]=='L':
            area[i][j] = 1

max_distance = 0
for i in range(n):
    for j in range(m):
        #해당 지점이 육지이면 bfs로 최단거리 배열 생성 
        if area[i][j] == 1:
            max_distance = max(max_distance, bfs(area, i, j))

print(max_distance)