# 1. 재귀함수를 이용한 이진수 출력
# 문제 : 입력된 10진수 N을 2진수로 변환하여 출력. 단, 재귀함수를 이용해서 출력
# 조건 : 첫 번째 줄에 10진수 N(1 <= N <= 1,000)이 주어짐
# 회고 : 재귀함수의 종료 조건과 출력되는 순서를 잘 파악함
#        몫이 1일 때의 2로 나눈 나머지가 끝인데, 몫이 0인 경우와 헷갈림

# My_Solution
def DFS(x):  # 11
    if x > 0:
        DFS(x // 2)  # 5, 2, 1, 0
        print(x % 2, end="")  # 1, 0, 1, 1


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# Solution_2 -> if ~ else문 사용
def DFS(x):
    if x == 0:  # x가 0일 경우 무한 반복을 종료
        return
    else:
        DFS(x // 2)
        print(x % 2, end="")  # 거꾸로 출력


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# test_case1
# n = 11
# result : 1011

# test_case2
# n = 120
# result : 1111000

# test_case3
# n = 360
# result : 101101000
