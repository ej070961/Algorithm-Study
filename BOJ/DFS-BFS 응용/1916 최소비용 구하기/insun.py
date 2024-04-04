#1916 최소비용구하기
import sys
from queue import PriorityQueue
#현재 사용할 수 있는 노드들을 우선순위 큐 자료구조에 넣어, 현재 연결된 노드 중 가장 적은 비용을 지니고 있는 노드를 빠르게 찾을 수 있음
#우선순위 큐는 데이터가 새롭게 들어올 때마다 자동으로 정렬됨. 

input = sys.stdin.readline

N=int(input()) #노드 개수
M=int(input()) #에지 개수
MyList = [[] for _ in range(N+1)] #에지 데이터 저장 인접 리스트
dist = [sys.maxsize] *(N+1) #거리 저장 리스트
visit = [False]*(N+1) #방문 여부 저장 리스트

for _ in range(M): #에지 개수만큼 반복
    start,end,weight = map(int,input().split())
    MyList[start].append((end,weight)) #인접리스트에 에지 정보를 저장함

start_index, end_index = map(int,input().split())
def dijkstra(start,end):
    pq = PriorityQueue()
    pq.put((0,start)) #출발 노드를 우선순위 큐에 넣고 시작함->자동으로 거리가 최소인 노드를 가져오는 자료구조
    #우선순위에 데이터를 최단 거리, 노드 순으로 삽입
    dist[start]=0
    while pq.qsize()>0: #큐가 빌 때까지
        nowNode = pq.get()
        now = nowNode[1]
        if not visit[now]: #현재 선택된 노드가 방문한 적이 있는지 확인
            visit[now] = True # 현재 노드를 방문 노드로 업데이트
            for n in MyList[now]: #현재 선택 노드의 에지 개수만큼 반복
                if not visit[n[0]] and dist[n[0]] > dist[now] + n[1]: 
                    #타깃 노드가 방문하기 전이고 현재 선택노드의 최단거리에 비용을 더한것이 타깃노드의 최단거리보다 작다면
                    dist[n[0]] = dist[now] + n[1] #타깃노드의 최단거리 업데이트
                    pq.put((dist[n[0]], n[0]))
                    #우선순위 큐에 타깃 노드 추가
    return dist[end]
    #종료 인덱스의 최종거리 리턴

print(dijkstra(start_index, end_index))
