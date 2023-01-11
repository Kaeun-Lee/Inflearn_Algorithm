# 4. 합이 같은 부분집합(DFS : 아마존 인터뷰)
# 문제 : N개의 원소로 구성된 자연수 집합을 두 개의 부분집합으로 나누었을 때
#       두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 "YES", 그렇지 않으면 "NO" 출력
#       둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 됨
#       ex. {1, 3, 5, 6, 7, 10} -> {1, 3, 5, 7} = {6, 10}
# 조건 : 첫 번째 줄에 자연수 N(1 <= N <= 10)이 주어짐
#        두 번째 줄에 집합의 원소 N개가 주어짐. 각 원소는 중복되지 않음
# 회고 : 1로 시작하는 v와 nums의 idx 범위가 헷갈려서, 디버깅 해보기 전까진 값을 잘못 가져옴
#        global 키워드로 전역변수 yes를 명시해 줘야함
#        N개의 원소가 1씩 커지는 게 아니라 랜덤으로 주어지는 경우이며, 예시에서는 2^6의 경우의 수가 생김. 즉, 64가지(공집합 빼면 63가지)
#        DFS에서 sys.exit(0)으로 아예 프로그램을 종료시킬 수 있다는 걸 몰랐음

# My_solution -> (성공)
def DFS(v, nums):
    global yes
    if v == (n + 1):
        zero = 0
        one = 0
        for i in range(1, n + 1):  # 0으로 표시된 것과 1로 표시된 것들을 각각 더해줌
            if ch[i] == 0:
                zero += nums[i - 1]  # 입력으로 받은 자연수 집합은 idx가 0부터 시작
            else:
                one += nums[i - 1]
        if zero == one:  # 두 부분집합의 원소의 합이 같을 경우 표시
            yes += 1
    else:
        ch[v] = 1
        DFS(v + 1, nums)
        ch[v] = 0
        DFS(v + 1, nums)


if __name__ == "__main__":
    n = int(input())
    nums_set = list(map(int, input().split()))
    ch = [0] * (n + 1)
    yes = 0
    DFS(1, nums_set)

    if yes >= 1:
        print("YES")
    else:
        print("NO")


# Solution_2
import sys


def DFS(l, sum):  # l : a라는 list를 참조하는 idx(level), sum : 내가 만들고 있는 부분집합의 합
    if l == n:  # l은 0부터 시작
        if sum == (total - sum):  # (total - sum) : 선택되지 않은 원소들의 부분집합의 합
            print("YES")
            sys.exit(0)  # 함수가 아니라 아예 프로그램을 종료
    else:
        DFS(l + 1, sum + a[l])  # 왼쪽
        DFS(l + 1, sum)  # 오른쪽


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)  # 원소의 총합
    DFS(0, 0)
    print("NO")


# Solution_3 -> cut edge를 추가하여 시간 복잡도를 줄임
import sys


def DFS(l, sum):
    if l == n:
        if sum > (total // 2):  # total이 홀수일 수 있으므로 ==가 아닌 >를 사용
            return  # sum이 total // 2를 넘어가면, 그 밑으로 내려갈 필요가 없음
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(l + 1, sum + a[l])
        DFS(l + 1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")


# test_case 1
# n = 6
# nums = 1 3 5 6 7 10
# result : YES

# test_case 2
# n = 7
# nums = 1 2 3 4 5 6 7
# result : YES

# test_case 3
# n = 9
# nums = 3 6 13 11 7 16 34 23 12
# result : NO
