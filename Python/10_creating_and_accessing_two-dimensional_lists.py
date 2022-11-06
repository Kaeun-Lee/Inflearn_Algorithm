# 2차원 리스트 생성과 접근

# 1차원 리스트 생성
a = [0] * 3  # 0으로 초기화 한 3개의 리스트 값 생성
print(a)


# 2차원 리스트 생성
a = [[0] * 3 for _ in range(3)]  # 반복문을 3번 돌면서, 0으로 초기화 된 크기가 3인 1차원 list를 생성
print(a)


# 2차원 리스트 좌표에 접근하여 값을 변경
a[0][1] = 1
print(a)
a[1][1] = 2
print(a)


# 2차원 리스트를 표 형태로 출력
for x in a:
    print(x)


# 2차원 리스트를 대괄호 없이 표 형태로 출력
for x in a:
    for y in x:
        print(y, end=" ")
    print()
