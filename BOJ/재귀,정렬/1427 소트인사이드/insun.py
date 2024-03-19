#1474 소트인사이드
import sys

# 1. 반복문을 이용해서 버블 정렬(인접한 요소들끼리 비교해서 정렬하기)_처음 시도, 실패
# N=list(str(input()))
# print("내가 정렬하고자 하는 숫자 :",N)
# while int(str(N[len(N)-1]))==int(min(int(str(N)))): <-----여기 조건 대문에ㅜㅜ
#     for i in range(len(N)-1):
#         print(i+1,"번째 요소 : ",N[i])
#         if int(N[i])<int(N[i+1]):
#             print(N[i],"가",N[i+1],"보다 작다")
#             N[i],N[i+1]= N[i+1],N[i]
#         else:
#             print(N[i],"가",N[i+1],"보다 크다")
#             N[i],N[i+1]= N[i],N[i+1]
# print(N)


# 2. 반복문을 이용한 버블 정렬_ 지피티, 성공, 정렬 성공 여부를 판단하는 플래그를 도입
# N = list(str(input("숫자를 입력하세요: ")))
# print("내가 정렬하고자 하는 숫자 :", N)

# # 정렬이 완료되었는지 확인하기 위한 플래그
# is_sorted = False

# # 정렬이 완료될 때까지 반복
# while not is_sorted:
#     is_sorted = True  # 반복문 시작 시, 정렬 완료로 가정
#     for i in range(len(N) - 1):
#         # 현재 요소가 다음 요소보다 작다면, 위치를 교환
#         if int(N[i]) < int(N[i + 1]):
#             N[i], N[i + 1] = N[i + 1], N[i]
#             is_sorted = False  # 위치 교환이 일어났으므로, 정렬이 아직 완료되지 않았음을 표시

# print("정렬된 숫자 :", ''.join(N))


#3. 파이썬 내장함수 사용하기
# 입력 받은 숫자를 문자열 리스트로 변환
N = list(str(input()))
#print("내가 정렬하고자 하는 숫자 :", N)

# 문자열 내의 각 숫자를 정수로 변환하고, 내림차순으로 정렬
N = sorted([int(x) for x in N], reverse=True)

# 정렬된 리스트를 문자열로 변환하여 출력
#print("정렬된 숫자 :", ''.join(map(str, N)))
print(''.join(map(str, N)))