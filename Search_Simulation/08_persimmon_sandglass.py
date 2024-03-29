# 8. 곶감(모래시계)
# 문제 : 마당은 N*N 격자판으로 이루어져 있고, 현수는 각 격자단위로 말리는 감의 수를 정함
#        그런데 해의 위치에 따라 특정 위치의 감은 잘 마르지 않음.
#        그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 함
#        만약 회전 명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 회전함
#        첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회전하는 격자의 수임
#        M개의 회전 명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감이 총 몇 개가 있는지 출력
# 조건 : 첫 줄에 자연수 N(3 <= N <= 20)이 주어지며, N은 홀수임
#        두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어짐
#        이 자연수는 각 격자 안에 있는 감의 개수이며, 각 격자 안 감의 개수는 100을 넘지 않음
#        그다음 줄에 회전 명령의 개수인 M(1 <= M <= 10)이 주어지고, 이어서 M개의 회전 명령 정보가 M줄에 걸쳐 주어짐
# 회고 : 모래시계 모양의 영역을 탐색하는 방법은 알았으나 회전하는 방법을 생각하지 못함
#        append, pop, insert로 구현할 수 있는데, idx를 이용해 하나씩 다 바꿔주는 복잡한 방법만 생각함

# Solution_1
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
s = 0
e = n
result = 0

# 회전 처리
for i in range(m):
    row, to, k = map(int, input().split())
    if to == 0:  # 왼쪽으로 회전
        for _ in range(k):
            p[row - 1].append(p[row - 1].pop(0))  # 0번 idx의 원소를 pop해서 행의 마지막에 추가
    else:  # 오른쪽으로 회전
        for _ in range(k):
            p[row - 1].insert(0, p[row - 1].pop())  # 마지막 원소를 pop해서 행의 0번 idx에 추가

# 모래 시계 모양 영역에 있는 곶감 수 세기
for i in range(n):
    for j in range(s, e):
        result += p[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(result)


# test_case 1
# n = 5
# persimmon = 10 13 10 12 15
#             12 39 30 23 11
#             11 25 50 53 15
#             19 27 29 37 27
#             19 13 30 13 19
# m = 3
# rotation = 2 0 3
#            5 1 2
#            3 1 4
# result : 362

# test_case 2
# n = 7
# persimmon = 74 10 31 26 59 16 89
#             78 44 49 1 64 33 15
#             9 95 70 18 22 25 40
#             62 77 28 3 78 75 23
#             82 38 20 16 42 1 79
#             1 24 2 25 95 26 79
#             4 35 46 94 70 44 83
# m = 3
# rotation = 2 0 3
#            5 1 2
#            3 1 4
# result : 1034

# test_case 3
# n = 9
# persimmon = 64 8 59 87 94 71 66 4 9
#             38 21 30 24 33 65 7 79 27
#             99 10 78 74 84 32 33 74 30
#             4 6 69 53 100 15 23 15 88
#             22 88 8 3 62 75 46 4 41
#             39 64 7 75 91 26 83 32 41
#             100 98 20 100 18 39 90 60 56
#             56 30 94 29 81 76 96 50 11
#             66 88 88 95 13 56 29 13 31
# m = 5
# rotation = 1 0 5
#            3 0 6
#            2 1 5
#            6 0 7
#            5 0 8
# result : 2539
