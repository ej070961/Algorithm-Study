n = int(input())

input_list = list(map(int, input().split()))

for i in range(1, n):
    input_list[i] = max(input_list[i-1] + input_list[i], input_list[i])
    
print(max(input_list))