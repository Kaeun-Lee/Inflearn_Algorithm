# 3. 부분집합 구하기(DFS)
# 문제 : 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력
#        단, 공집합은 출력하지 않음
# 조건 : 첫 번째 줄에 10진수 N(1 <= N <= 10)이 주어짐
#        첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래 출력 예제와 같은 순서로 출력(깊이우선탐색 전위 순회 방식으로 출력)
# 회고 : 숫자 1, 2, 3이 이진 트리의 값이 되는 것이 아니라, 숫자의 '사용 유무'로 이진 트리(상태 트리)를 구성한다는 것을 생각하지 못함
#        n이 3일 때, 각 원소의 사용 유무에 따라 경우의 수는 8가지가 됨(2 x 2 x 2)
#        이때, 공집합(모든 원소를 사용하지 않는 경우)을 포함하기 때문에 이를 제거해야 함
#        DFS(n + 1)이 되었을 때, 1 ~ n까지의 원소 사용 유무(부분집합)를 출력해야 함
#        *DFS 문제는 상태 트리를 잘 구성하고 그 상태 트리에 의해 재귀 함수를 호출하면 됨

# Solution_1
def DFS(v):  # 매개변수. 원소 값(노드 값)
    if v == n + 1:  # 종착점. n + 1에 도달하면 idx 출력
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=" ")  # 부분집합 출력
        print()  # 줄바꿈
    else:
        check[v] = 1  # v를 사용함(해당 원소를 부분집합으로 사용)
        DFS(v + 1)
        check[v] = 0  # v를 사용하지 않음
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n + 1)  # 원소 사용 유무를 체크하기 위한 변수. 넉넉하게 1개 더 만들어줌
    DFS(1)


# test_case 1
# n = 3
# result : 1 2 3
#          1 2
#          1 3
#          1
#          2 3
#          2
#          3

# test_case 2
# n = 5
# result : 1 2 3 4 5
#          1 2 3 4
#          1 2 3 5
#          1 2 3
#          1 2 4 5
#          1 2 4
#          1 2 5
#          1 2
#          1 3 4 5
#          1 3 4
#          1 3 5
#          1 3
#          1 4 5
#          1 4
#          1 5
#          1
#          2 3 4 5
#          2 3 4
#          2 3 5
#          2 3
#          2 4 5
#          2 4
#          2 5
#          2
#          3 4 5
#          3 4
#          3 5
#          3
#          4 5
#          4
#          5
