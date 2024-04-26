# 주식을 산다.
# 원하는 만큼 가지고 있는 주식을 판다.
# 아무것도 안한다.

# 최대 이익이 되도록 만들어야 함 
# 10, 7, 6 
# max 왼쪽은 다 사야 한다
# max의 위치에 따라 달라짐 => 시간초과
# 뒤에서부터 하면 풀린다.

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a = int(sys.stdin.readline())
    li = list(map(int,sys.stdin.readline().split()))
    n = len(li)
    max_res = 0
    res = 0

    for i in range(n-1, -1, -1):
        if li[i] > max_res:
            max_res = li[i]
        res += max_res - li[i]
    print(res)