#1463
import sys
N=int(sys.stdin.readline())
D=[0]*(N+1)

'''
점화식
D[i]=i에서 1로 만드는데 필요한 최소 연산 횟수

D[i]=D[i-1]-1 -> 1을 빼주는 연산을 할 경우
if(i%2==0) min(D[i], D[i/2]+1) -> 2로 나눠주는 연산을 할 경우
if(i%3==0) min(D[i], D[i/3]+1) -> 3으로 나눠주는 연산을 할 경우
'''

D[1]=0

for i in range (2,N+1):
    D[i]=D[i-1]+1
    if i%2==0:
        D[i]=min(D[i],D[i//2]+1)
    if i%3==0:
        D[i]=min(D[i],D[i//3]+1)

print(D[N])