# 13. 라이브러리를 이용한 조합(수들의 조합)

# My_Solution
from itertools import combinations

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

for tmp in combinations(a, k):
    if sum(tmp) % m == 0:
        cnt += 1
print(cnt)


# test_case 1
# n, m = 5 3
# nums = 2 4 5 8 12
# k = 6
# result : 2

# test_case 2
# n, m = 7 3
# nums = 2 4 5 8 12 7 13
# k = 6
# result : 5

# test_case 3
# n, m = 10 3
# nums = 2 4 5 8 12 7 13 3 6 16
# k = 3
# result : 42
