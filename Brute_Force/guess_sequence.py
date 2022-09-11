# 수열 추측하기

# Solution -> n!의 가짓수, 하나의 순열이 나오면 규칙을 이용하여 계산
import sys
def DFS(l, sum):
    if l == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit()
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[l] = i
                DFS(l + 1, sum + (p[l] * b[l]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n         # [0, 0, 0, 0]. 순열 만들 곳
    b = [1] * n         # [1, 1, 1, 1]. 이항계수 초기화
    ch = [0] * (n + 1)  # [0, 0, 0, 0, 0]
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i 
    DFS(0, 0)


# test case
# input : 4 16
# result : 3 1 2 4