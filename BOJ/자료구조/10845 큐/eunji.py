import sys

n = int(sys.stdin.readline())

queue = []
for i in range(n):
    data = list(sys.stdin.readline().split(' '))

    if data[0] =='push':
        #정수 X를 큐에 추가
        queue.append(int(data[1]))
    elif data[0] == 'pop\n':
        #큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            queue.remove(queue[0])
    elif data[0] == 'size\n':
        #큐에 들어있는 정수의 개수를 출력
        print(len(queue))
    elif data[0] == 'empty\n':
        #큐가 비어있으면 1, 아니면 0을 출력
        print(1 if len(queue)==0 else 0)
    elif data[0] == 'front\n':
        #큐의 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
        print(-1 if len(queue)==0 else queue[0])
    elif data[0] == 'back\n':
        #큐의 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력
        print(-1 if len(queue)==0 else queue[-1])

    
