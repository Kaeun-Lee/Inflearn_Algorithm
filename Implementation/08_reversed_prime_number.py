# 8. 뒤집은 소수
# 문제 : N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력
#        예를 들어 32를 뒤집으면 23이고, 23은 소수이니 23을 출력함
#        단, 910을 뒤집으면 19로 숫자화해야 함. 첫 자리부터의 연속된 0을 무시함
#        뒤집는 함수인 def reverse(x)와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성
#        출력 순서는 입력된 순서대로 출력
# 조건 : 첫 줄에 자연수의 개수 N(3 <= N <= 100)이 주어지고, 그다음 줄에 N개의 자연수가 주어짐
#        각 자연수의 크기는 100,000를 넘지 않음
# 회고 : 첫 자리부터 연속되는 0만 제거하고, 중간에 나오는 0은 유지해야 함. ex. 100 -> 1, 902 -> 209
#        첫 자리가 0인 경우, 0이 아닌 숫자가 있는 곳을 찾아서 for문의 시작점으로 정해줌
#        1이 소수인지 아닌지 판별하는 코드도 isPrime 함수 내에 넣어줘야 함
#        x를 10으로 나눈 나머지와 몫을 이용하여 식으로 쉽게 구할 수 있음

# My_Solution -> (성공) -> 숫자를 문자열로 치환 후 뒤집음
import math

# import sys

# sys.stdin = open("input.txt", "r")


def reverse(x):
    x = list(reversed(str(x)))  # ["2", "3"]
    result = ""
    start = 0

    for i in range(len(x)):  # 첫 자리부터의 연속된 0이 끝나는 위치 찾기
        if x[i] == "0":
            start += 1
        else:
            break

    for j in range(start, len(x)):
        result += x[j]
    return int(result)


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
nums = map(int, input().split())
for i in nums:  # 32
    num = reverse(i)
    if num != 1 and isPrime(num):  # 숫자가 1이 아니거나 소수인 경우 출력
        print(num, end=" ")


# Solution_2 -> 숫자를 10으로 나눈 나머지와 몫을 이용하여 뒤집음
def reverse(x):
    res = 0
    while x > 0:  # x가 0이 되면 break
        t = x % 10  # x의 일의 자리 숫자
        res = res * 10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):  # 약수는 1과 자기 자신을 제외하고 자신의 절반까지만 존재
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
nums = list(map(int, input().split()))
for x in nums:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")


# test_case 1
# n = 5
# nums = 32 55 62 3700 250
# result : 23 73

# test_case 2
# n = 12
# nums = 50 91 457 52 699 170 413 54 416 97 199 33
# result : 5 19 71 79 991

# test_case 3
# n = 27
# nums = 469 84 8851 189 69 1210 682 57 6217 484 8 3590 662 36 8275 887 17 1254 462 67 8969 141 70 5603 958 100 3843
# result : 953 71 7 859

# test_case 4
# n = 36
# nums = 590 7628 27139 431 73 5652 11890 460 76 3452 2067 902 12 614 18039 518 71 5329 26422 793 41 8808 2878 10 720 49 2808 22122 611 91 8561 27991 408 54 4926 1395
# result : 37 9811 67 2543 17 397 19
