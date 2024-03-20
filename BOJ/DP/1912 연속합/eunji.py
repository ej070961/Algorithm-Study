import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))

#n크기의 배열 생성 
dp = [0] * n
#첫번째 원소 저장 
dp[0] = nums[0]
#2번째 원소부터 새로운 배열의 합으로 갈지, 이전 요소를 포함시킬지 결정 
for i in range(1, n):
    #새로운 원소와 이전합에 새로운 원소를 더한 값 비교하여 더 큰 값 저장 
    dp[i] = max(nums[i], dp[i-1]+nums[i])
print(max(dp))