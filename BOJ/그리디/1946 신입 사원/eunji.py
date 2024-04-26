import sys

#테스트 케이스 개수
t= int(sys.stdin.readline())

result = []
for _ in range(t):
    #지원자 숫자 
    n = int(sys.stdin.readline())
    score_list = [0]*n
    max_cnt = n
    for _ in range(n):
        #서류심사 성적, 면접 성적 입력 받기 
        p, i = map(int, sys.stdin.readline().split(' '))
        score_list[p-1] = i

    min_num = score_list[0]
    for i in range(1, n):
        #서류면접 순위 비교 
        if score_list[i] > min_num:
            max_cnt -= 1
        else:
            min_num = score_list[i]
    result.append(max_cnt)

for i in result:
    print(i)

        

    