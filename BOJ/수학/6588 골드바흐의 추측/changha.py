import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    
    a_prime = []
    for i in range(3, n//2 + 1):
        if is_prime(i):
            a_prime.append(i)
        
    for a in a_prime:
        b = n - a
        if is_prime(b):
            print(str(n) + " = " + str(a) + " + " + str(b))
            break