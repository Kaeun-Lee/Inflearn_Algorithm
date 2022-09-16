# 바둑이 승차

# Solution
def DFS(l, sum, tsum): # l : 각 바둑이 무게에 접근하는 idx, sum : 내가 만드는 부분집합의 합
    global result
    if sum + (total - tsum) < result:
        return
    if sum > c:  # sum이 무게 제한을 넘으면 종료
        return
    if l == n:  # 부분집합 완성. 종료지점
        if sum > result:
            result = sum
    else:
        DFS(l + 1, sum + a[l], tsum + a[l])
        DFS(l + 1, sum, tsum + a[l])
    

if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0] * n           # 바둑이 각각의 무게를 저장할 list
    result = -2147000000  # 아주 작은 값으로 초기화
    for i in range(n):    # 0 1 2 3 4
        a[i] = int(input())
    total = sum(a)        # 바둑이 총합
    DFS(0, 0, 0)
    print(result)


# test case
# input : 259 5
# dogs weight : 81
#               58
#               42
#               33
#               61
# result : 242