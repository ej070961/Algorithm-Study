#10989 수 정렬하기3
# import sys
# from collections import deque

# N=int(sys.stdin.readline()) #수의 개수
# # print('몇 개 입력할꺼야: ', N)
# #A=[]#사용자가 입력한 수를 담을 배열
# A=deque()

# for i in range (N):
#     num = int(sys.stdin.readline())
#     # print(i+1,'번째 숫자 : ', num)
#     A.appendleft(num)
# # print("정렬 전 A: ",A)

# #정렬 성공 여부를 나타내는 플래그를 도입함

# is_sorted=False

# while not is_sorted:
#     is_sorted=True
#     for i in range(N-1):
#         if A[i]>=A[i+1]:
#             A[i],A[i+1]=A[i+1],A[i]
#             is_sorted=False

# # print("정렬 후 A: ",A)

# for i in range (N):
#     print(A[i])

# #아니 sort함수를 안썼는데도 메모리 초과가 나는데 for문안에 append를 쓰는게 문제였다니
# #1. 리스트 대신 deque를 썼는데도 메모리 초과
# #2. 당연하거긴 한데 append대신 appendleft써도 메모리 초과

#결국 계수정렬 기반으로 입력 받는 수의 범위가 제한적이라는 점을 이용해 코드를 작성함
import sys

N = int(sys.stdin.readline())
# 가능한 입력 범위가 1부터 10,000까지이므로, 각 숫자를 인덱스로 하는 리스트를 생성하고, 처음에는 모두 0으로 초기화합니다.
counts = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1  # 입력 받은 숫자의 빈도를 카운트합니다.

for i in range(1, 10001):
    if counts[i] > 0:  # 해당 숫자가 한 번 이상 입력되었다면,
        for _ in range(counts[i]):  # 그 숫자를 입력된 횟수만큼 출력합니다.
            print(i)




