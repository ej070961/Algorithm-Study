# 1차 서류심사, 2차 면접시험 
# 적어도 다른 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다. => 둘 다 떨어지면 선발 되지 못함
# 최대 인원수를 구하라 

# 3 2
# 1 4
# 4 1
# 2 3
# 5 5


# 하나 기준으로 해볼까 
# 1 2 3 4 5
# 4 3 2 1 5 

# 하나의 기준을 정하고 <-- 틀림
# 오른쪽으로 탐색 
# 가장 커야 됨 


# 1차 시도 = 이중 for문을 이용해서 기준을 모두 한번씩 적용하려고 함 

t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    for _ in range(n):
        a, b = map(int, input().split())
        li.append((a,b))
    li.sort()
    
    max_cnt = 0 # 최대 인원수 저장 변수 
    min_rank =  float('inf') # 현재 가장 큰 수 
    for current in range(n):
        if li[current][1] <= min_rank:
            max_cnt += 1
            min_rank  = li[current][1]
        
    print(max_cnt)

