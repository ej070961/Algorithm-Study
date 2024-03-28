from collections import deque

n, m, v = list(map(int, input().split()))

graph_dfs = [[] for _ in range(n+1)]
graph_bfs = [[] for _ in range(n+1)]

visited_dfs = [False for _ in range(n+1)] 
visited_bfs = [False for _ in range(n+1)] 

ans_dfs = []
ans_bfs = []

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph_dfs[a].append(b)
    graph_dfs[b].append(a)
    graph_bfs[a].append(b)
    graph_bfs[b].append(a)

for i in range(n+1):
    graph_dfs[i].sort()
    graph_bfs[i].sort()

def dfs(v):
    visited_dfs[v] = True
    ans_dfs.append(v)
    for next in graph_dfs[v]:
        if not visited_dfs[next]:
            dfs(next)

def bfs(v):
    visited_bfs[v] = True
    tmp = deque([])
    tmp.append(v)
    ans_bfs.append(v)
    while tmp:
        t = tmp.popleft()
        if not visited_bfs[t]:
            visited_bfs[t] = True
            ans_bfs.append(t)
        for i in graph_bfs[t]:
            if not visited_bfs[i]:
                tmp.append(i)

dfs(v)
bfs(v)
for i in ans_dfs:
    print(i, end=" ")
print()
for i in ans_bfs:
    print(i, end=" ")

