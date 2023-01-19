# 12. 라이브러리를 이용한 순열(수열 추측하기)

# 라이브러리에 너무 의존하면 라이브러리 사용을 막아놨을 때 문제를 풀지 못하는 경우가 발생함
# 어떤 조건을 만족하는 원소만 뽑아서 순열이나 조합을 만드는 경우에도 라이브러리 사용이 힘듦
# 가장 우선 되어야 하는 건 DFS(재귀 함수)로 순열과 조합을 만들어내는 것

# Solution_1
from itertools import permutations

n, f = map(int, input().split())
a = range(1, n + 1)
b = [1] * n

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i

for tmp in permutations(a):  # 모든 순열 중 하나씩 가져옴
    sum_ = 0
    for l, x in enumerate(tmp):  # 0 1, 1 2, 2 3, 3 4
        sum_ += x * b[l]  # 원소 * 이항계수
    if sum_ == f:
        for x in tmp:
            print(x, end=" ")
        break  # 맨 처음 나온 for문을 멈춤


# test_case 1
# n, f = 4 16
# result : 3 1 2 4

# test_case 2
# n, f = 5 39
# result : 4 1 3 2 5

# test_case 3
# n, f = 9 1610
# result : 1 2 3 5 9 6 8 4 7
