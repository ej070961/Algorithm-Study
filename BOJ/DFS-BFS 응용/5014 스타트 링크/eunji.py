import sys
from collections import deque
f, s, g, u, d = map(int, sys.stdin.readline().split())

def bfs(s):
    # dis 배열 초기값을 -1로 하여 값이 -1일 경우, 방문하지 않았음을 판별할 수 있도록 함 
    dis = [-1]*(f+1)
    queue = deque([s])

    #시작지점의 거리는 0
    dis[s] = 0

    while queue:
        point = queue.popleft()
        
        if point == g:
            return dis[g]
        
        for bs in (point+u, point-d):
            #범위 체크, 방문 여부 체크 
            if 1<=bs<=f and dis[bs] == -1:
                dis[bs] = dis[point] + 1
                queue.append(bs)
    
    #탐색이 종료되었는데도 return되지 않았으면, 엘레베이터를 통해 이동할 수 없는 것이므로 "use the stairs" 리턴 
    return "use the stairs"

#강호의 현재 위치 s
print(bfs(s))