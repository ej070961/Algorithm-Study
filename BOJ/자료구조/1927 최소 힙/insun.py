#1927 최소힙
# A=[] #사용자가 입력한 수들을 저장하는 배열
# N = int(sys.stdin.readline()) #몇개의 숫자를 입력할 건지
# answer = []

# for i in range(N):
#     x = int(sys.stdin.readline())#N횟수만큼 숫자를 입력받음
#     if(x>0):#자연수면 배열에 저장
#         A.append(x)
#     if(x==0):
#         if(len(A)==0):#사용자가 입력한 값이 O인데 지금 배열이 비어있으면
#             answer.append(0)
#             print(0)
#         else:
#             print(min(A))
#             answer.append(min(A))
#             A.remove(min(A))

# print (answer)

#print("A:", A)
#B = A.count(0)
#print("B:", B)
#for i in range(zero):
#    print(min(A))
    #A.remove(x)

import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap: # 힙이 비어있지 않을 경우
            print(heapq.heappop(heap)) # 가장 작은 값을 출력하고 제거
        else: # 힙이 비어있을 경우
            print(0)
    else:
        heapq.heappush(heap, x) # 힙에 x 추가
