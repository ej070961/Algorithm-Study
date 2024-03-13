import sys

n = list(map(int, sys.stdin.readline().rstrip()))

n.sort(reverse=True)

result = ''
for i in n:
    result+=str(i)


print(result)