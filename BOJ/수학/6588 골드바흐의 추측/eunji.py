import sys

MAX = 1000000
is_prime = [True]*(MAX+1)

#MAX보다 작은 홀수 소수 세팅 
for i in range(3, int(MAX**0.5)+1, 2):
    if(is_prime[i]):
        for j in range(i*2, MAX+1, i):
            is_prime[j] = False


while True:
    n = int(sys.stdin.readline())

    if(n==0):
        break

    valid = False
    for i in range(3, int(n//2)+1, 2):
        if(is_prime[i] and is_prime[n-i]):
            print(n, "=", i, "+", n-i)
            valid = True
            break
    if(valid==False):
         print("Goldbach's conjecture is wrong.")