# 네트워크 선 자르기(Bottom-Up)
# 문제 : 네트워크 선의 길이가 Nm일 때 몇가지의 자르는 방법이 나올까?
#        부분증가수열의 최대 길이 출력
# 조건 : 네트워크 선의 총 길이인 자연수 N(3 <= N <= 45)

# Solution
n = int(input())
dy = [0] * (n + 1)
dy[1] = 1
dy[2] = 2
for i in range(3, n + 1):
    dy[i] = dy[i - 1] + dy[i - 2]
print(dy[n])


# test case
# input : 7
# result : 21