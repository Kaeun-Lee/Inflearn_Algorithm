# 문제 : 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
#        가장 확률이 높은 숫자를 출력. '정답이 여러 개일 경우 오름차순'으로 출력
# 조건 : 첫 번째 줄에는 자연수 N과 M이 주어짐. N과 M은 4, 6, 8, 12, 20 중 하나임
# 회고 : 리스트에서 조합을 찾는 itertools의 product를 사용함. Counter와 이중 for문으로도 간단하게 해결 가능함
#        list의 index를 주사위 두 눈의 합으로 활용하는 방법 알아두기

# My Solution 1 -> (정답) 두 개 이상의 리스트에서 모든 조합 구하기
import sys
from itertools import product

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
a = range(1, n + 1)
b = range(1, m + 1)
tmp = list(product(a, b))
dict_ = {}

for i in tmp:
    if sum(i) not in dict_:
        dict_[sum(i)] = 1
    else:
        dict_[sum(i)] += 1

max_ = max(dict_.values())
for i in dict_:
    if dict_[i] == max_:
        print(i, end=" ")


# My Solucion 2 -> (정답)
import sys
from collections import Counter

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
counter = Counter([i + j for i in range(1, n + 1) for j in range(1, m + 1)])
# counter = Counter([i + j for i, j in itertools.product(range(1, n + 1), range(1, m + 1))])
result = sorted([num for num, freq in counter.items() if freq == max(counter.values())])

for r in result:
    print(r, end=" ")


# Lecture Solution -> 이중 for문을 이용한 풀이
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)  # cnt의 index는 주사위 두 눈의 합, value는 빈도수를 저장 ("+3"은 여유 공간)

# 가능한 주사위 눈 조합의 빈도수 구하기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

# 최대 빈도수 찾기
max_ = -2147000000
for i in range(n + m + 1):
    if cnt[i] > max:
        max_ = cnt[i]

# 최대 빈도수를 갖는 index 찾기
for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=" ")  # 옆으로 이어붙여서 출력


# Test Case 1
# input : 4 6
# output : 5 6 7

# Test Case 2
# input : 8 8
# output : 9

# Test Case 3
# input :  12 20
# output : 13 14 15 16 17 18 19 20 21
