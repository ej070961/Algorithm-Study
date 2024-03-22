n = int(input())

input_list = [0] * 91

input_list[1] = 1
input_list[2] = 1
input_list[3] = 2
for i in range(4, 91):
    input_list[i] = input_list[i-1] + input_list[i-2]

print(input_list[n])