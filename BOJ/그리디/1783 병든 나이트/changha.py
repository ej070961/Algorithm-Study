n, m = map(int, input().split())
res = 0
if n == 1:
    res = 1
elif n == 2:
    if m <= 2:
        res = 1
    elif 3 <= m <= 4:
        res = 2
    elif 5 <= m <= 6:
        res = 3
    else:
        res = 4
elif n >= 3:
    if m <= 6:
        res = min(m, 4)
    else:
        res = m - 2

print(res)