# 8. 사과나무(BFS)
# 문제 : 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자 안에는 한 그루의 사과가 심어져 있음
#        N의 크기는 항상 홀수임. 현수는 격자판 안의 사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고
#        나머지 격자 안의 사과는 새들을 위해서 남겨놓음. 만약 N이 5라면 아래 그림과 같이 진한 부분의 사과를 수학함
#        현수가 수확하는 사과의 총개수를 출력
# 조건 : 첫 줄에 자연수 N(홀수, 3 <= N <= 20)이 주어짐
#        두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어짐. 이 자연수는 각 격자 안에 있는 사과나무에 열린 사과의 개수임
#        각 격자 안 사과의 개수는 100을 넘지 않음
# 회고 : bfs로 해결하는 상태 트리를 떠올리지 못함
#        queue가 빌 때까지 진행하는 게 아니니 while queue가 아닌 while True로 지정한 뒤, 다른 조건들을 이용해 bfs를 진행해야 함
#        level로 종료 포인트를 만들고 queue의 길이를 사용하여 탐색할 범위를 넓혀가는 방법을 생각하지 못함

# Solution_1
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0

queue = deque()
ch[n // 2][n // 2] = 1  # 방문한 곳 체크
sum += g[n // 2][n // 2]  # 방문한 곳 누적
queue.append((n // 2, n // 2))  # queue에 넣어줌
l = 0

while True:
    if l == n // 2:  # level이 2에 도달하면 종료
        break
    size = len(queue)
    for i in range(size):  # queue의 길이만큼 반복
        tmp = queue.popleft()
        for j in range(4):  # 상하좌우 살피기
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:  # 방문하지 않은 경우
                ch[x][y] = 1
                sum += g[x][y]
                queue.append((x, y))
    l += 1
print(sum)


# test_case 1
# n = 5
# grid = 10 13 10 12 15
#        12 39 30 23 11
#        11 25 50 53 15
#        19 27 29 37 27
#        19 13 30 13 19
# result : 379

# test_case 2
# n = 7
# grid = 74 10 31 26 59 16 89
#        78 44 49 1 64 33 15
#        9 95 70 18 22 25 40
#        62 77 28 3 78 75 23
#        82 38 20 16 42 1 79
#        1 24 2 25 95 26 79
#        4 35 46 94 70 44 83
# result : 1049
