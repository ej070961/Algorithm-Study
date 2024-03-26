import sys
from collections import deque

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        # 가장 작은 정점 번호를 먼저 pop
        node = stack.pop()
        # print("node : ", node)
        if node not in visited:
            visited.append(node)
            # print("visitied : ", visitied)
            item = list(set(graph[node]) - set(visited))
            if(len(item)>1):
                item.sort(reverse=True)
                # print(item)
            stack.extend(item)
            # print("stack", stack)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        # print("node : ", node)
        if node not in visited:
            visited.append(node)
            # print("visitied : ", visitied)
            graph[node].sort()
            queue.extend([n for n in graph[node] if n not in visited])
            # print("queue", queue)
    return visited

n, m, v = map(int, sys.stdin.readline().split())

#정점의 개수만큼의 2차원 배열 리스트 생성 
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    #a 정점의 리스트에 연결된 b 정점 추가
    graph[a].append(b)
    #b 정점의 리스트에 연결된 a 정점 추가
    graph[b].append(a)


# print(graph)
dfs_result = dfs(graph, v)
bfs_result = bfs(graph, v)
print(' '.join(map(str,dfs_result)))
print(' '.join(map(str,bfs_result)))
