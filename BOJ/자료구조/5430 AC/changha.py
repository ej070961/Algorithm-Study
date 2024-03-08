#R => 배열 순서를 뒤집음
#D => 첫번 째 수를 버림 IF, 배열 비어있는데 사용하면 ERROR

# 배열 input 받을 때, [ ] 이거 제외시켜야함 
#Queue 이용 
import sys 
from collections import deque
t = int(sys.stdin.readline())

def reverse_arr(arr):
    arr.reverse()
def delete_arr(arr):
    if len(arr) != 0:
        arr.popleft()
        return False
    else:
        return True
    
for _ in range(t):
    fun_arr = list(map(str, sys.stdin.readline()))
    n = int(sys.stdin.readline())
    in_arr = sys.stdin.readline().strip()
    # 문자열에서 숫자만 추출하기 위해 리스트 표현의 괄호를 제거하고, 쉼표로 구분된 숫자를 분리
    numbers_str = in_arr.strip('[]').split(',')
    # numbers_str = ['1', '2', '3']

    # 문자열 리스트를 정수 리스트로 변환
    if n == 0:
        print("error")
        continue
    numbers = deque(list(map(int, numbers_str)))
    
    error = False
    for i in fun_arr:
        if i == "R":
            reverse_arr(numbers)
        elif i == "D":
            error = delete_arr(numbers)
            if error:
                break

    if error:
        print("error")
    else:
        print(list(numbers))
