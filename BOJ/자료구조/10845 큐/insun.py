#10845-큐
import sys
mystack = []

def Push(number):
    mystack.append(number)
    #print(mystack)

def Pop():
    if len(mystack)!=0: #pop은 스택이 비어있지 않을 때만 가능
        print(mystack[0])
        del mystack[0]
        #print(mystack)
    else:
        print(-1)

def Size():
     if len(mystack)!=0:
        #print ("지금 mystack의 size : ", len(mystack))
        print (len(mystack))
        return len(mystack)
     else:
        #print ("지금 mystack의 size : ", len(mystack))
        print (0)
        return 0

def Empty():
    if len(mystack)==0:
        #print("지금 mystack은 비어있음, 1")
        print("1")
        return 1
    else:
        #print("지금 mystack은 비어있지 않음, 0")
        print("0")
        return 0
    
def Front():
    if len(mystack)==0:
        m_top=-1
        #print("-1, 정수 없음")
        print("-1")
        return m_top
    else:
        m_top = mystack[0]
        #print("지금 mystack의 top : ", m_top)
        print(m_top)
        return m_top
   
def Back():
    if len(mystack)==0:
        m_top=-1
        #print("-1, 정수 없음")
        print("-1")
        return m_top
    else:
        m_top = mystack[-1]
        #print("지금 mystack의 top : ", m_top)
        print(m_top)
        return m_top

n = int(sys.stdin.readline())
#print("명령의 수 : " , n)

commands = [] #명령어를 저장할 리스트 초기화
for i in range (n):
    command = sys.stdin.readline().rstrip().split()
    commands.append(command) #명령어를 리스트에 추가

for i in range (n):
    #print("내가 입력한",i+1,"번째 명령어 : ", commands[i])
    if commands[i][0]=='push': #commands[i]만 하면 push 뒤에 있는 숫자까지 같이 받게됨
        Push(int(commands[i][1]))
        #print(mystack)
    if commands[i][0]=='pop': 
        Pop()
        #print(mystack)
    if commands[i][0]=='size': 
        Size()
    if commands[i][0]=='empty': 
        Empty()
    if commands[i][0]=='front': 
        Front()
    if commands[i][0]=='back': 
        Back()





