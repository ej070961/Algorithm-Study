import sys



def dfs_stack(field, visited, x, y):

    #스택 초기값 설정 
    stack = [(x, y)]
    

    while len(stack) > 0:
        x, y = stack.pop()

        #n,m 범위값 초과 시 건너뜀
        if x < 0 or x >= m or y < 0 or y >= n:
            continue
        #위치 값이 0이거나 이미 방문 했을 경우 건너뜀
        if field[x][y] == 0 or visited[x][y]:
            continue
        
        #방문 표시 
        visited[x][y] = True

        #상하좌우 4가지 값 스택에 푸쉬 
        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))

    return 

t = int(sys.stdin.readline())

result = []

# 테스트케이스 개수 t만큼 반복 
for _ in range(t):
  
    m, n, k = map(int, sys.stdin.readline().split())

    #field[m][n]배열 선언 
    field = [[0 for _ in range(n)] for _ in range(m)] 
    visited = [[False for _ in range(n)] for _ in range(m)] 
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1
        
    count = 0
    for i in range(m):
        for j in range(n):
            #field[i][j]가 1이고, 방문하지 않았을 경우 dfs 함수 시작 
            if field[i][j] == 1 and visited[i][j] == False:
                #새로운 배추 그룹 
                count += 1
                #dfs 시작 
                dfs_stack(field, visited, i, j)

    result.append(count)


for re in result:
    print(re)