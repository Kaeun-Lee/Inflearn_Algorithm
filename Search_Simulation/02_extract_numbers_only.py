# 2. 숫자만 추출
# 문제 : 문자와 숫자가 섞여있는 문자열이 주어지면 그중 숫자만 추출하여 그 순서대로 자연수를 만듦
#        만들어진 자연수와 그 자연수의 약수 개수를 출력
#        만약 "t0e0a1c2h0er"에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수로 만들면 120이 됨
#        즉 첫 자리 0은 자연수화할 때 무시함. 출력은 120을 출력한 뒤, 다음 줄에 120의 약수의 개수를 출력하면 됨
#        추출하여 만들어지는 자연수는 100,000,000을 넘지 않음
# 조건 : 첫 줄에 숫자가 섞인 문자열이 주어짐. 문자열의 길이는 50을 넘지 않음
# 회고 : 문자열 "00120"을 int 함수에 넣으면(int(00120)) 120이 됨
#        첫 자리의 연속된 0을 제거하는 식을 앞에서 공부했으나 또 내가 편한 방법으로 구현했음
#        손에 잘 익지 않고 바로 떠오르지 않아도 배운 것을 계속 사용하려는 자세를 갖자

# "0".isdecimal() : 0 ~ 9까지의 숫자만 찾음
# "0".isdigit() : 알파벳이 아닌 숫자 형태는 다 찾음. 2^2, 2^31도 숫자로 인식함

# My_Solution -> 문자열을 이용
import sys
import math

sys.stdin = open("input.txt", "r")
string = input()
num = ""
cnt = 0

for i in string:  # 숫자만 추출
    if i.isdigit():
        num += i

for i in range(1, int(math.sqrt(int(num))) + 1):
    if int(num) % i == 0:
        if i == math.sqrt(int(num)):  # 약수가 제곱근인 경우 +1
            cnt += 1
        else:
            cnt += 2
print(int(num))
print(cnt)


# Solution_2 -> 식을 활용
s = input()
res = 0
cnt = 0

for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)


# test_case 1
# string = g0en2Ts8eSoft
# result : 28
#          6

# test_case 2
# string = kdk1k0kdjfkj0kkdjkfj0fkd
# result : 1000
#          16

# test_case 3
# string = dkf0jkk0dkjkgjljl1kgh0ekjlkjf2lkjsklfjlkdj
# result : 102
#          8
