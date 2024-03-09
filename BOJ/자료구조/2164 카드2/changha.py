# 위에서부터 아래로 1~N
# 동작반복
# 최상단 카드 버림
# 이후, 최상단 카드를 제일 최하위로 옮김
# queue이용해서 하면 될듯? 
import sys 
from collections import deque

n = int(sys.stdin.readline())
q = deque([])
#초기화
for i in range(n):
    q.append(i+1)

if n == 1:
    print(q[0])
else:
    while True:

        # 최상단 버림 
        tmp = q.popleft()
        # 버렸을 떄 queue가 1개남았을 때 출력 
        if len(q) == 1:
            print(q[0])
            break   
        else:
            # 다음 최상단을 최하위로 옮김 
            q.append(q.popleft())



