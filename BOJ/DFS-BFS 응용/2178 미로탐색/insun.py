#2178
#bfs를 사용해 최초로 도달했을 때 깊이를 출력하면 문제를 해결할 수 있다.
#dfs보다 bfs가 적합한 이유는, bfs는 해당 깊이에서 갈 수 있는 노드 탐색을 마친 후 다음 깊이로 넘어가기 때문이다

from collections import deque

# 상하좌우를 탐색하기 위한 리스트 선언
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# dx,dy : 상하좌우를 탐색하기 위한 define값 정의 변수
N,M = map(int, input().split())
# N=row 가로, M=column 세로
A=[[0]*M for _ in range(N)]
# A : 데이터 저장할 2차원 행렬
visited = [[False]*M for _ in range(N)]
# visited는 당연히 방문 기록 저장 리스트

for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j]=int(numbers[j])
        #A리스트에 사용자가 입력한 데이터 싹 저장해줌

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    #큐에 시작 노드 삽입
    visited[i][j] = True
    #visited리스트에 현재 노드 방문 기록
    while queue:
        #queue가 비어있을 때까지 
        now = queue.popleft()
        #큐에서 노드 데이터 가져오고
        for k in range(4): #4는 상하좌우 탐색 의미
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x>=0 and y>=0 and x<N and y<M: #유효한 좌표라면~
                if A[x][y] != 0 and not visited[x][y]: 
                    #1이어야 이동하니까, 이동할 수 있는 칸이면서 False여야 조건문 들어올테니까 방문하지 않은 노드
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1
                    #A리스트에 depth를 현재 노드의 depth + 1로 업데이트함
                    queue.append((x,y))

BFS(0,0)
print(A[N-1][M-1])


