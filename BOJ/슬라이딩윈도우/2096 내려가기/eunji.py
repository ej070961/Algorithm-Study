import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
dp_max = data
dp_min = data


for i in range(N-1):
    data = list(map(int, sys.stdin.readline().split()))
    dp_max = [data[0] + max(dp_max[0],dp_max[1]), data[1] + max(dp_max[0], dp_max[1], dp_max[2]), data[2] + max(dp_max[1], dp_max[2])]
    dp_min = [data[0] + min(dp_min[0],dp_min[1]), data[1] + min(dp_min[0], dp_min[1], dp_min[2]), data[2] + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))

