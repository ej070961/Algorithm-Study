from collections import deque 

n, k = map(int, input().split())

MAX_NUM = 100001
graph = [0] * MAX_NUM
q = deque([])
q.append(n)
while q:
    t = q.popleft()
    if t == k:
        print(graph[k])
        break
    
    if 0 <= t-1 < MAX_NUM and graph[t-1] == 0:
        graph[t-1] = graph[t] + 1
        q.append(t-1)
    if 0 <= t+1 < MAX_NUM and graph[t+1] == 0:
        graph[t+1] = graph[t] + 1
        q.append(t+1)
    if 0 <= t*2 < MAX_NUM and graph[t*2] == 0:
        graph[t*2] = graph[t] + 1
        q.append(t*2)

