# 6. 격자판 최대합
# 문제 : N*N 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력
# 조건 : 첫 줄에 자연수 N이 주어짐(1 <= N <= 50)
#        두 번째 줄부터 N줄에 걸쳐 N개의 자연수가 주어짐. 각 자연수는 100을 넘지 않음
# 회고 : 각 행, 열, 대각선의 합을 리스트에 담지 않고 바로 largest와 비교해도 됨

# My_Solution
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
row_sums = []
col_sums = []
dia_sums = []

# 각 행, 열의 합
for i in range(n):
    row_sum = col_sum = 0
    for j in range(n):
        row_sum += g[i][j]
        col_sum += g[j][i]
    row_sums.append(row_sum)
    col_sums.append(col_sum)

# 각 대각선의 합
dia_sum1 = dia_sum2 = 0
for i in range(n):
    dia_sum1 += g[i][i]
    dia_sum2 += g[i][n - i - 1]
dia_sums.append(dia_sum1)
dia_sums.append(dia_sum2)

print(max(max(row_sums), max(col_sums), max(dia_sums)))


# Solution_2 -> 행, 열, 대각선의 최대 합을 largest와 비교
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    row_sum = col_sum = 0  # 각 행, 열의 합 초기화
    for j in range(n):
        row_sum += a[i][j]
        col_sum += a[j][i]
    if row_sum > largest:
        largest = row_sum
    if col_sum > largest:
        largest = col_sum

dia_sum1 = dia_sum2 = 0
for i in range(n):
    dia_sum1 += a[i][i]
    dia_sum2 += a[i][n - i - 1]
if dia_sum1 > largest:
    largest = dia_sum1
if dia_sum2 > largest:
    largest = dia_sum2

print(largest)


# test_case 1
# n = 5
# grid = 10 13 10 12 15
#        12 39 30 23 11
#        11 25 50 53 15
#        19 27 29 37 27
#        19 13 30 13 19
# result : 155

# test_case 2
# n = 10
# grid = 75 79 6 72 40 72 28 43 64 19
#        97 71 12 48 64 95 64 40 38 24
#        52 17 58 64 13 37 38 5 30 36
#        43 30 15 8 13 21 81 29 79 33
#        20 4 31 24 93 60 61 19 9 88
#        12 33 30 4 38 62 98 34 65 33
#        37 26 6 60 82 57 49 85 66 67
#        93 4 29 67 65 96 5 27 39 87
#        16 52 8 7 56 19 8 53 52 93
#        87 55 58 84 61 92 3 74 66 34
# result : 614
