# 0. [선수지식] 재귀함수와 스택

# 재귀함수 : 자기 자신을 호출하는 함수. 재귀 함수는 스택 자료구조를 사용해 작동하며, 반복문의 효과를 냄
#            코드 유연성이 떨어지는 for문, while문, 중첩 for문(3중, 4중 for문) 문제들의 경우,
#            재귀함수를 이용하면 유연성 있는 코드를 작성할 수 있고 쉽게 해결할 수 있음
# main script : script가 실행되면 __main__을 찾은 뒤 해당 코드부터 실행됨


# 문제 1 : n이 입력되면 1부터 n까지 출력되는 재귀함수

# My_Solution -> 불필요한 변수를 생성함
def recursive_function(start, x):
    if start <= x:
        print(start)
        recursive_function(start + 1, x)


if __name__ == "__main__":  # main script
    n = int(input())
    recursive_function(1, n)


# Solution_2
def DFS(x):
    if x > 0:  # 무한 루프를 피하기 위한 종료 조건
        DFS(x - 1)
        print(x, end=" ")


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# 문제 2 : n이 입력되면 n부터 1까지 출력되는 재귀함수

# Solution_1
def DFS(x):
    if x > 0:
        print(x)
        DFS(x - 1)


if __name__ == "__main__":
    n = int(input())
    DFS(n)
