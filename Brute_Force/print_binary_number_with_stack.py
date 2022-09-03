# 재귀함수를 이용한 이진수 출력
# 문제 : 입력된 10진수 N을 2진수로 변환하여 출력. 단, 재귀함수를 이용해서 출력
# 조건 : 첫 번째 줄에 10진수 N(1 <= N <= 1,000)이 주어짐

# Solution
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end='')


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# test_case1
# n = 11
# return : 1011

# test_case2
# n = 23
# return : 10111

# test_case3
# n = 360
# return : 101101000