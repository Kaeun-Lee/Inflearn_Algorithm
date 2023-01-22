# 7. 송아지 찾기(BFS : 상태 트리 탐색)
# 문제 : 현수의 위치와 송아지의 위치가 직선상의 좌표 점으로 주어지면, 현수는 현재 위치에서
#        송아지의 위치까지 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있음
#        최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 출력
# 조건 : 현수의 위치 S와 송아지의 위치 E가 주어짐. 직선의 좌표 점은 1부터 10,000까지임
# 회고 : bfs가 어떤 식으로 작동하는지, 기준을 어떻게 잡는지, 점프 횟수를 이전 횟수에 더해서 list에 기록하는 방법을 생각하지 못함
#        반복되는 구간은 다중 if문이 아닌 for문으로 간단하게 해결할 수 있음
#        위치를 계산할 때마다 주어진 좌표의 범주를 넘지 않았는지 확인해야 함
#        BFS Search : 출발점에서 도착점까지의 가장 최단 거리를 찾는 것
#        distance list : 출발점에서 몇 번 만에 도착점에 갈 수 있는지 기록. 출발점의 값은 0이며, idx가 수직선 상의 좌표 지점을 의미
#        check list : 한 번 방문한 곳은 가지 않도록 체크
#        최초로 종료점이 나왔을 때 끝내지 않고 더 진행하면, 멀리 돌아간 값이 덮어씌워짐

# My_Solution -> (성공) 조건을 if문으로 표현해 깔끔하지 않음
import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

s, e = map(int, input().split())
dis = [0] * 10001
ch = [0] * 10001
dis[s] = 0
ch[s] = 1

queue = deque()
queue.append(s)

while queue:
    n = queue.popleft()
    if n == e:
        print(dis[n])
        break
    else:
        if (n + 1) > 0 and (n + 1) <= 10000:
            if ch[n + 1] == 0:
                ch[n + 1] = 1
                dis[n + 1] = dis[n] + 1
                queue.append(n + 1)
        if (n - 1) > 0 and (n - 1) <= 10000:
            if ch[n - 1] == 0:
                ch[n - 1] = 1
                dis[n - 1] = dis[n] + 1
                queue.append(n - 1)
        if (n + 5) > 0 and (n + 5) <= 10000:
            if ch[n + 5] == 0:
                ch[n + 5] = 1
                dis[n + 5] = dis[n] + 1
                queue.append(n + 5)


# Solution_2 -> for문으로 반복되는 구간 설정
import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
s, e = map(int, input().split())
ch[s] = 1  # s 방문 표시
dis[s] = 0  # s에서 출발
queue = deque()
queue.append(s)  # 출발점 추가

while queue:  # queue가 비면 종료
    now = queue.popleft()  # 현재 지점
    if now == e:  # 최초로 도착점에 오면 queue 멈춤
        break
    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX:  # 음수가 아니거나 최댓값을 초과하지 않은 경우
            if ch[next] == 0:  # 방문하지 않은 곳
                queue.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[e])  # 출발점에서 도착점까지의 최소 횟수


# test_case 1
# s, e = 5 14
# result : 3

# test_case 2
# s, e = 7000 3
# result : 6997

# test_case 3
# s, e = 1 21
# result : 4

# test_case 4
# s, e = 3 4356
# result : 873

# test_case 5
# s, e = 7 8945
# result : 1790
