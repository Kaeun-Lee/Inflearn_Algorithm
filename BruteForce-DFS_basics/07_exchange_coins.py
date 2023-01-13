# 7. 동전교환
# 문제 : 여러 단위의 동전들이 주어져 있을 때 거스름돈을 가장 적은 수의 동전으로 교환해 주려면?
#        각 단위의 동전은 무한정 쓸 수 있음
# 조건 : 첫 번째 줄에 동전 종류의 개수 N(1 <= N <= 12)이 주어짐
#        두 번째 줄에 N개 동전의 종류가 주어지고, 그 다음 줄에 거슬러 줄 금액 M(1 <= M <= 500)이 주어짐
#        각 동전의 종류는 100원을 넘지 않음
# 회고 : 가장 큰 수부터 교환한다고 해서 가장 적은 수의 동전을 거슬러 줄 수 있는 게 아님
#        ex. 129 ->* 50*2 + 25*1 + 4*4 = 7개 보다 50*2 + 20*1 + 8*1 + 1*1 = 5개가 더 최소임
#        D(l)로 사용된 동전의 개수를 세고, D(sum)으로 확인하는 방법을 생각하지 못함. 나눗셈으로 풀려다 보니 헷갈렸음
#        if문의 조건을 잘못 걸면 문제가 안 풀리니 주의

# My_Solution -> (테케 3번에서 실패)
def DFS(l, rim):
    if rim == 0:
        print(sum(ch))
    else:
        ch[l] += rim // coins[l]  # 몫을 거슬러준 코인의 수로 추가
        DFS(l + 1, (rim % coins[l]))  # 나머지를 넘겨줌


if __name__ == "__main__":
    n = int(input())
    coins = sorted(map(int, input().split()), reverse=True)  # 가장 큰 수부터 계산
    m = int(input())
    ch = [0] * n  # 0 1 2
    DFS(0, m)


# Solution_1 -> 중복순열 코드와 유사
import sys

sys.stdin = open("input.txt", "r")


def DFS(l, sum):  # l : 사용된 동전의 개수
    global res
    if l > res:  # level이 최솟값보다 크면 종료
        return
    if sum > m:  # 동전의 합이 m을 넘어가면 종료
        return
    if sum == m:
        if l < res:
            res = l
    else:
        for i in coins:  # 동전의 종류만큼 가지를 뻗음
            DFS(l + 1, sum + i)


if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    coins.sort(reverse=True)  # 가장 큰 동전부터 적용
    DFS(0, 0)
    print(res)


# test_case 1
# n = 3
# coins = 1 2 5
# m = 15
# result : 3

# test_case 2
# n = 5
# coins = 1 5 7 11 15
# m = 39
# result : 5

# test_case 3
# n = 5
# coins = 1 8 20 25 50
# m = 129
# result : 5
