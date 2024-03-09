m, n = map(int, input().split())
arr = []
def is_prime(x):
    # 1에 대한 처리 
    if x == 1:
        return False

    for i in range(2, int(x**0.5)+1): ## 연산 횟수를 크게 줄임 
        #나뉜다면 False 반환 
        if x % i == 0:
            return False
    # 그외에는 True 
    return True

for i in range(m, n+1):
    if is_prime(i):
        arr.append(i)

for v in arr:   
    print(v)