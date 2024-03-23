#11726
import sys

N=int(sys.stdin.readline())

d=[0]*(N+1)

# d[1] = 1
# # d[2] = 2


if N==1:
    print(1)

if N==2:
    print(2)
    

if N >=3:
    # d=[0]*(N+1)
    d[1] = 1
    d[2] = 2
    for i in range(3, N+1):
        d[i] = d[i-1] + d[i-2]
    print(d[N]%10007)