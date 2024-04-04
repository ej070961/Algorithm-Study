import sys
import heapq  # 우선순위 큐 사용을 위한 heapq 모듈 임포트

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    st, ar, co = map(int, input().split())
    graph[st].append((co, ar))  # 비용을 우선으로 해서 튜플을 구성

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    distance[start] = 0
    
    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

target_st, target_ar = map(int, input().split())

dijkstra(target_st)
print(distance[target_ar])
