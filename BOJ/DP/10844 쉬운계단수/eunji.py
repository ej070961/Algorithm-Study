import sys

n = int(sys.stdin.readline())

# DP 테이블 초기화
# dp[i][j]는 길이가 i이고, 마지막 숫자가 j인 계단 수의 개수를 의미
# j의 범위는 0~9
dp = [[0 for _ in range(10)] for _ in range(0, n+1)]

# 초기 조건 설정: dp[1][1~9]를 모두 1로 초기화
for i in range(0, 9):
    dp[1][i] = 1

# DP 진행
for i in range(2, n+1):
    for j in range(10):
        # 끝자리가 0일 때
        if j==0:
            dp[i][j] = dp[i-1][1]
        # 끝자리가 9일 때 
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# 길이가 n인 계단 수의 총 합을 계산
result = sum(dp[n]) % 1000000000

print(result)