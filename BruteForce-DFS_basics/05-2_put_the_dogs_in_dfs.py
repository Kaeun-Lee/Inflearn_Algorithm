# 5-2. 바둑이 승차(DFS)
# 문제 : 철수는 트럭에 C킬로그램을 넘지 않으면서 바둑이들을 가장 무겁게 태우고 싶음
#        N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 트럭에 태울 수 있는 가장 무거운 무게를 구하라
# 조건 : 자연수 C(1 <= C <= 100,000,000)와 N(1 <= N <= 30)이 주어짐
#        둘째 줄부터 N마리 바둑이의 무게가 주어짐
# 회고 : 04번 문제와 비슷하지만, N의 범위가 30이하임. 즉, 최대 2^30가지의 경우의 수가 생기니 시간 복잡도를 고려했어야 함
#        17번 줄에서 c 보다 큰 sum의 경우 종료시키기 때문에, 19번 줄의 if sum < c는 필요 없었음. 그리고 c미만이 값이 아니라 c보다 '작거나 같아야'함
#        15번 줄의 if sum > c가 14번 줄에서 단일 if문으로 나와있어야 cut edge가 제대로 적용됨
#        부분집합 만들기에 판단된 것들(tsum)과, 남아있는 것들의 합(total - tsum)을 이용하는 방법을 생각하지 못함

# My_Solution -> (실패) Time Limit Exceeded 발생
def DFS(l, sum):
    global max_
    if l == n:
        if sum > c:  # cut edge
            return
        if (max_ < sum) and (sum < c):
            max_ = sum
    else:
        DFS(l + 1, sum + dogs[l])
        DFS(l + 1, sum)


if __name__ == "__main__":
    c, n = map(int, input().split())
    dogs = [int(input()) for _ in range(n)]
    max_ = -2147000000
    DFS(0, 0)
    print(max_)


# Solution_1 -> cut edge 하나 더 추가
import sys

sys.stdin = open("input.txt", "r")


def DFS(l, sum, tsum):
    global result
    if (
        sum + (total - tsum) < result
    ):  # cut edge. (전체 바둑이 무게 - 부분집합 만들기에 판단된 바둑이) = 남은 바둑이들의 무게
        return
    if sum > c:  # cut edge. sum이 c를 초과하면 종료
        return
    if l == n:  # 부분집합 하나가 완성되는 종료지점
        if sum > result:
            result = sum
    else:
        DFS(l + 1, sum + dogs[l], tsum + dogs[l])
        DFS(l + 1, sum, tsum + dogs[l])


if __name__ == "__main__":
    c, n = map(int, input().split())
    dogs = [int(input()) for _ in range(n)]
    result = -2147000000
    total = sum(dogs)  # 바둑이들의 총합
    DFS(0, 0, 0)
    print(result)


# test_case 1
# c, n = 259 5
# dogs = 81
#        58
#        42
#        33
#        61
# result : 242

# test_case 2
# c, n = 3570 15
# dogs = 27
#        303
#        251
#        121
#        50
#        55
#        123
#        93
#        360
#        84
#        353
#        429
#        765
#        391
#        562
# result : 3568
