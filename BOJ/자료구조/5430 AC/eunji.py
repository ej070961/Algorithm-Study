from collections import deque
import sys

#테스트 케이스 개수 입력 받기 
t = int(sys.stdin.readline())

for i in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()

    if p.count('D') > n:
        print('error')

    else:

        deq = deque()
        if s != '[]':
            li= list(map(int, s.lstrip('[').rstrip(']').split(',')))
            deq = deque(li)

        reverse_count = 0
        for j in p:
            if j=='R':
                reverse_count += 1
            elif j=='D':
                if reverse_count%2==0: #뒤집을 횟수가 짝수이면, 그대로인 배열 이므로 왼쪽에서 pop
                    deq.popleft()
                else: #뒤집을 횟수가 홀수이면, 뒤집어진 상태이므로 오른쪽에서 pop
                    deq.pop()

        # 마지막에 R의 개수에 따라 뒤집어주기
        if(reverse_count%2!=0):
            deq.reverse()

        #출력 형식을 지켜줘야함 
        print('[' + ','.join(map(str, deq)) + ']')