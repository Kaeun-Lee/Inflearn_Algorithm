# 4. 대푯값
# 문제 : 학생 N명의 수학점수가 주어진다. N명의 학생들의 평균(소수 첫째짜리 반올림)을 구하고,
#        N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력
#        평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
#        높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 가장 빠른 학생의 번호를 답으로 한다
# 조건 : 첫 줄에 자연수 N(5 <= N <= 100)이 주어지고, 두 번째 줄에 각 학생의 수학점수인 N개의 자연수가 주어짐
#        학생의 번호는 앞에서부터 1로 시작해서 N까지임
# 회고 :

# My_Solution
n = map(int, input())
scores = list(map(int, input().split()))
avg = int(round(sum(scores) / len(scores), 0))

diff = 999999
for i in scores:
    if abs(avg - i) < diff:
        diff = abs(avg - i)

result = []
for i, v in enumerate(scores):
    if abs(avg - v) == diff:
        result.append((v, i))
result = sorted(result, key=lambda x: (x[0], -x[1]), reverse=True)[0]
print(avg, result[1] + 1)


# test case 1
# N : 10
# scores : 45 73 66 87 92 67 75 79 75 80
# result : 74 7

# test case 2
# N : 15
# scores : 12 34 17 6 11 15 27 42 39 31 25 36 35 25 17
# result : 25 11

# test case 3
# N : 10
# scores : 12 34 17 6 11 15 27 42 39 31
# result : 23 7

