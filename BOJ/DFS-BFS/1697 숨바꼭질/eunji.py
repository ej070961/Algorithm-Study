import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

#해당 지점을 탐색했는지 체크하기 위한 체크 배열
visited = [False]*100001

#n 지점 부터 k지점까지 거리를 저장하기 위한 dis 배열
dis = [0] * 100001

def bfs(visited, start):
    #초기 stack값 세팅 
    queue = deque([start])
    #초기 위치 방문 체크 
    visited[start] =True

    while queue:

        c = queue.popleft()

        #방문한 곳이 k일 경우 
        if c == k:
            return dis[c]
        
        #방문했다고 체크 
        visited[c] = True

        #3가지 경우의 수 체크 
        for next_c in (c-1, c+1, 2*c):
            if 0<=next_c<=100000 and not visited[next_c]:
                visited[next_c] = True
                #현재 위치에서 다음 위치까지 거리 계산 
                dis[next_c] = dis[c] + 1
                queue.append(next_c)
if(n==k):
    print(0)
else: 
    print(bfs(visited, n))
