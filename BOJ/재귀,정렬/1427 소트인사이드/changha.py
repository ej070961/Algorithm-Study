n = input()
input_list = [int(char) for char in n]
input_list.sort(reverse=True)

for i in input_list:
    print(i, end="")


