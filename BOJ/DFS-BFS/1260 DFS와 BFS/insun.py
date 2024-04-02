#1206
from collections import deque
N,M,Start = map(int,input().split())
A=[[] for _ in range(N+1)] #이거 이차원 배열임 근데 당연함ㅋㅋ
# 인접리스트에 그래프 데이터 저장

print("노드의 개수 : ",N)
print("에지의 개수 : ",M)
print("탐색을 시작할 노드의 번호 : ",Start)

for _ in range(M):
    s,e=map(int,input().split())
    #s노드에서 시작해서 e노드로 에지가 연결되는 것
    A[s].append(e)
    A[e].append(s)
    #양방향 에지이므로 양쪽에 에지를 더하기

for i in range(N+1):
    A[i].sort() #각 노드와 관련된 에지를 정렬
    #번호가 작은 노드부터 방문하기 위해서 정렬하기

def DFS(v):
    print(v,end='')
    visited[v]=True #visited 리스트에 현재 노드 방문 기록하기
    for i in A[v]:#현재 노드의 연결 노드 중
        if not visited[i]: #visited[i]가 false이면 조건문에 들어갈 것임 =  현재 노드의 연결노드 중 방문하지 않은 노드로 DFS 실행하기(재귀함수형태)
            DFS(i)

visited = [False]*(N+1)
DFS(Start)

def BFS(v): #인수로 Start, 탐색을 시작할 노드가 들어올 것임
    queue = deque()
    queue.append(v) #자료구조에 시작노드를 삽입
    visited[v]=True #visited리스트에 현재 노드의 방문 기록하기
    while queue: #queue가 true면 계속 while문에 들어갈 것임, 그 말은 queue가 false여야 while에 안들어감 = 큐가 비어있을 때까지
        now_Node = queue.popleft() #큐에서 노드 데이터를 가져오기
        print(now_Node, end='')#현재 가져온 노드 출력
        for i in A[now_Node]:#현재 노드의 연결 노드 중
            if not visited[i]: #visited[i]가 false면 조건문에 들어갈 것임, 현재 노드의 연결노드 중 미방문노드라면~
                visited[i]=True #미방문 노드를 방문리스트에 true로 기록하고
                queue.append(i) #미방문 노드를 큐에 삽입

print()
visited=[False]*(N+1)#리스트 초기화
BFS(Start)



