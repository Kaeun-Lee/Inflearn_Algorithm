# 15. 경로 탐색(그래프 DFS)
# 문제 : 주어진 방향 그래프의 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력
#        아래 그래프에서 1번 정점에서 5번 정점으로 가는 가지 수는 총 6가지임
#        그래프에서 방문한 노드는 중복해서 방문하지 않음
# 조건 : 정점의 수 N(2 <= N <= 20)과 간선의 수 M이 주어짐
#        그다음부터 M줄에 걸쳐 연결 정보가 주어짐
# 회고 : graph에 정보를 담고, 노드의 수만큼 생성한 check list에 노드의 사용 여부를 체크하는 방법을 생각하지 못함
#        1 ~ n + 1까지 for문을 수행하는 상태 트리를 생각하지 못해 dfs 작동 순서를 생각하지 못함
#        방문한 노드를 check하지 않으면, 무한 반복에 빠짐

# My_Solution_1 -> (성공) for문 수행 전 방문한 노드를 check
import sys

sys.stdin = open("input.txt")


def DFS(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        ch[v] = 1
        for i in range(1, n + 1):
            if (ch[i] == 0) and (g[v][i] == 1):
                DFS(i)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for i in range(n + 1)]
    ch = [0] * (n + 1)
    cnt = 0

    for i in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1

    DFS(1)
    print(cnt)


# Solution_2 -> 첫 번째 노드를 미리 check하고 시작
def DFS(v):  # v : vertex, 노드 번호
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:  # 갈 수 있는 노드를 확인
                ch[i] = 1  # i번 노드 방문
                DFS(i)
                ch[i] = 0  # 방문 후 다시 0으로 돌려줌


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    cnt = 0

    for i in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1  # 방향 그래프

    ch[1] = 1  # 1번 노드 방문
    DFS(1)
    print(cnt)


# 경로를 확인하는 코드
def DFS(v):  # v : vertex, 노드 번호
    global cnt
    if v == n:
        cnt += 1
        for x in path:  # 경로 출력
            print(x, end=" ")
        print()
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:  # 갈 수 있는 노드를 확인
                ch[i] = 1  # i번 노드 방문
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0  # 방문 후 다시 0으로 돌려줌


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    cnt = 0
    path = []

    for i in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1  # 방향 그래프

    ch[1] = 1  # 1번 노드 방문
    path.append(1)
    DFS(1)
    print(cnt)


# test_case 1
# n, m = 5 9
# info = 1 2
#        1 3
#        1 4
#        2 1
#        2 3
#        2 5
#        3 4
#        4 2
#        4 5
# result : 6

# test_case 2
# n, m = 7 8
# info = 1 2
#        2 3
#        3 4
#        4 5
#        5 6
#        6 7
#        2 4
#        3 5
# result : 6

# test_case 3
# n, m = 10 17
# info = 1 2
#        3 4
#        2 5
#        2 3
#        5 6
#        6 7
#        3 7
#        1 7
#        1 8
#        1 9
#        1 10
#        7 3
#        2 8
#        2 9
#        9 10
#        1 3
#        3 2
# result : 5
