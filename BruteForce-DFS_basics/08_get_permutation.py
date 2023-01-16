# 8. 순열 구하기
# 문제 : 1부터 N까지 번호가 적힌 구슬 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력
#        결과를 출력한 뒤 맨 마지막에 총 경우의 수를 출력
# 조건 : 자연수 N(3 <= N <=10)과 M(2 <= M <= N)이 주어짐. 출력순서는 사전순으로 오름차순으로 출력
# 회고 :

# My_Solution
def DFS(l):
    global cnt
    if l == n:
        for i in ch:
            print(i, end=" ")
            cnt += 1
        print()

    else:
        for i in range(n):
            ch[l] = i
            if l == 1:
                if ch[l - 1] == ch[l]:
                    continue
            else:
                DFS(l + 1, )


if __name__ == "__main__":
    n, n = map(int, input().split())
    ch = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)