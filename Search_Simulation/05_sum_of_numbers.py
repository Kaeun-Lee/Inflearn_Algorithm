# 5. 수들의 합
# 문제 : N개의 수로 된 수열 A[1], A[2], ..., A[N]이 있음
#       이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가
#       M이 되는 경우의 수를 출력
# 조건 : 첫 줄에 N(1 <= N <= 10,000), M(1 <= M <= 300,000,000)이 주어짐
#        다음 줄에 A[1], A[2], ..., A[N]이 공백으로 분리되어 주어짐
#        각각의 A[x]는 30,000을 넘지 않는 자연수임
# 회고 : 슬라이싱 하는 것도 중요하지만, 하나의 숫자가 단독으로도  m과 같을 경우도 고려해야 함
#        들어오는 수열의 길이, 각 수들의 크기가 큼
#        전체 수열에서의 연속적인 부분 수열의 합의 m과 같은 경우가 몇 번 있는지
#        lt와 rt가 같을 수는 있어도 lt가 rt를 넘어갈 수는 없음


# My_Solution
import sys

# sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
nums = list(map(int, input().split()))
p1 = 0
p2 = 1
cnt = 0

while p1 <= n and p2 <= n:  # pointer가 수열 개수보다 커지면 종료. 슬라이싱을 하기 때문에 <= n으로 지정함
    tmp = sum(nums[p1 : p2 + 1])  # 수열의 합 구하기
    if tmp >= m:  # 수열의 합이 m보다 크거나 같은 경우, 더 적은 수들을 더해야 함
        if tmp == m:
            cnt += 1
        p1 += 1
    else:  # 수열의 합이 m보다 작은 경우 더 많은 숫자를 더해야 함
        p2 += 1
print(cnt)


# test_case 1
# n, m = 8 3
# nums = 1 2 1 3 1 1 1 2
# result : 5

# test_case 2
# n, m = 10 5
# nums = 3 2 2 1 3 1 2 3 2 2
# result : 5
