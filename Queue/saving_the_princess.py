# 공주 구하기
# 문제 : 왕자 N명과 특정 숫자 K가 주어질 때 공주를 구하러 갈 왕자의 번호를 출력
# 조건 : 1부터 시작하여 K를 외친 왕자는 제외되고, 다음 왕자부터 다시 1부터 시작하여 번호를 외침
#        N(5 <= N <= 1,000), K(2 <= K <= 9)

# Solution_1
from collections import deque
def solution(n, k):
    dq = deque([i for i in range(1, n + 1)])
    while len(dq) > 1:
        for _ in range(k - 1): # 0, 1
            left = dq.popleft()
            dq.append(left)
        dq.popleft()
    return dq[0]


# Solution_2
from collections import deque
def solution(n, k):
    dq = deque(list(range(1, n + 1)))
    while dq:
        for _ in range(k - 1):
            cur = dq.popleft()
            dq.append(cur)
        dq.popleft()
        if len(dq) == 1:
            return dq[0]
 

# test case
print(solution(8, 3))     # 7
print(solution(20, 3))    # 20
print(solution(1000, 9))  # 329