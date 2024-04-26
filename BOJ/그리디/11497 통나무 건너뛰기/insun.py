#11497 통나무 건너뛰기

import sys

T= int(sys.stdin.readline())

for i in range (T):
    t_num = int(sys.stdin.readline())
    t_height = [int(x) for x in sys.stdin.readline().split()]
    #입력받은 문자열을 정수로 바로 변환
    t_height.sort()

    max_level = 0
    for i in range(2,t_num):
        max_level=max(max_level,abs(t_height[i]-t_height[i-2]))
    #왜 2인가?
    #유독 차이가 큰 경우를 바로 인접하게 하면,  n-1과 n+2사이의 격차가 n과 n+1사의 격차보다 크므로,난이도를 줄이지 못함

    print(max_level)
