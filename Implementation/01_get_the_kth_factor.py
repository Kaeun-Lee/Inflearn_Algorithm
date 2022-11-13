# 1. K 번째 약수
# 문제 : 어떤 자연수 p와 q가 있을 때, p를 q로 나눈 나머지가 0이면 q는 p의 약수이다
#        두 개의 자연수 N와 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력
#        오름차순 정렬했을 때 K번째로 나타나는 숫자를 출력
#        *만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않으면 -1을 출력
# 조건 : 첫째 줄에 N(1 <= N <= 10,000)과 K(1 <= K <= N)가 빈칸을 사이에 두고 주어짐

# 회고 : 풀이 방법은 쉽게 생각해 냈으나, 모든 약수를 구하지 않아도 되는 방법을 생각하지 못함
#        range는 1부터 시작하기 때문에 순서는 보장됨. 주어진 조건을 이용해 메모리와 시간을 아끼자

# My_Solution -> n의 모든 약수를 구함
def kth_factor(n, k):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    if len(result) < k:
        return -1
    else:
        return result[k - 1]


# Solution_2 -> k번째 까지의 약수만 구함
def kth_factor(n, k):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            return i
    else:
        return -1


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(kth_factor(n, k))


# test case 1
# n, k = 6, 3
# return : 3

# test case 2
# n, k = 25, 5
# return : -1

# test case 3
# n, k = 100, 5
# return : 10
