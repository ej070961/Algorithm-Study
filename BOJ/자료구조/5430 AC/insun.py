# #5430.py
# from collections.abc import Reversible
# import sys
# from collections import deque

# def R (li):
#     if len(li)==0:
#         print("error")
#     else:
#         # li = deque(li) # 리스트를 deque로 변환
#         # temp = deque(li) # 원본 deque를 복사
#         # li.clear() # 원본 deque를 비워
#         # li.extendleft(temp) # 복사한 deque의 요소를 역순으로 추가
#         li.reverse()
#         li = deque(li)
#     return li

# def D(li):
#     if len(li)==0:
#         print("error")
#     else:
#         li.popleft()
#     return li
        

# T=int(sys.stdin.readline())
# #print("테스트 몇 개? : ",T)

# P=sys.stdin.readline().rstrip()
# #print("내가 입력한 명령어 : ",P)

# n=int(sys.stdin.readline())
# #print("숫자 몇개: ",n)

# original = deque()
# # original = deque(map(int, sys.stdin.readline().rstrip()[1:-1].split(',')))


# for i in range(n):
#     element = int(sys.stdin.readline())
#     original.append(element)

# #print("orginal 초기 배열 : ", original)

# Order = list(P)
# #print("명령어 잘 분리된건지 : ",Order)
# for i in range(len(Order)):
#  #   print(i+1,'번째 명령어 : ',Order[i])
#     if Order[i]=='R':
#         original = R(original)
#         #print("R명령어 하고 나서 배열 상태: ", original)
#     elif Order[i]=='D':
#         # original = D(original)
#         result = D(original)
#         #print("D명령어 하고 나서 배열 상태: ", original)
#         if result == "error":
#             print(result)
#             break

# # print("최종 original 배열", original)
# print(str(list(original)).replace(' ', ''))

from collections.abc import Reversible
from collections import deque

def R (li):
    if len(li)==0:
        print("error")
    else:
        li.reverse()
        li = deque(li)
    return li

def D(li):
    if len(li)==0:
        return "error"
    else:
        li.popleft()
    return li

# 테스트 케이스의 수 T
T = int(input())

for _ in range(T):
    # 함수 P
    P = input().rstrip()

    # 배열의 크기 n
    n = int(input())

    # n개의 배열 요소
    original = deque(map(int, input().strip()[1:-1].split(',')))

    Order = list(P)
    for i in range(len(Order)):
        if Order[i]=='R':
            original = R(original)
        elif Order[i]=='D':
            result = D(original)
            if result == "error":
                print(result)
                break

    print(str(list(original)).replace(' ', ''))
