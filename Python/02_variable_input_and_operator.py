# 2. 변수입력과 연산자

# 키보드로 변수에 값 입력하기
a = input("숫자를 입력하세요 : ")
print(a)

a, b = input("숫자를 입력하세요 : ").split()  # 공백을 기준으로 분리
print(type(a))
c = a + b
print(c, type(c))  # 문자끼리 연결됨

a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(type(a), a + b)

# map 함수로 int 만들기
a, b = map(int, input("숫자를 입력하세요 : ").split())

# 사칙 연산
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # 몫
print(a % b)  # 나머지
print(a**b)  # 거듭제곱

a = 4.3
b = 5
c = a + b  # 실수형 + 정수형 = 실수형. 실수가 정수보다 넒은 범위임
print(c, type(c))
