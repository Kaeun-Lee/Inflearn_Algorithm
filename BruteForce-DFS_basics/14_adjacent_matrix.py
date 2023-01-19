# 14. 인접 행렬(가중치 방향 그래프)
# 문제 : 아래와 같은 그래프 정보를 인접 행렬로 출력
# 조건 : 첫째 줄에 정점의 수 N(2 <= N <= 29)와 간선의 수 M이 주어짐
#        그다음부터 M줄에 걸쳐 연결정보와 거리 비용이 주어짐
# 회고 : 인접 행렬을 출력할 때 이중 for문을 사용하면 된다는 것을 생각하지 못함
#        그래프를 초기화할 때는 0 ~ n + 1 크기로 만든 뒤 출력할 때 1 ~ n만 하면 됨

# 그래프: 노드와 간선(노드와 노드를 연결하는 선)의 집합
# 방향 그래프 : 간선에 방향이 설정되어 있는 그래프
# 가중치 방향 그래프 : 방향 그래프의 간선에 값이 설정되어 있는 그래프
# 그래프를 프로그래밍 하려면 자료구조에 표현을 해야 함
# 인접 행렬은 항상 '행 번호에서 -> 열 번호'로 이동함


# <무방향 그래프>를 인접 행렬로 표현
# 무방향 : g[a][b] =1 이면 g[b][a] = 1도 가능하다는 의미
n, m = map(int, input().split())  # n : 노드 수, m : 간선의 수
g = [[0] * (n + 1) for _ in range(n + 1)]  # g : 그래프, 2차원 리스트 인접 행렬

for i in range(m):
    a, b = map(int, input().split())  # 간선 정보를 하나씩 가져옴
    g[a][b] = 1  # a -> b로 갈 수 있음을 표시
    g[b][a] = 1  # b -> a로 갈 수 있음을 표시

for i in range(1, n + 1):  # 1 ~ n번 idx를 출력
    for j in range(1, n + 1):
        print(g[i][j], end=" ")
    print()


# test_case 1
# n, m = 5 5
# info = 1 2
#        1 3
#        2 4
#        3 4
#        4 5
# result : 0 1 1 0 0
#          1 0 0 1 0
#          1 0 0 1 0
#          0 1 1 0 1
#          0 0 0 1 0


# <가중치 방향 그래프>를 인접 행렬로 표현
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
g = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())  # 간선 정보
    g[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=" ")
    print()


# test_case 1
# n, m = 6 9
# info = 1 2 7
#        1 3 4
#        2 1 2
#        2 3 5
#        2 5 5
#        3 4 5
#        4 2 2
#        4 5 5
#        6 4 5
# result : 0 7 4 0 0 0
#          2 0 5 0 5 0
#          0 0 0 5 0 0
#          0 2 0 0 5 0
#          0 0 0 0 0 0
#          0 0 0 5 0 0
