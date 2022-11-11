# 11. 함수 만들기

# 특정 기능을 하는 코드를 함수화
def add(a, b):
    c = a + b
    print(c)


add(3, 2)


# return : 값을 반환한 뒤 함수 종료
def add(a, b):
    c = a + b
    return c  # 함수가 아닌 main script 쪽에서 결과물을 반환 받아 출력


x = add(3, 2)
print(x)


# 2개의 값을 tuple로 반환
def add(a, b):
    c = a + b
    d = a - b
    return c, d


print(add(3, 2))  # (5, 1)


# 소수를 확인하는 함수
def isPrime(x):  # x : 함수의 지역 변수
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=" ")
