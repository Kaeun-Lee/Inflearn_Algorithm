# 동전교환
# 문제 : 여러 단위의 동전들이 주어졌을 때, 거슬러 줄 동전의 최소개수를 출력
#        각 단위의 동전은 무한정 쓸 수 있음
# 조건 : 동전의 종류개수 N(1 <= N <= 12), 거슬러 줄 금액 M(1 <= M <= 500)
#        각 동전의 종류는 100원을 넘지 않음

# Solution
def DFS(l, sum):
    global res
    if l > res:  # 레벨이 최솟값인 res보다 크면 리턴
        return
    if sum > m:
        return 
    if sum == m:
        if l < res:
            res = l
    else:
        for i in range(n):  # 동전의 종류 개수만큼 0 1 2
            DFS(l + 1, sum + a[i])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000      # 최솟값을 구해야 하니 큰 값으로 넣어놓음
    a.sort(reverse=True)  # 가장 큰 동전부터 적용
    DFS(0, 0)
    print(res)


# test case
# number of types : 3 
# types of coins : 1 2 5
# pay back : 15
# result : 3