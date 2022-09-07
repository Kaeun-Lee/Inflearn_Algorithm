# 합이 같은 부분집합 (아마존 인터뷰)
# 문제 : N개의 원소로 구성된 자연수 집합을 두 개의 부분집합으로 나누었을 때
#       두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 "YES", 그렇지 않으면 "NO" 출력
# 조건 : 두 부분집합은 서로소 집합임. ex. {1, 3, 5, 7} = {6, 10}
#       집합의 원소 N개(1 <= N <= 10), 각 원소는 중복되지 않음

# Solution_1
import sys
def DFS(L, sum):  # L : a라는 list를 참조하는 idx
    if L == n:  
        if sum == (total - sum):  # (total - sum) : 선택되지 않은 원소들의 부분집합의 합
            print('YES')
            sys.exit(0)  # 함수가 아니라 프로그램을 종료
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)
    

# Solution_2 -> sum > (total // 2)을 추가하여 시간복잡도 줄임
import sys
def DFS(L, sum):
    if sum > (total // 2):  # total이 홀수일 수 있으므로 == 가 아닌 >를 사용
        return
    if L == n:  
        if sum == (total - sum):  
            print('YES')
            sys.exit(0)  
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)  # 원소의 총합
    DFS(0, 0)
    print('NO')


# test_case1
# number : 6
# elements : 1 3 5 6 7 10
# result : YES

# test_case2
# number : 9
# elements : 3 6 13 11 7 16 34 23 12
# result : NO