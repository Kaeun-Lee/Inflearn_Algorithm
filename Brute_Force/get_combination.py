# 조합 구하기
# 문제 : 1부터 N까지 번호가 적힌 구슬 중 M개를 뽑는 방법의 수를 출력
# 조건 : 총 경우의 수도 출력. 출력 순서는 사전순으로 오름차순
#        자연수 N(3 <= N <= 10), M(2 <= M <= N)

# Solution
def DFS(l, s):
    global cnt
    if l == m:
        for j in range(m):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(s, n + 1):
            res[l] = i
            DFS(l + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m  # [0, 0]
    cnt = 0
    DFS(0, 1)
    print(cnt)


# test case
# input : 4 2
# result : 1 2
#          1 3
#          1 4
#          2 3
#          2 4
#          3 4
#          6