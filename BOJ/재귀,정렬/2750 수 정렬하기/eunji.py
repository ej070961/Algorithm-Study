import sys

n = int(sys.stdin.readline())

list = []
for i in range(n):
    #입력되는 수 리스트에 추가 
    list.append(int(sys.stdin.readline()))


list.sort()

for i in list:
    print(i)