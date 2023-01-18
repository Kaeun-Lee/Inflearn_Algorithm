# 10. 조합 구하기
# 문제 : 1부터 N까지 번호가 적힌 구슬 중 M개를 뽑는 방법의 수를 출력
#        결과를 출력한 뒤 맨 마지막에 총 경우의 수를 출력
# 조건 : 자연수 N(3 <= N <=10)과 M(2 <= M <= N)이 주어짐
#        출력 순서는 사전 순으로 오름차순으로 출력
# 회고 : 크고 작다의 부등호와 if ~ else문의 구조를 헷갈림
#        숫자가 중복되면 안 되는데, '8. 순열 구하기 문제'와 똑같은 실수를 했음
#        순열과 상태 트리가 약간 다름. level이 증가하면, 이전 level 값 보다 +1 큰 숫자부터 for문을 수행해야 함
#        start라는 새로운 변수가 필요하고, i + 1로 range의 시작 값을 조정하는 방법을 생각하지 못함
#        for i in range(5, 4)라면 for문을 수행하지 않고 종료함

# My_Solution_1 -> (실패) m이 3이상인 경우, l == 0이었을 때 쓰인 숫자들이 다시 중복돼서 나올 수 있음
def DFS(l):
    global cnt
    if l == m:
        for i in res:
            print(i, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if l == 1 and res[0] >= i:
                continue
            else:
                res[l] = i
                DFS(l + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)


# My_Solution_2 -> (성공) level과 start 매개 변수 사용
def DFS(l, s):  # start : 가지를 뻗는 첫 번째 숫자
    global cnt
    if l == m:
        for j in res:
            print(j, end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):  # s부터 for문을 수행
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                DFS(l + 1, i + 1)  # 가지를 뻗을 때, 현재 i값 + 1을 해서 자신보다 큰 수부터 range 되도록 함
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0, 1)
    print(cnt)


# Solution_3 -> check list 없이 수행
def DFS(l, s):
    global cnt
    if l == m:
        for j in range(l):
            print(res[j], end=" ")
        cnt += 1
        print()
    else:
        for i in range(s, n + 1):
            res[l] = i
            DFS(l + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (m + 1)
    cnt = 0
    DFS(0, 1)
    print(cnt)


# test_case 1
# n, m = 3 2
# result : 1 2
#          1 3
#          2 3
#          3

# test_case 2
# n, m = 5 3
# result : 1 2 3
#          1 2 4
#          1 2 5
#          1 3 4
#          1 3 5
#          1 4 5
#          2 3 4
#          2 3 5
#          2 4 5
#          3 4 5
#          10
