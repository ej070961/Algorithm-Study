import sys

n = int(sys.stdin.readline())

if n==1:
    print(0)
elif n==2:
    print(1)
elif n==3:
    print(1)

else:
#n이 4이상
    dp = [0]*(n+1)

    #n이 1일 때
    dp[1] = 1
    #n이 2일 때
    dp[2] = 1
    #n이 3일 때
    dp[3] = 1

    for i in range(4, n+1):
        dp[i] = 1 + dp[i-1]
        #i가 3의 배수일 때
        if i%3==0:
            if(1 + dp[i//3]) < dp[i]:
                dp[i]= 1 + dp[i//3]
        #i가 2의 배수일 때
        if i%2==0:
            if (1 + dp[i//2]) < dp[i]:
                dp[i] = 1 + dp[i//2]
        # print(i, dp[i])
    print(dp[n])
