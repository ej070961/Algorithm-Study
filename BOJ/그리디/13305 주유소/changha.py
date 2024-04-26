# Thinking
# 최소 변수를 만듦
# 도시에 도착했을 때 최소인지 아닌지 판별
# 최소x=> 이전 최소값으로 다음 주행할 거리 만큼만 곱하면 됨
# 최소o=> 갱신 후 곱하면 됨 

n = int(input())
distances = list(map(int,input().split()))
cities = list(map(int,input().split()))

min_oil = cities[0]
res = 0

for i in range(n-1):
    if min_oil > cities[i]:
        min_oil = cities[i]
    res += min_oil * distances[i]

print(res)