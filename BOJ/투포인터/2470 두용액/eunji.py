import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

current_sum = 0
start, end = 0, N-1

#data 정렬 수행
data.sort()
answer = (data[0], data[-1])


while start < end:
  
    current_sum = data[start] + data[end]

    #특성값의 합이 0이면,
    if current_sum == 0:
        answer = (data[start], data[end])
        break

    #저장되어 있던 특성값의 합보다 새로운 특성값 합이 작다면
    elif abs(current_sum) < abs(answer[0] + answer[1]):
        answer = (data[start], data[end])
    
    #특성값의 합이 0보다 클 경우
    if current_sum > 0:
        end -= 1
    elif current_sum < 0:
        start += 1

    
print(answer[0], answer[1])


