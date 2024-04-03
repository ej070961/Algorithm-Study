import sys 
from collections import deque

n, m = map(int, sys.stdin.readline().split())

area = [[]*m for _ in range(n)]

for i in range(n):
    area[i] = list(sys.stdin.readline().rstrip())

# print(area)

def bfs(area, x,y):
    visited = [[False]*m for _ in range(n)]
    queue = deque([(x,y)])

    # cost = 1

    while queue:
        a, b = queue.popleft()
        # cost += 1
        visited[a][b] = True

        if a == n-1 and b == m-1:
            return area[a][b]
        
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            dx = dx + a
            dy = dy + b
            # print(dx,dy)
            if 0<=dx<n and 0<=dy<m:
                if not visited[dx][dy] and int(area[dx][dy]) == 1:
                    queue.append((dx,dy))
                    area[dx][dy] = int(area[a][b]) + 1

print(bfs(area, 0,0))

