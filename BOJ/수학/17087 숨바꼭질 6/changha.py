n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 시간초과 
# def gcd(a, b):
#     for i in range(min(a,b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i

def euclid(x, y):
    while y:
        x, y = y, x%y
    return x

distance = [abs(i-s) for i in arr]

gcd_value = distance[0]

for value in distance[1:]:
    gcd_value = euclid(gcd_value, value)

print(gcd_value)


