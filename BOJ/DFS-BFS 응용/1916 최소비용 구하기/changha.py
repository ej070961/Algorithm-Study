import heapq

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
i, j = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # 이전에 처리된 노드 
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(i)
print(distance[j])