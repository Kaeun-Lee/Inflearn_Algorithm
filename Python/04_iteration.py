# 4. 반복문(for, while, break, continue)

# range 함수
a = range(1, 11)  # 순차적으로 정수 list를 만들어 a에 대입. 1 ~ 10
print(list(a))


# for 문
for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)


# while 문
i = 1
while i <= 10:  # 10까지 참
    print(i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1


# break 문 -> 반복문을 돌다가 특정 조건에서 참이 되면 멈춤 or 무한 반복을 멈춤
i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1


# continue
for i in range(1, 11):
    if i % 2 == 0:  # continue 밑에 있는 구문들은 pass
        continue
    print(i)


# for ~ else 구문 -> for문의 break
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:  # for 문 도중에 break되어 비정상 종료된 경우, else 문을 실행하지 않음
    print(11)
