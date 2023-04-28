# 문제 : 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있음
#        규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받음
#        규칙(2) 같은 눈이 2개만 나오는 경우 1,000원+(같은 눈)*100원의 상금을 받음
#        규칙(3) 모두 다른 눈이 나오는 경우 (그중 가장 큰 눈)*100원의 상금을 받게 됨
#        예를 들어, 3개의 눈 3, 3, 6 -> 상금 : 1,000+3*100 = 1,300원
#                  3개의 눈 2, 2, 2 -> 상금 : 10,000+2*1,000 = 12,000원
#                  3개의 눈 6, 2, 5 -> 상금 : 6*100 = 600원
#         N명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력
# 조건 : 첫 줄에 참여하는 사람 수 N(2 <= N <= 1,000)이 주어짐
#        그다음 줄부터 N개의 줄에, 주사위를 던져서 나온 3개의 눈이 빈칸을 사이에 두고 각각 주어짐
# 회고 : 6 3 3과 3 3 6, 3 6 3의 경우, 같은 눈이 2개인데 형태가 다르니 주의해야 함
#        맨 앞에 있는 눈의 개수만 확인할 경우, 6의 개수는 1이 되어서 모두 다른 눈이 나오는 경우로 계산될 수 있음
#        Solution_3에서는 sort()를 했기 때문에 사실상 a == c인 경우를 제거해도 무관함

# My Solution 1 -> (정답) 눈의 개수가 1이라면 나머지 2개 눈의 개수를 확인
import sys

sys.stdin = open("input.txt", "r")


def win_cashprize(x):
    for i in x:
        cnt = x.count(i)
        if cnt == 3:
            return 10000 + (i * 1000)
        elif cnt == 2:
            return 1000 + (i * 100)
    return max(x) * 100  # 모두 다른 눈이 나오는 경우


n = int(input())
dics = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in dics:  # 3 3 6
    result.append(win_cashprize(i))
print(max(result))


# My Solution 2 -> (정답) Counter 활용
import sys
from collections import Counter

sys.stdin = open("input.txt", "r")
n = int(input())

result = []
for i in range(n):
    counter = Counter(list(map(int, input().split())))
    most_cnt = counter.most_common(1)[0][1]
    if most_cnt == 3:
        num = counter.most_common()[0][0]
        result.append(10000 + (num) * 1000)
    elif most_cnt == 2:
        num = counter.most_common()[0][0]
        result.append(1000 + (num) * 100)
    else:
        num = max(counter.keys())
        result.append((num) * 100)
print(max(result))


# Lecture Solution -> if ~ elif ~ else문을 활용해 for문을 한 번만 사용함
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
res = 0

for i in range(n):
    tmp = input().split()  # ['3', '3', '6']
    tmp.sort()  # 눈이 모두 다를 경우, 가장 큰 숫자를 찾아야 함
    a, b, c = map(int, tmp)
    # if문을 쓸 때, 가장 좋은 조건을 우선적으로 작성 (최대 상금을 출력하라고 했기 때문)
    if a == b and b == c:  # 조건 (1) a, b, c가 모두 같은 경우
        money = 10000 + (a * 1000)
    elif a == b or a == c:  # 조건 (2) 눈 a로 계산. 3 3 6 or 3 6 3
        money = 1000 + (a * 100)
    elif b == c:  # 조건 (2) 눈 b로 계산. 6 3 3
        money = 1000 + (b * 100)
    else:  # 조건 (3)
        money = c * 100
    if money > res:
        res = money
print(res)


# Another Solution -> set 활용
from collections import Counter

sys.stdin = open("input.txt", "r")
n = int(input())
total = [list(map(int, input().split())) for _ in range(n)]
prize = [0] * n

for i in range(n):
    k = set(total[i])
    if len(k) == 1:  # 규칙(1)
        prize[i] = 10000 + (max(k) * 1000)
    elif len(k) == 2:  # 규칙(2)
        freq = Counter(total[i]).items()
        freq = sorted(freq, key=lambda x: x[1], reverse=True)
        prize[i] = 1000 + (freq[0][0] * 100)
    else:  # 규칙(3)
        prize[i] = max(k) * 100

print(max(prize))


# Test Case 1
# < input >
# 3
# 3 3 6
# 2 2 2
# 6 2 5

# output : 12000

# Test Case 2
# < input >
# 3
# 3 3 6
# 6 3 3
# 6 2 5

# output : 1300

# Test Case 3
# < input >
# 3
# 1 1 1
# 2 3 5
# 4 5 5

# output : 11000
