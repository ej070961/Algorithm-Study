import sys
from collections import deque


n = int(sys.stdin.readline())

#range를 이용하여 list만들기 
deq = deque(range(1, n+1))

#n이 2 이하일 경우 
if(n==1):
    print(1)
elif(n==2):
    print(2)

else:
    for i in range(n-2):
        deq.popleft()
        a = deq.popleft()
        deq.append(a)

    deq.popleft() # 마지막 숫자를 버림 
    print(deq[0])

