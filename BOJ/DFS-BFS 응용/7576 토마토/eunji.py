import sys
from collections import deque

#상자의 가로 칸의 수, 세로 칸의 수 입력 
m, n = map(int, sys.stdin.readline().split())

tomato = []

for i in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        #만약 익은 토마토라면 
        if tomato[i][j]==1: 
            queue.append((i,j))


while queue:
    a, b = queue.popleft()

    for ba, bb in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ba = ba + a
        bb = bb + b
        # print(ba, bb)
        #범위체크
        if 0<=ba<n and 0<=bb<m:
            #토마토의 값이 0 -> 아직 익지 않고, 방문하지 않음 
            if tomato[ba][bb]==0:
                tomato[ba][bb] = tomato[a][b] + 1
                queue.append((ba, bb))


max_count = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        if tomato[i][j]-1 > max_count:
            max_count = tomato[i][j]-1

print(max_count)
