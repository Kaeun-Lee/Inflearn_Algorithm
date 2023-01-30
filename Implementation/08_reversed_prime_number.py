# 8. 뒤집은 소수
# 문제 : N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력
#        예를 들어 32를 뒤집으면 23이고, 23은 소수이니 23을 출력함
#        단, 910을 뒤집으면 19로 숫자화 해야 함. 첫 자리부터의 연속된 0을 무시함
#        뒤집는 함수인 def reverse(x)와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성
#        출력 순서는 입력된 순서대로 출력
# 조건 : 첫 줄에 자연수의 개수 N(3 <= N <= 100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어짐
#        각 자연수의 크기는 100,000를 넘지 않음
# 회고 : 001처럼 1이 되는 경우를 제외해야 함. 902는 29가 아니라 209여야 함
#       중간에 있는 0은 0으로 채워야 하고, 처음부터 연속되는 0만 제거해 줘야 함

# My_Solution
import math
import sys

sys.stdin = open("input.txt", "r")


def reverse(x):
    x = reversed(str(x))
    result = ""
    for i in range(len(x)):
        if i != "0":
            result += i
    return int(result)


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    nums = map(int, input().split())
    for i in nums:  # 32
        num = reverse(i)
        if num != 1 and isPrime(num):
            print(num, end=" ")


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
