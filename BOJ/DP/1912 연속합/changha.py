n = int(input())

input_list = list(map(int, input().split()))

# for i in range(1, n):
#     input_list[i] = max(input_list[i-1] + input_list[i], input_list[i])
    
# print(max(input_list))

total_max = input_list[0]
cur_max = [input_list[0]] * n

for i in range(1, n):
    cur_max[i] = max(input_list[i] + cur_max[i-1], input_list[i])
    total_max = max(total_max, cur_max[i])

print(total_max)


