import sys 
import collections
n = int(sys.stdin.readline())

arr = collections.deque()

def push(item):
    arr.append(item)

def pop():
    if len(arr) != 0:
        print(arr.popleft())
    else:
        print(-1)
def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[0])

def back():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[len(arr)-1])

for _ in range(n):
    in_arr = list(map(str, sys.stdin.readline().split()))
    if len(in_arr) == 2:
        push(int(in_arr[1]))
    else:
        in_text = in_arr[0]
        if in_text == "front":
            front()
        elif in_text == "back":
            back()
        elif in_text == "size":
            size()
        elif in_text == "pop":
            pop()
        elif in_text == "empty":
            empty()
