# 문제 : OX 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말함
#        여러 개의 OX 문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해 다음과 같이 점수 계산을 하기로 함
#        1번 문제가 맞는 경우 1점으로 계산하고, 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산함
#        또한, 연속으로 문제의 답이 맞는 경우 두 번째 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산함
#        틀린 문제는 0점으로 계산함
#        예를 들어, 10개의 OX 문제(1011100110)에서 답이 맞은 문제의 경우 1로 표시하고, 틀린 경우 0으로 표시하였을 때,
#        점수 계산은 1012300120와 같이 계산되어, 총 점수는 10점임
#        시험문제의 채점 결과가 주어졌을 때, 가산점을 고려한 총 점수를 계산
# 조건 : 첫 줄에 문제의 개수 N(1 <= N <= 100)이 주어짐
#        둘째 줄에는 N개 문제의 채점 결과를 나타내는 0 혹은 1이 빈칸을 사이에 두고 주어짐
#        0은 문제의 답이 틀린 경우이고, 1은 문제의 답이 맞는 경우임
# 회고 : 가산점이 증가하는 경우와 리셋되는 경우를 고려하면 쉽게 해결됨

# My Solution -> (정답) 곱셈으로 계산
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
exam = map(int, input().split())
result = 0
tmp = 1

for i in exam:
    if i == 1:
        result += i * tmp
        tmp += 1  # 1이 연속된 경우 가중치 증가
    else:
        tmp = 1
print(result)


# Lecture Solution -> 덧셈으로 계산
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
exam = map(int, input().split())
sum = 0
cnt = 0

for i in exam:
    if i == 1:
        cnt += 1  # 1이 연속된 경우 가중치 증가
        sum += cnt
    else:
        cnt = 0
print(sum)


# Test Case 1
# < input >
# 10
# 1 0 1 1 1 0 0 1 1 0

# output : 10

# Test Case 2
# < input >
# 10
# 0 1 0 0 1 0 1 1 0 0

# output : 5

# Test Case 3
# < input >
# 20
# 0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 1 1

# output : 9
