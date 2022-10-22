# 조건문(if 분기문, 다중 if문)

x = 7
if x != 7:  # 관계 연산자. 같으면 True, 다르면 False
    print("Lucky")
    print("ㅋㅋ")


# 중첩 if문
x = 12
if x >= 10:
    if x % 2 == 1:
        print("10 이상의 홀수")

x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")

# 논리 연산자를 사용해 하나의 if문으로 만들기
x = 7
if x > 0 and x < 10:
    print("10보다 작은 자연수")

x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")


# if 분기문 -> 양 갈래로 갈라짐
x = -3
if x > 0:
    print("양수")
else:
    print("음수")


# 다중 if문 -> if ~ else문 사용
x = 50
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >=60 :
    print("D")
else:
    print("F")