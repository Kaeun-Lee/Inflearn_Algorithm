# 6. 중첩 반복문(2중 for문)

for i in range(5):
    print("i:", i, sep="", end=" ")
    for j in range(5):
        print("j:", j, sep="", end=" ")
    print()  # 줄바꿈


# 별 찍기(5 x 5)
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# 삼각형 별 찍기
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()


# 역삼각형 별 찍기 1
for i in range(5):
    for j in range(5 - i):
        print("*", end=" ")
    print()


# 역삼각형 별 찍기 2
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
