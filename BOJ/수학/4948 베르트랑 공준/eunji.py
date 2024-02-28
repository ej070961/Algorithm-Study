import sys

while True:
    n = int(sys.stdin.readline())

    if(n==0):
        break

    is_prime = [True] * (2*n+1)

    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int((2*n)**0.5)+1):
        if(is_prime[i]):
            for j in range(2*i, 2*n+1, i):
                is_prime[j] = False
    
    cnt = 0
    for i in range(n+1, 2*n+1):
        if(is_prime[i]):
            cnt+=1
    
    print(cnt)
