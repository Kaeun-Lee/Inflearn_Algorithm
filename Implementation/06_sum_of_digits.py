# 6. 자릿수의 합
# 문제 : N개의 자연수가 입력되면 각 자연수의 자릿수 합을 구하고, 그 합이 최대인 자연수를 출력
#        '자릿수의 합이 같을 경우 입력 순으로 먼저인 숫자'를 출력함
#        각 자연수의 자릿수 합을 구하는 함수를 def digit_sum(x)로 작성하라
# 조건 : 첫 줄에 자연수의 개수 N(3 <= N <= 100)이 주어지고, 그다음 줄에 N개의 자연수가 주어짐
#        각 자연수의 크기는 10,000,000를 넘지 않음
# 회고 : 자릿수의 합을 구하는 내용만 digit_sum(x) 함수 안에 넣었어야 하는데, return 값까지 구함
#        자릿수 관련된 문제는 10진법인 경우 10으로 나눈 몫과 나머지를 활용할 수 있음
#        비슷한 작업을 하는 for문을 줄여서 하나의 for문으로도 값을 내도록 하자

# max = -2147000000으로 하는 이유 : C++의 정수형은 4byte이고 2^31 숫자까지 저장됨(양수 쪽의 실제 최댓값은 2147483647)
#                                  실제 범위는 음수 쪽으로 2^31, 양수 쪽으로 2^31 - 1(숫자 0이 하나를 차지함)임

# My_Solution_1 -> (성공) 문자열로 각 숫자를 분리한 뒤 더하기
def digit_sum(x):
    sum_list = []
    max = -2147000000

    for number in x:  # 125
        tmp = 0
        for i in number:  # 1, 2, 5
            tmp += int(i)
        sum_list.append(tmp)

    for i, s in enumerate(sum_list):
        if s > max:
            max = s
            idx = i
    return x[idx]


n = int(input())  # 3
numbers = list(input().split())  # 문자로 받음. 125 15232 97
print(digit_sum(numbers))


# My_Solution_2 -> list comprehension 이용
def digit_sum(x):
    n_sum = 0
    while x:
        n_sum += x % 10  # 나머지
        x = x // 10  # 몫
    return n_sum


n = int(input())
nums = list(map(int, input().split()))
result = [(i, digit_sum(num)) for i, num in enumerate(nums)]
result = sorted(result, key=lambda x: (x[-1], -x[0]), reverse=True)
print(nums[result[0][0]])


# Solution_3 -> 각 숫자를 10으로 나눈 나머지와 몫을 이용
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0  # 자릿수를 더할 변수
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


max = -2147000000
for x in a:  # list의 각 숫자에 접근
    total = digit_sum(x)  # 각 숫자의 자릿수 합 구하기
    if total > max:
        max = total
        result = x
print(result)


# Solution_4 -> (pythonic한 방법) 문자열 이용
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for i in str(x):  # 정수 x를 문자열화, i : 문자열의 문자 하나에 접근
        sum += int(i)
    return sum


max = -2147000000
for x in a:  # list의 각 숫자에 접근
    total = digit_sum(x)  # 각 숫자의 자릿수 합 구하기
    if total > max:
        max = total
        result = x
print(result)


# Solution_5
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
total = list(map(int, input().split()))


def digit_sum(x):  # 자릿수의 합 구하는 함수
    string = str(x)
    result = sum(int(string[i]) for i in range(len(string)))
    return result


result = list(map(digit_sum, total))
max_sum = max(result)

for i in range(n):
    if max_sum == result[i]:
        max_index = i  # max 값에 해당하는 게 2개 이상일 경우 index가 가장 작은 것을 출력
        break

with open("output6.txt", "a") as f:
    print(total[max_index], file=f)


# test_case 1
# n = 3
# numbers = 125 15232 97
# return : 97

# test_case 2
# n = 7
# numbers = 137 460 603 40 521 128 125
# return : 137

# test_case 3
# n = 50
# numbers = 401 100 932 79 822 233 192 18 491 965 34 477 255 948 906 959 528 949 200 138 886 66 535 337 493 154 500 717 336 99 849 390 578 659 853 216 590 417 447 724 507 208 675 377 824 780 708 482 790 127
# return : 959
