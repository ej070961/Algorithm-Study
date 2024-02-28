
def is_prime(x):
    for j in range(2, int(x**(1/2))+1):
        if x % j == 0:
            return False
        
    return True
while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for i in range(n+1, 2*n+1):
            if is_prime(i):
                cnt += 1
        print(cnt)
        
