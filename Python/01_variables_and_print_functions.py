# 1. 변수와 출력함수

"""
변수명 정하기
1) 영문과 숫자, _ 로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나, _ 로 시작한다.
3) 특수문자를 사용하면 안된다.(&, % 등)
5) 키워드를 사용하면 안된다.(if, for 등)
"""

a = 1
A = 2
A1 = 3
# 2b = 4
print(a, A, A1)

a, b, c = 3, 2, 1  # 변수 값을 바꾸면, 기존 값이 지워지고 새로운 값이 들어감
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b)

# 변수 타입
a = 12345  # 정수
print(a, type(a))

a = 12.123456789123456789  # 실수, 8 byte까지 저장
print(a, type(a))

a = "student"  # 문자
print(a, type(a))

# 출력방식
print("number")

a, b, c = 1, 2, 3
print(a, b, c)  # 쉼표는 띄어쓰기되어 출력
print("number : ", a, b, c)
print(a, b, c, sep=", ")  # 각 변수 사이를 sep으로 분리
print(a, b, c, sep=",")
print(a, b, c, sep="")
print(a, b, c, sep="\n")  # 줄바꿈
print(a)  # print 함수는 default가 줄바꿈임
print(b, end=" ")  # 줄바꿈을 없앰
print(c)
