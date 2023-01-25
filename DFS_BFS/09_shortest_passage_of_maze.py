# 9. 미로의 최단거리 통로(BFS)
# 문제 : 7*7 격자판 미로를 탈출하는 최단 경로의 경로 수를 출력
#        경로 수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미함
#        출발점은 격자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7) 좌표임
#        격자판의 1은 벽이고, 0은 도로임. 격자판은 상하좌우로만 움직임
#        첫 줄에 최단으로 움직인 칸의 수를 출력. 도착할 수 없다면 -1을 출력
# 회고 : 방문한 기록과 최단 경로를 미로 변수에 표시하는 것인지, 거리 변수에 표시하는 것인지 잘 구분하지 못함
#        방문한 곳은 maze 변수에 1로 체크해야 하고, 최단 경로는 dis 변수에 따로 저장해야 함
#        벽에 가로막혀 도착점에 가지 못하는 경우는 dis[6][6] = 0인 것으로 예외 처리할 수 있음
#        최단 경로 기록 시 출발점은 0으로 두어야 이동하면서 경로를 +1씩 셀 수 있음

# Solution_1
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

maze = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
queue.append((0, 0))
maze[0][0] = 1  # 방문한 곳은 1로 체크. dis가 아닌 maze에 체크해야 함

while queue:  # queue가 빌 때까지 반복
    tmp = queue.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and maze[x][y] == 0:
            maze[x][y] = 1  # 방문한 곳은 1로 체크
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            queue.append((x, y))
if dis[6][6] == 0:  # 벽에 가로막혀서 도착점에 가지 못한 경우
    print(-1)
else:
    print(dis[6][6])


# test_case 1
# maze = 0 0 0 0 0 0 0
#        0 1 1 1 1 1 0
#        0 0 0 1 0 0 0
#        1 1 0 1 0 1 1
#        1 1 0 1 0 0 0
#        1 0 0 0 1 0 0
#        1 0 1 0 0 0 0
# result : 12

# test_case 2
# maze = 0 0 0 0 0 0 0
#        0 1 1 1 1 1 0
#        0 0 0 1 0 0 0
#        1 1 0 1 0 1 1
#        1 1 0 0 0 0 1
#        1 1 0 1 1 1 0
#        1 0 0 0 0 0 0
# result : 12

# test_case 3
# maze = 0 0 0 0 0 0 0
#        0 1 1 0 1 1 0
#        0 0 0 1 0 1 0
#        1 1 0 1 1 0 1
#        1 1 1 0 1 0 1
#        1 1 1 0 1 0 0
#        1 0 1 0 0 0 0
# result : -1
