import sys

#도시의 개수
n = int(sys.stdin.readline())
#도시간의 길이
length = list(map(int, sys.stdin.readline().split()))
#기름 가격
price = list(map(int, sys.stdin.readline().split()))

min_price = price[0]
total_cost = 0


for i in range(n-1):
    if price[i] < min_price:
        #순회 중 만약 해당 도시 기름 가격이 최소가격이라면 min_price로 설정
        min_price = price[i]
        # print("min_price, total_length", min_price, total_length)
        # print("total_cost : ", total_cost)
    total_cost += min_price*length[i]

        # print("min_price, total_length", min_price, total_length)
        # print("total_cost : ", total_cost)


    
print(total_cost)