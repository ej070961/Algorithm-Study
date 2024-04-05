from collections import deque

f, s, g, u, d = map(int, input().split())

li = [-1] * (f+1)
li[s] = 0
q = deque([])
q.append(s)
while q: 

    cur = q.popleft()

    if cur == g:
        print(li[g])
        break
    
    for i in (cur - d, cur + u):
        
        if i <= 0 or i > f:
            continue 
        
        if li[i] == -1:
            li[i] = li[cur] + 1
            q.append(i)

if li[g] == -1:
    print("use the stairs")
