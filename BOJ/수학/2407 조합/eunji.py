from sys import stdin

n, m  = list(map(int, stdin.readline().split(' '))) # n, m 값 저장

upper = 1
for i in range(n-(m-1), n+1):
    upper*=i

lower =1 
for j in range(1, m+1):
    lower*=j

print(upper//lower)


