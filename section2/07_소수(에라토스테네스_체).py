# 문제 : 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력
#        만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개임
#        제한 시간은 1초
# 조건 : 자연수의 개수 N(2 <= N <= 200,000)이 주어짐
# 회고 : check 변수의 idx 번호가 1부터 n까지의 숫자라고 생각해야 함
#        소수의 배수들은 1과 자기 자신뿐만 아니라 해당 소수를 약수로 가지고 있음
#        while문과 for문으로 구하는 방법 모두 알아놓기

# My Solution -> (정답)
import sys
import math

sys.stdin = open("input.txt", "r")
n = int(input())
ch = [True] * (n + 1)  # idx가 n까지 생기도록 생성

for i in range(2, int(math.sqrt(n)) + 1):  # 1은 소수가 아님
    if ch[i] == True:
        j = 2
        while i * j <= n:  # i의 배수
            ch[i * j] = False
            j += 1
print(sum(ch[2:]))  # 2부터 n개까지의 True 개수를 더함


# Lecture Solution
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
ch = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):  # i의 배수로 증가
            ch[j] = 1
print(cnt)


# Test Case 1
# input : 20
# output : 8

# Test Case 2
# input : 200000
# output : 17984

# Test Case 3
# input : 150000
# output : 13848
