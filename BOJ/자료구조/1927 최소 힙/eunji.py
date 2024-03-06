import sys
import heapq
n = int(sys.stdin.readline())

heap= []
for i in range(n):
    x = int(sys.stdin.readline())

    if x>0:
        # 배열에 x를 추가
        heapq.heappush(heap, x)
    else:
        #배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거 
        print(0 if len(heap)==0 else heapq.heappop(heap))
