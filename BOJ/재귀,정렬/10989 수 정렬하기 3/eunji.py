import sys

n = int(sys.stdin.readline())

MAX_NUM = 10000
count = [0]*(MAX_NUM+1)

#list의 각 요소를 count 배열의 index로 접근하여 1증가 
for i in range(n):
    num = int(sys.stdin.readline())
    count[num]+=1

#이제 count의 인덱스에 접근하여, 값이 0이상이면, 입력받은 수
for i in range(len(count)):
    if count[i]!=0:
        for _ in range(count[i]):
            print(i)
