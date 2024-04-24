import sys

t = int(sys.stdin.readline())

result = []
for _ in range(t):
    n = int(sys.stdin.readline())
    trees = list(map(int, sys.stdin.readline().split()))
    trees.sort()
    new_list = []
    for i in range(n):
        if i % 2 != 0:
            new_list.append(trees[i])
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            new_list.append(trees[i])

    #첫번째와 맨 끝 나무통  차이계산
    max_num = abs(new_list[0]-new_list[-1])
    for i in range(n-1):
        max_num = max(max_num, abs(new_list[i]-new_list[i+1]))
    result.append(max_num)


for i in result:
    print(i)

