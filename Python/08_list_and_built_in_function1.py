# 8. 리스트와 내장함수(1)

import random as r

# 리스트 생성
a = []
b = list()
print(a)
print(b)

a = [1, 2, 3, 4, 5]
print(a)


# 리스트 인덱싱
print(a[0])


# range를 사용해 리스트 값 초기화
b = list(range(1, 11))
print(b)


# 리스트 더하기 -> 두 리스트가 연결됨
c = a + b
print(c)


# 리스트 내장함수
# 값 추가
a.append(6)  # 리스트의 맨 끝에 값 추가
print(a)

a.insert(3, 7)  # 특정 인덱스 지점에 값 추가
print(a)


# 값 제거
a.pop()  # 리스트의 맨 끝 값을 꺼내고 제거
print(a)

a.pop(3)  # 리스트의 idx 위치에 있는 값을 꺼내고 제거
print(a)


# 특정 값 지우기
a.remove(4)  # 특정 값을 찾아서 제거
print(a)


# 특정 값의 idx 찾기
print(a.index(5))  # 리스트에 있는 특정 값의 idx를 return


# 리스트 합, 최댓값, 최솟값
a = list(range(1, 11))
print(a)
print(sum(a))  # 리스트의 모든 요소의 합
print(max(a))  # 리스트의 값 중 가장 최댓값
print(min(a))  # 리스트의 값 중 가장 최솟값
print(min(7, 5))  # 인자들 중 최솟값
print(min(7, 3, 5))


# 리스트 안의 값을 무작위로 섞기
r.shuffle(a)  # 게임에서 무작위 위치 설정할 때 많이 사용
print(a)


# 리스트 정렬
a.sort(reverse=True)  # 내림차순 정렬
print(a)

a.sort()  # 오름차순 정렬
print(a)


# 리스트에 있는 모든 값 제거
a.clear()
print(a)  # 빈 리스트
