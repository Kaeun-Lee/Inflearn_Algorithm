# 11. 수들의 조합
# 문제 : N개의 정수 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 가짓수는 총 몇 개가 있는지 출력
#        ex. 5개의 숫자 2 4 5 8 12가 주어지고, 3개를 뽑은 조합의 합이 6의 배수인 조합은 4+8+12, 2+4+12로 2가지가 있음
# 조건 : 첫 줄에 정수의 개수 N(3 <= N <= 20)과 임의의 정수 K(2 <= K <= N)가 주어짐
#        두 번째 줄에 N개의 정수가 주어지고, 세 번째 줄에 M이 주어짐
# 회고 : level과 시작점 s로 DFS를 구성하는 걸 생각하지 못함. 사용한 숫자를 원래대로 돌리는 방법과, 그냥 조합만 구하는 방법을 헷갈림
#        1씩 커지는 숫자가 아니라 랜덤이기 때문에, idx의 값을 이용해야 함
#        조합은 for문이 도는 시작점인 s가 필요함
#        5개 중 3개를 뽑는 방법은 5C3 = 10가지

# My_Solution -> (성공)
def DFS(l, s, sum):  # s : for문을 수행하는 시작 지점, sum : 원소의 합
    global cnt
    if l == k:
        if sum % m == 0:  # 원소의 합이 m의 배수인 경우
            cnt += 1
    else:
        for i in range(s, n):
            res[l] = nums[i]
            DFS(l + 1, i + 1, sum + nums[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)


# Solution_2 -> 조합을 출력할 필요가 없기 때문에 check 변수는 필요 없음
def DFS(l, s, sum):
    global cnt
    if l == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):  # n - 1까지 돌아야 함
            DFS(l + 1, i + 1, sum + nums[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))  # 원소가 idx 0번 ~ n - 1번까지 들어있음
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)


# test_case 1
# n, k = 5 3
# nums = 2 4 5 8 12
# m = 6
# result : 2

# test_case 2
# n, k = 7 3
# nums = 2 4 5 8 12 7 13
# m = 6
# result : 5

# test_case 3
# n, k = 10 3
# nums = 2 4 5 8 12 7 13 3 6 16
# m = 3
# result : 42
