import sys

def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a

n, s = map(int, sys.stdin.readline().split(' '))

data = list(map(int, sys.stdin.readline().split(' ')))

#최대 공약 수를 찾아야 할 듯 
for i in range(n):
    data[i] = abs(data[i]-s)

result = data[0]
for i in data[1:]:
   result = gcd(result, i)

print(result)