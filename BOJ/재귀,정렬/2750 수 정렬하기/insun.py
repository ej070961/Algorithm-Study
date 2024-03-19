#2750

import sys

N=int(sys.stdin.readline()) 
#print("몇 개의 수를 입력: ",N)
A=[]

for i in range(N):
    num = int(sys.stdin.readline())
    #print(i+1,"번째의 숫자는 : ", num)
    A.append(num)

#print("정렬 전 A: ",A)

is_sorted=False

while not is_sorted:
    is_sorted=True
    for i in range(N-1):
        if A[i]>A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
            is_sorted=False


#print("정렬 후 A: ",A)

for i in range(N):
    print(A[i])