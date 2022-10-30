# 9. 리스트와 내장함수(2)

a = [23, 12, 36, 53, 19]

# 리스트 슬라이싱
print(a[:3])
print(a[1:4])


# 리스트 길이
print(len(a))


# 리스트 인덱싱
for i in range(len(a)):
    print(a[i], end=" ")
print()

# 리스트의 값 하나하나에 접근
for x in a:
    print(x, end=" ")
print()

for x in a:
    if x % 2 == 1:
        print(x, end=" ")
print()


# 리스트의 idx와 원소 값에 접근
for x in enumerate(a):  # idx와 value를 튜플로 출력 (0, 23)
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()


# Tuple : 원소 값 변경 불가
b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7


# all, any 함수
if all(60 > x for x in a):  # 조건문(60 > x)이 '모두 참'이면 True
    print("YES")
else:
    print("NO")

if any(11 > x for x in a):  # 조건문(15> x)이 '한 번이라도 참'이면 True
    print("YES")
else:
    print("NO")
