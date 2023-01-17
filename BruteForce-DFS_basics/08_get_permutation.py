# 8. 순열 구하기
# 문제 : 1부터 N까지 번호가 적힌 구슬 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력
#        결과를 출력한 뒤 맨 마지막에 총 경우의 수를 출력
# 조건 : 자연수 N(3 <= N <=10)과 M(2 <= M <= N)이 주어짐. 출력 순서는 사전 순으로 오름차순으로 출력
# 회고 : 자기 자신과 같은 수가 나오는 경우를 제외하는 조건 걸어줬으나, m이 2일 때만 가능함
#        check list를 만들어 사용한 숫자는 1로 check한 뒤, DFS 호출이 끝나면 다시 0으로 바꿔주는 방법을 생각하지 못함
#        DFS(l + 1)의 위쪽과 아래쪽은 대칭 구조임
#        상태 트리 자체는 중복 순열 구하기와 똑같은 원리로 작동함

# My_Solution -> (실패) m이 3이상인 경우, l == 0이었을 때 쓰인 숫자들이 다시 중복돼서 나올 수 있음
def DFS(l):
    global cnt
    if l == m:
        for i in ch:
            print(i, end=" ")
        cnt += 1
        print()

    else:
        for i in range(1, n + 1):
            ch[l] = i
            if l == 1:
                if ch[l - 1] == ch[l]:
                    continue
            DFS(l + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)


# Solution_1 -> 중복되지 않도록 check list를 만들고, 0이 아니면 가지를 뻗지 않도록 cut
def DFS(l):
    global cnt
    if l == m:
        for j in res:
            print(j, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:  # 이미 사용된 i는 사용하지 않음
                ch[i] = 1  # 작업
                res[l] = i  # 작업
                DFS(l + 1)  # 호출
                ch[i] = 0  # 다시 되돌아오면 작업 취소. 사용한 i를 다시 0으로 되돌림


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n + 1)  # check list
    cnt = 0
    DFS(0)
    print(cnt)


# test_case 1
# n, m = 3 2
# result : 1 2
#          1 3
#          2 1
#          2 3
#          3 1
#          3 2
#          9

# test_case 2
# n, m = 5 3
# result : 1 2 3
#          1 2 4
#          1 2 5
#          1 3 2
#          1 3 4
#          1 3 5
#          1 4 2
#          1 4 3
#          1 4 5
#          1 5 2
#          1 5 3
#          1 5 4
#          2 1 3
#          2 1 4
#          2 1 5
#          2 3 1
#          2 3 4
#          2 3 5
#          2 4 1
#          2 4 3
#          2 4 5
#          2 5 1
#          2 5 3
#          2 5 4
#          3 1 2
#          3 1 4
#          3 1 5
#          3 2 1
#          3 2 4
#          3 2 5
#          3 4 1
#          3 4 2
#          3 4 5
#          3 5 1
#          3 5 2
#          3 5 4
#          4 1 2
#          4 1 3
#          4 1 5
#          4 2 1
#          4 2 3
#          4 2 5
#          4 3 1
#          4 3 2
#          4 3 5
#          4 5 1
#          4 5 2
#          4 5 3
#          5 1 2
#          5 1 3
#          5 1 4
#          5 2 1
#          5 2 3
#          5 2 4
#          5 3 1
#          5 3 2
#          5 3 4
#          5 4 1
#          5 4 2
#          5 4 3
#          60