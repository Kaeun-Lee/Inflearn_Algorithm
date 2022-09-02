# 부분집합 구하기
# 문제 : 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력
# 조건 : 공집합은 출력하지 않음. 자연수 N(1 <= N <= 10)

# Solution
def DFS(v):
    if v == n + 1: # 종료 지점
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=" ")  # 1로 체크된 idx만 출력
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    DFS(1)


# test_case1
# number : 3
# result : 1 2 3
#          1 2
#          1 3    
#          2 3
#          2
#          3

 # test_case2
 # number : 5
 # result : 1 2 3 4 5
#           1 2 3 4
#           1 2 3 5
#           1 2 3
#           1 2 4 5
#           1 2 4
#           1 2 5
#           1 2
#           1 3 4 5
#           1 3 4
#           1 3 5
#           1 3
#           1 4 5
#           1 4
#           1 5