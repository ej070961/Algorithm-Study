#R => 배열 순서를 뒤집음
#D => 첫번 째 수를 버림 IF, 배열 비어있는데 사용하면 ERROR

# 배열 input 받을 때, [ ] 이거 제외시켜야함 
#Queue 이용 
import sys 
from collections import deque
t = int(sys.stdin.readline())

    
for _ in range(t):
    fun_arr = list(map(str, sys.stdin.readline()))
    n = int(sys.stdin.readline())
    numbers = sys.stdin.readline().rstrip()[1:-1].split(",")

    queue = deque(numbers)
    r = 0

    if n == 0:
        queue = []
        
    
    for i in fun_arr:
        if i == "R":
            r += 1
        elif i == "D":
            if len(queue) == 0:
                print("error")
                break
            else:
                if r % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if r % 2 == 0:
            print('[' + ','.join(queue) + ']')
        else:
            queue.reverse()
            print('[' + ','.join(queue) + ']')

