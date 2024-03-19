n = int(input())
print(2**n - 1)

def hanoi(cnt, start, dest, mid):
    if cnt == 1:
        print(start, dest, sep=" ")
        return 
    if cnt >= 2:
        # 아래의 원판 제외. 시작 기둥에서 보조 기둥으로 
        hanoi(cnt - 1, start, mid, dest)
        # 이동 from 시작 to 대상
        print(start, dest, sep=" ")
        # 아래의 원판 제외. 보조 기둥에서 대상 기둥으로 
        hanoi(cnt - 1, mid, dest, start)
if n <= 20:
    hanoi(n, 1, 3, 2)