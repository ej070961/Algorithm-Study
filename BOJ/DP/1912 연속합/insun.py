# #1912
# import sys

# N=int(sys.stdin.readline())
# print("N: ",N)

# dp=[0]*(N)
# sum_dp=[0]*N

# for i in range (N):
#     num=int(sys.stdin.readline())
#     print("num: ",num)
#     dp[i]=num
#     for j in range (i):
#         sum_dp[i]=sum_dp[i-1]+sum_dp[i-j]
#     print("sum_dp: ",sum_dp)

# print("dp: ",dp)
# print(max(sum_dp))

import sys

N = int(input())  
nums = list(map(int, input().split()))  # 수열을 한 번에 입력

# DP 테이블 초기화: 각 위치에서 끝나는 최대 부분합을 저장
dp = [0] * N
dp[0] = nums[0]  # 첫 번째 원소로 초기화

# 연속된 수들의 최대 합을 DP를 사용하여 계산
for i in range(1, N):
    # 현재 위치의 값과 이전 위치까지의 최대 부분합 + 현재 위치의 값을 비교하여 더 큰 값을 선택
    dp[i] = max(dp[i-1] + nums[i], nums[i])

# 구해진 최대 부분합 중 가장 큰 값을 출력
print(max(dp))
