import sys
from collections import deque
#테스트케이스 수 입력받음 
t = int(sys.stdin.readline())

result = []

for _ in range(t):
    # date 수
    n = int(sys.stdin.readline())
    stock= deque(map(int, sys.stdin.readline().split()))
    my_stock_count = 0
    my_stock_price = 0
    max_price = 0
    while stock:
        stock_price = stock.pop()
        if stock_price > max_price:
            if my_stock_count > 0:
                 my_stock_price += max_price*my_stock_count
                 my_stock_count = 0
                #  print("count, price : ", my_stock_count, my_stock_price)
            max_price = stock_price
           
        elif stock_price < max_price:
            #주식을 산다 
            my_stock_count += 1
            my_stock_price -= stock_price
            # print("count, price : ", my_stock_count, my_stock_price)

    if my_stock_count > 0:
        my_stock_price += max_price*my_stock_count
        my_stock_count = 0
        # print("count, price : ", my_stock_count, my_stock_price)

    result.append(my_stock_price)

for i in result:
    print(i)