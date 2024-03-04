import sys

#명령의 수 입력받음
n = int(sys.stdin.readline())

result = []
for i in range(n):
    data = list(sys.stdin.readline().split(' '))
    print(data)
    if data[0]=='push':
        # 정수 x를 스택에 넣는 연산 
        result.append(int(data[1]))
    elif data[0]=='pop\n':
        # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
        print(result.pop() if len(result)!=0 else -1)
    elif data[0]=='size\n':
        # 스택에 들어있는 정수의 개수를 출력
        print(len(result))
    elif data[0]=='empty\n':
        # 스택이 비어있으면 1, 아니면 0을 출력
        print(1 if len(result)==0 else 0)
    elif data[0]=='top\n':
        # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
        print(-1 if len(result)==0 else result[-1])
 
