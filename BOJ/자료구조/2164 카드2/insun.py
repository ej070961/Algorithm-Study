#2164 카드2
from collections import deque
import sys

N = int(input())
cards = deque(range(1, N+1))  # 1부터 N까지의 카드를 생성

while len(cards) > 1:  # 카드가 한 장 남을 때까지
    cards.popleft()  # 제일 위의 카드를 버림
    cards.rotate(-1)  # 제일 위의 카드를 아래로 옮김

print(cards[0])  # 남은 카드 출력

# N = int(sys.stdin.readline())
# stash = [] #버리는거
# bottom = [] #바닥에 놓는거
# original = deque(range(1,N+1))


# #print("초기 카드 상태 : ",original)


# #for i in range(N):
# while len(original)>=2:
#     #original.popleft()
#     stash.append(original[0])
#     #print(i+1,'번째에 버린거 : ',original[0])
    
#     #original.remove(original[0])
#     del(original[0])
#     #print(i+1,'번째에 버린 후 original 카드 상태 : ',original)
#     bottom.append(original[0])
#     #print(i+1,'번째에 버린 후 바닥에 놓을 카드 : ',original[0])
#     del(original[0])
#     #original.remove(original[0])
#     #original.popleft()
#     #print(i+1,'번째에 바닥에 놓기전 original 카드 상태 : ',original)
#     original.append(bottom[0])
#     #print(i+1,'번째에 버린 후 바닥에 놓고 original 카드 상태 : ',original)
#     #bottom.popleft()
#     del(bottom[0])
#     #print(i+1,'번째 최종 original 상태 : ',original)
# print(original)

       