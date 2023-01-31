# 1. 회문 문자열 검사
# 문제 : N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면
#        YES를 출력하고 회문 문자열이 아니면 NO를 출력
#        단, 회문을 검사할 때 대소문자를 구분하지 않음
# 조건 : 첫 줄에 정수 N(1 <= N <= 20)이 주어지고, 그다음 줄부터 N개의 단어가 입력됨
#        각 단어의 길이는 100을 넘지 않음
# 회고 : 문자열 slicing과 indexing으로 해결. a[start:end:step]
#        pythonic한 코드도 좋지만 직접 비교하며 구현하는 손 코딩 면접에서는 두 번째 solution을 사용하기

# My_Solution -> (성공) 문자열 slicing 이용. pythonic한 코드
import sys

sys.stdin = open("input.txt", "r")
n = int(input())

for i in range(n):
    string = input().lower()
    if string == string[::-1]:  # 문자열의 마지막 요소부터 가져오며 반대로 뒤집음
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")


# # Solution_2 -> s[-1] indexing으로 접근
n = int(input())
for i in range(n):
    s = input().upper()
    for j in range(len(s) // 2):
        if s[j] != s[-1 - j]:
            print(f"#{i + 1} NO")
            break
    else:  # for ~ else문
        print(f"#{i + 1} YES")


# test_case 1
# n = 5
# string = level
#          moon
#          abcba
#          soon
#          gooG
# result : #1 YES
#          #2 NO
#          #3 YES
#          #4 NO
#          #5 YES

# test_case 2
# n = 7
# string = stts
#          moon
#          abcba
#          yes
#          goodboy
#          stttttts
#          tttttttttttttt
# result : #1 YES
#          #2 NO
#          #3 YES
#          #4 NO
#          #5 NO
#          #6 YES
#          #7 YES
