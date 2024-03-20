#10844
# 쉬운 계단 수
import sys
N = int(sys.stdin.readline())

DP = [[0]*10 for _ in range(N+1)]
for i in range(10):
    if i == 0:
        continue
    DP[1][i] = 1
    #길이가 1일때의 초기값 설정

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
            #j가 0일때 앞에는 1밖에 올 수 없음

        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
            #j가 9일 때 앞에는 8밖에 올 수 없음

        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
            #앞에는 1 작은 것, 1 큰 것 두 가지가 올 수 있음

print(sum(DP[-1]) % 1000000000)