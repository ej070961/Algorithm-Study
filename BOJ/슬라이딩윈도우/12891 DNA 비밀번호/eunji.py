import sys

#문자열 길이 S, 부분문자열 길이 P
S, P = map(int, sys.stdin.readline().split())

data = sys.stdin.readline().rstrip()

a, c, g, t = map(int, sys.stdin.readline().split())

answer = 0

test = data[0:P]
org_a = test.count('A')
org_c = test.count("C")
org_g = test.count("G")
org_t = test.count("T")

# 각 문자열 개수가 최소 개수보다 많으면 answer 1 증가
if org_a >= a and org_c >= c and org_g >= g and org_t>=t and org_a + org_c + org_g + org_t==P:
    answer += 1


for i in range(P, len(data)):
    #처음 시작 시 초기화 
    # if i==0:
    #     test = data[0:P]
    #     org_a = test.count('A')
    #     org_c = test.count("C")
    #     org_g = test.count("G")
    #     org_t = test.count("T")
    
    if data[i-P] == "A":
        org_a -= 1
    elif data[i-P] == "C":
        org_c -= 1
    elif data[i-P] == "G":
        org_g -= 1
    elif data[i-P] == "T":
        org_t -= 1

    if data[i] == "A":
        org_a += 1
    elif data[i] == "C":
        org_c += 1
    elif data[i] == "G":
        org_g += 1
    elif data[i] == "T":
        org_t += 1

    # 각 문자열 개수가 최소 개수보다 많으면 answer 1 증가
    if org_a >= a and org_c >= c and org_g >= g and org_t>=t and org_a + org_c + org_g + org_t ==P:
        answer += 1

print(answer)