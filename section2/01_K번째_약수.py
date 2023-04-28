# 문제 : 어떤 자연수 p와 q가 있을 때, p를 q로 나눈 나머지가 0이면 q는 p의 약수이다
#        두 개의 자연수 N와 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력
#        오름차순 정렬했을 때 K번째로 나타나는 숫자를 출력
#        *만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않으면 -1을 출력
# 조건 : 첫째 줄에 N(1 <= N <= 10,000)과 K(1 <= K <= N)가 빈칸을 사이에 두고 주어짐

# 회고 : 풀이 방법은 쉽게 생각해 냈으나, 모든 약수를 구하지 않아도 되는 방법을 생각하지 못함
#        range는 1부터 시작하기 때문에 순서는 보장됨. 주어진 조건을 이용해 메모리와 시간을 아끼자
#        n의 제곱근까지의 약수 쌍을 구하면 시간을 절약할 수 있음

# My Solution -> (정답) n의 모든 약수를 구함
import sys

sys.stdin = open("input.txt", "r")


def kth_factor(n, k):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    if len(result) < k:
        return -1
    else:
        return result[k - 1]


# Lecture Solution -> k번째까지의 약수만 구함
import sys

sys.stdin = open("input.txt", "r")


def kth_factor(n, k):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            return i
    else:  # for문 도중 return되지 않은 경우, else문 실행
        return -1


# Another Solution -> n의 제곱근까지의 약수만 구하여 시간 절약
import sys

sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
result = []

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        result.extend((i, n // i))  # 약수 쌍을 모두 저장

result = sorted(set(result))  # 16의 약수인 4의 경우 중복 제거
print(result[k - 1] if len(result) >= k else -1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(kth_factor(n, k))


# Test Case 1
# input : 6 3
# output : 3

# Test Case 2
# input : 25 5
# output : -1

# Test Case 3
# input : 100 5
# output : 10
