from sys import stdin
m, n = list(map(int, stdin.readline().split(' ')))

is_prime = [True]*(int(n)+1)

is_prime[0] = False
is_prime[1] = False

for i in range(2, int(int(n)**0.5)+1 ):
    if is_prime[i]:
        for j in range(i*2, int(n)+1, i):
            is_prime[j]= False

for i in range(int(m), int(n)+1):
    if is_prime[i]:
        print(i)
    