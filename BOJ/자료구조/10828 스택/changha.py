import sys
N = int(sys.stdin.readline())

arr = []
def push(item):
    arr.append(item)

def size():
    print(len(arr))

def top():
    if len(arr) > 0:
        print(arr[-1])
    else:
        print(-1)
def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)
def pop():
    if len(arr) > 0:
        print(arr.pop())
    else:
        print(-1)
for _ in range(N):

    in_arr = list(map(str, sys.stdin.readline().split()))
    if len(in_arr) == 2:
        push(int(in_arr[1]))
    else:
        in_text = in_arr[0]
        if in_text == 'size':
            size()
        elif in_text == 'pop':
            pop()
        elif in_text == 'top':
            top()
        elif in_text == 'empty':
            empty()
        
