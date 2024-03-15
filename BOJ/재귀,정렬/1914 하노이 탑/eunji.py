import sys 

n = int(sys.stdin.readline())

def hanoi(count, start, sub, objective):
    if count == 1:
        print(start, objective)
        return
    hanoi(count-1, start, objective, sub) #n-1개의 원반을 start에서 sub로 이동 
    print(start, objective)#마지막 남은 하나의 원반을 start에서 objective 기둥으로 이동 
    hanoi(count-1, sub, start, objective) #sub 기둥에 있던 n-1개의 원반을 start를 서브 기둥으로 활용하여 objective로 이동 



print(2**n-1) # 총 이동 횟수 
if n <= 20:
    hanoi(n, 1, 2, 3)
