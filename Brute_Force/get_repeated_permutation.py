# 중복순열 구하기
# 문제 : 1부터 N까지 번호가 적인 구슬 중 중복을 허락하여 
#        M번을 뽑아 일렬로 나열하는 방법을 모두 출력
# 조건 : 사전순으로 오름차순으로 출력
#        자연수 N(3 <= N <= 10), M(2 <= M <= N)

# Solution -> tree가 n가닥으로 뻗어나감
import sys
input = sys.stdin.readline  # 입력 양이 많을 때 사용(문자열이 들어오면 .rstrip() 필수)

def DFS(l):
    global cnt
    if l == m:
        for j in range(m):  # 0 1
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):  # 1 2 3
            res[l] = i
            DFS(l + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m  # [0, 0]
    cnt = 0
    DFS(0)
    print(cnt)


# test case
# input : 3 2
# result : 1 1
#          1 2
#          1 3
#          2 1
#          2 2
#          2 3
#          3 1
#          3 2
#          3 3
#          9