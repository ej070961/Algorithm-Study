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