# 순열 구하기
# 문제 : 1부터 N까지 번호가 적인 구슬 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력
#        총 경우의 수도 출력
# 조건 : 사전순으로 오름차순으로 출력
#        자연수 N(3 <= N <= 10), M(2 <= M <= N)

# Solution -> 중복되지 않도록 check list를 만듦
def DFS(l):
    global cnt
    if l == m:
        for j in range(m):  # 0 1
            print(res[j], end=' ')
        print()
        cnt += 1    
    else:
        for i in range(1, n + 1):  # 1 2 3
            if ch[i] == 0:  # 이미 사용된 i는 사용하지 않음
                ch[i] = 1
                res[l] = i
                DFS(l + 1)
                ch[i] = 0   # 사용한 i를 0으로 다시 돌려줌


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m  # [0, 0]
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)


# test case
# input : 3 2
# result : 1 2
#          1 3
#          2 1
#          2 3
#          3 1
#          3 2
#          6