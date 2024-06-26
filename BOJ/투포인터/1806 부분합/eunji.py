import sys

L, S = map(int, sys.stdin.readline().split()) 
#수열 리스트
data = list(map(int, sys.stdin.readline().split()))
#디버깅용
step = 0
# end 인덱스 
end = 0
# 부분합
interval_num = data[0]
#카운트
count = L + 1

for start in range(L):
    print("Step", step, "부분합:", interval_num)
    print("start pointer :", start,"end pointer :", end)

    # 부분합이 S보다 작을 경우
    while interval_num < S and end < L-1:
        end += 1
        interval_num += data[end]
        step += 1
        print("Step", step, "부분합:", interval_num)
        print("start pointer :", start,"end pointer :", end)

    if interval_num >= S:
        # 길이 계산
        temp = end - start + 1
        count = min(count, temp)

    #start를 증가시켜야하므로 현재 start가 가리키는 값 빼기 
    interval_num -= data[start]
    step += 1


print(0 if count == L+1 else count)