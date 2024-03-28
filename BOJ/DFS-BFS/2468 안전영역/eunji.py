import sys

n = int(sys.stdin.readline())

area = [[]] * n

for i in range(n):
    area[i] = list(map(int, sys.stdin.readline().split()))

#최대 높이 구하기 
max_height = max(max(row) for row in area) 

def dfs(area, height, x, y):
    #초기 스택값 
    stack = [(x,y)]

    while stack:
        a, b = stack.pop()
        # print("a, b:", a, b)
        visited[a][b] = True

        #4가지 방향에 대해 체크 
        if(a + 1 < n and not visited[a+1][b] and area[a+1][b] > height):
            stack.append((a+1,b))
        if(a - 1 >= 0 and not visited[a-1][b] and area[a-1][b] > height):
            stack.append((a-1, b))
        if(b + 1 < n and not visited[a][b+1] and area[a][b+1] > height):
            stack.append((a, b+1))
        if(b - 1 >= 0 and not visited[a][b-1] and area[a][b-1] > height):
            stack.append((a, b-1))
        
    # #체크가 끝났으면 return
    # return 

count_list = []
rain_height = 0

while rain_height < max_height:
    # print(rain_height)
    #방문배열 초기화 
    visited = [[False for _ in range(n)] for _ in range(n)]
    #rain 높이에 따라 안전영역 count 시작 
    count = 0
    for x in range(n):
        for y in range(n):
            #영역이 비의 높이 보다 높고, 방문하지 않았다면, 
            if area[x][y] > rain_height and not visited[x][y]:
                count += 1
                dfs(area, rain_height, x, y)
    # print(count)
    #해당 비 높이의 안전영역 개수 append
    count_list.append(count)
    rain_height += 1
# print(count_list)
print(max(count_list) if len(count_list)> 0 else 0)