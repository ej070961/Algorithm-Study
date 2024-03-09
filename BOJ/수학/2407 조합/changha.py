n, m = map(int, input().split())

def factorial(x):
    res = x 
    for i in range(x-1, 0, -1):
        res = res * i
    return res 

res = factorial(n) // (factorial(n-m) * factorial(m))

print(res)