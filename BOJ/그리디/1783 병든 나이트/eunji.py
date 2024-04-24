import sys

n, m = map(int, sys.stdin.readline().split())

if n==1:
    result = 1
elif n==2:
    if 1<=m<=6:
        result = (m+1)//2
    elif m>=7:
        result = 4
elif n>=3:
    if 1<=m<=6:
        result = min(m,4)
    elif m>=7:
        result = m-2

print(result)