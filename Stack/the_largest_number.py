# 가장 큰 수
# 문제 : 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수 만들기

# Solution_1
def solution(n, d):
    n = str(n)  # '5276823'
    tmp = [n[0]]  # ['5']
    cnt = d       # 3
    for i in range(1, len(n)): # 1, 2, 3, 4, 5, 6
        while len(tmp) != 0 and int(tmp[-1]) < int(n[i]):
            if cnt == 0:
                break
            tmp.pop()
            cnt -= 1
        tmp.append(n[i])
    if cnt != 0:
        tmp = tmp[:-cnt]
    return int(''.join(tmp))


# Solution_2
def solution(num, m):
    num = list(map(int, str(num)))
    stack = []
    for x in num:
        while stack and m > 0 and stack[-1] < x:
            stack.pop()
            m -= 1
        stack.append(x)
    if m != 0:
        stack = stack[:-m]
    return ''.join(map(str, stack))


# test case
print(solution(5276823, 3))     # 7823
print(solution(9977252641, 5))  # 99776
print(solution(948096783986983, 5))  # 9983986983


# if __name__ == "__main__":
#     n, d = map(int, input().split())
#     solution(n, d)
