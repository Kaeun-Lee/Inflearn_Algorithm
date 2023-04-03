# 4. 대푯값
# 문제 : 학생 N명의 수학 점수가 주어진다. N명의 학생들의 '평균(소수 첫째 짜리 반올림)을 구하고',
#        N명의 학생 중 '평균에 가장 가까운 학생은 몇 번째 학생인지' 출력
#        평균과 가장 가까운 점수가 여러 개일 경우 먼저 '점수가 높은 학생의 번호'를 답으로 하고,
#        높은 점수를 가진 학생이 여러 명일 경우 그중 '학생 번호가 가장 빠른 학생의 번호'를 답으로 한다
# 조건 : 첫 줄에 자연수 N(5 <= N <= 100)이 주어지고, 두 번째 줄에 각 학생의 수학 점수인 N개의 자연수가 주어짐
#        학생의 번호는 앞에서부터 1로 시작해서 N까지임
# 회고 : for문 하나로 구현하는 방법을 생각하지 못해 2개를 사용함
#        평균과의 최소 거리를 구하면서 거리가 같은 경우, 숫자가 클 때만 바꿔주면 가장 먼저 나온 학생 번호를 유지할 수 있음
#        list comprehension으로 작성하는 습관을 들이자

# Python의 round()는 round_half_even 방식이므로, 반올림 계산 시 사용하면 X
# round_half_even 방식 : 반올림하는 자리의 숫자가 정확히 5인 경우, 올림 하는 것이 아니라 "짝수"쪽에 근사 시킴
# (ex) round(4.5) = 4, round(5.5) = 6, round(4.51) = 5
# (cf) 우리가 흔히 사용하는 반올림은 half_up 방식(5 이상은 올림)임
# 따라서 round(a) 대신, int(a + 0.5)를 사용할 것!
# (ex) int(66.5 + 0.5) = 67 -> 소수점이 5 이상인 경우, 1의 자릿수가 증가

# My_Solution -> (실패) 답을 맞히긴 했으나, round 함수로 인해 논리적 결함이 있음
n = map(int, input())
scores = list(map(int, input().split()))

avg = int(round(sum(scores) / len(scores), 0))  # 평균값
diff = float("inf")
result = []

# 평균과 가장 가까운 값의 거리 구하기
for s in scores:
    if abs(avg - s) < diff:
        diff = abs(avg - s)

# 펑균과 가장 가까운 점수와 학생 번호 구하기
for i, s in enumerate(scores):
    if abs(avg - s) == diff:
        result.append((s, i))
result = sorted(result, key=lambda x: (x[0], -x[1]), reverse=True)  # 높은 점수와 번호가 빠른 학생 순으로 정렬
print(avg, result[0][1] + 1)


# Solution_1 -> half up 반올림, 하나의 for문으로 처리
n = int(input())
a = list(map(int, input().split()))

ave = int((sum(a) / n) + 0.5)  # ave = round(sum(a) / n) -> (X)

min = 2147000000  # int형으로 표현할 수 있는 (4byte = 2^31) 정도 되는 가장 큰 수

# 평균과 가장 가까운 점수와 학생 번호 구하기
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:  # 같은 거리의 점수가 나왔을 때
        if x > score:  # (중요) 동일한 점수가 나와도 먼저 나온 번호를 유지. 더 늦은 학생의 번호를 출력하려면, 등호(=) 추가
            score = x
            res = idx + 1
print(ave, res)


# Solution_2 -> list comprehension 이용
n = int(input())
scores = list(map(int, input().split()))
mean_score = int((sum(scores) / n) + 0.5)  # mean_score = int(round((sum(scores) / n), 0)) -> (X)

lst = list(map(lambda x: abs(x - mean_score), scores))  # |점수-평균|
min_lst = min(lst)

result = [(i, std) for i, std in enumerate(scores) if abs(std - mean_score) == min_lst]
result = sorted(result, key=lambda x: (x[-1], -x[0]), reverse=True)
print(mean_score, result[0][0] + 1)


# test case 1
# n = 10
# scores = 45 73 66 87 92 67 75 79 75 80
# result : 74 7

# test case 2
# n = 15
# scores = 12 34 17 6 11 15 27 42 39 31 25 36 35 25 17
# result : 25 11

# test case 3
# n = 10
# scores = 12 34 17 6 11 15 27 42 39 31
# result : 23 7
