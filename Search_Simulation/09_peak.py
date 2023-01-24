# 9. 봉우리
# 문제 : 지도 정보가 N*N 격자판에 주어지고, 각 격자에는 그 지역의 높이가 쓰여있음
#        각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역임
#        봉우리의 개수를 출력. 격자의 가장자리는 0으로 초기화되었다고 가정함
# 조건 : 첫 줄에 자연수 N이 주어짐(1 <= N <= 50)
#        두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어짐. 각 자연수는 100을 넘지 않음
# 회고 : insert와 append 함수를 사용해서 가장자리에 0값을 넣어줄 수 있음
#        모든 격자판(가장자리 포함)을 탐색하는 게 아니라 숫자가 있는 격자판만 탐색하면 됨
#        상하좌우로 움직여도 가장자리에 0값이 있기 때문에 격자판을 벗어나는 경우가 없으니 좌표를 확인하는 코드는 제거 가능
#        all 함수 내에 for문을 사용하여 상하좌우 보다 큰 경우를 한 번에 계산할 수 있음

# insert 함수 : list 형태 data의 원하는 위치에 원하는 값을 추가하는 함수. 위치를 idx 값을 입력하여 list 형태를 재배열 함
#               idx 값을 음수로 입력 시 배열의 끝을 기준으로 추가됨
#               ex. 0번째에 추가
#               numbers = [6, 9, 7]
#               numbers.insert(0, [100, 200])  # [[100, 200], 6, 9, 7]
#               ex, 끝에서 1번째에 추가
#               numbers.insert(-1, 999)  # [[100, 200], 6, 9, 999, 7]
# all 함수 : 그 안에 있는 조건이 모두 참이면 참

# My_Solution -> (성공) 가장자리를 0으로 채운 후 높이 정보 추가
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
g = [[0] * (n + 2) for _ in range(n + 2)]  # 가장자리를 0으로 초기화
h = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

# 격자에 지역 높이 정보 추가
for i in range(n):
    for j in range(n):
        g[i + 1][j + 1] = h[i][j]

# 모든 격자판을 탐색
for i in range(n + 2):
    for j in range(n + 2):
        cnt = 0
        if g[i][j] != 0:  # 격자판의 숫자가 0이 아닌 경우
            for k in range(4):  # 자신의 상하좌우 숫자를 탐색
                x = i + dx[k]
                y = j + dy[k]
                if -1 < x < n + 2 and -1 < y < n + 2:
                    if g[i][j] > g[x][y]:  # 자신이 다른 방향의 숫자보다 크면 +1
                        cnt += 1
            if cnt == 4:  # 상하좌우 숫자보다 모두 크면 봉우리 지역
                result += 1
print(result)


# Solution_2 -> insert, append, all 함수 사용
n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]

# 가장 자리를 0으로 초기화
h.insert(0, [0] * n)  # 0번 행에 0으로 초기화된 n개의 값을 삽입
h.append([0] * n)  # 맨 뒤 행에 0으로 초기화된 n개의 값을 삽입
for i in h:  # 각 행의 0번 idx 자리와 맨 뒤에 0을 삽입
    i.insert(0, 0)
    i.append(0)

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n + 1):  # 가장자리는 0이기 때문에 1부터 수행
    for j in range(1, n + 1):
        if all(h[i][j] > h[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1
print(cnt)


# test_case 1
# n = 5
# height = 5 3 7 2 3
#          3 7 1 6 1
#          7 2 5 3 4
#          4 3 6 4 1
#          8 7 3 5 2
# result : 10

# test_case 2
# n = 7
# height = 27 33 80 73 19 23 15
#          48 84 61 3 36 9 62
#          87 57 3 14 69 17 22
#          17 57 86 21 85 51 82
#          7 94 66 21 19 41 82
#          27 5 59 28 26 77 64
#          5 46 4 63 76 99 8
# result : 11
