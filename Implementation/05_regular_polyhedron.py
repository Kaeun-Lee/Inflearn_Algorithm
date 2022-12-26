# 5. 정다면체
# 문제 : 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
#        가장 확률이 높은 숫자를 출력. '정답이 여러 개일 경우 오름차순'으로 출력
# 조건 : 첫 번째 줄에는 자연수 N과 M이 주어짐. N과 M은 4, 6, 8, 12, 20 중 하나임
# 회고 : 리스트에서 조합을 찾는 itertools의 product를 사용함. 이중 for문으로도 간단하게 해결 가능함

# My_Solution -> 두 개 이상의 리스트에서 모든 조합 구하기
from itertools import product

n, m = map(int, input().split())
a = range(1, n + 1)
b = range(1, m + 1)
tmp = list(product(a, b))
dict = {}

for i in tmp:
    if sum(i) not in dict:
        dict[sum(i)] = 1
    else:
        dict[sum(i)] += 1

max_ = max(dict.values())
for i in dict:
    if dict[i] == max_:
        print(i, end=" ")


# Solution_2 -> 이중 for문을 이용한 풀이
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)  # 넉넉하게 만들기 위해 +3을 해줌
max = -2147000000

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

# 눈의 합 빈도 횟수 중 최댓값 찾기
for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

# 답 출력
for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=" ")


# test case 1
# n, m = 4 6
# result : 5 6 7

# test case 2
# n, m = 8 8
# result : 9

# test case 1
# n, m = 12 20
# result : 13 14 15 16 17 18 19 20 21
