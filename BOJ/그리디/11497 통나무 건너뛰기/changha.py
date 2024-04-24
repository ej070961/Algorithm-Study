# 큰 것을 중앙에 두고 오른쪽, 왼쪽 순차적으로 배열함
# [2, 4, 5, 7, 9] => 홀수 일 때 
# 9-7 [4]-[3]
# 9-5 [4]-[2]
# 7-4 [3]-[1]
# 5-2 [2]-[0]
# 4-2 [1]-[0]

# [2, 2, 4, 5, 7, 9] => 짝수 일 때 
# 9-7 [5]-[4]
# 9-5 [5]-[3]
# 7-4 [4]-[2]
# 5-2 [3]-[1]
# 4-2 [2]-[0]
# 2-2 [1]-[0]

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    
    li.sort()
    
    max_res = 0
    
    for i in range(n-1, 1, -1):
        if i == 1:
            max_res = max(max_res, abs(li[i] - li[i-1]))

        if i == n-1:
            max_res = max(max_res, abs(li[i] - li[i-1]))
            max_res = max(max_res, abs(li[i] - li[i-2]))
        else:
            max_res = max(max_res, abs(li[i] - li[i-2]))        

    print(max_res)