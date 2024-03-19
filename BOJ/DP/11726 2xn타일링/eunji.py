import sys

#n을 입력 받음 
n= int(sys.stdin.readline())

#2*n 직사각형 채우기
dp = [0]*(n+1)

if n==1:
    print(1)
elif n==2:
    print(2)
else: 
    #n이 1일 때
    dp[1]=1
    #n이 2일 때 

    dp[2]=2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        

    print(dp[n]%10007)

