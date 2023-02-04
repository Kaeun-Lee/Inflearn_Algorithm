# 4. 두 리스트 합치기
# 문제 : 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력
# 조건 : 첫 번째 줄에 첫 번째 리스트의 크기 N(1 <= N <100)이 주어짐
#        두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어짐
#        세 번째 줄에 두 번째 리스트의 크기 M(1 <= M <= 100)이 주어짐
#        네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어짐
#        각 리스트의 원소는 int형 변수의 크기를 넘지 않음
# 회고 : 두 리스트를 +로 더한 뒤, sort를 사용해 출력해도 되지만 그렇게 해결하는 문제가 아님
#        이미 정렬되어 있다는 점을 활용해서 합치면 O(n)만에 해결할 수 있음
#        포인터를 이용하여 합치는 방법과 두 리스트 중 남은 리스트를 확인하는 깔끔한 방법을 생각하지 못함
#        while문의 조건을 알맞게 설정하면 if ~ else문의 중첩을 줄일 수 있음
#        while문 안에서 모든 과정을 끝낼 필요는 없음. 기능을 분리하여 코드 가독성을 높이자

# sort() : sort 함수는 quick sort을 이용하고 quick sort의 시간 복잡도는 가장 빠른 게 nlogn임

# My_Solution_1 -> 리스트의 extend 함수로 두 리스트를 합침
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
list1.extend(list2)  # 리스트 합치기
list1 = sorted(list1)  # 오름차순 정렬

for x in list1:
    print(x, end=" ")


# My_Solution_2 -> 두 지점을 가리키는 pointer 변수 사용
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
result = []  # 정렬된 결과값을 담을 리스트
np = mp = 0

while True:
    if np >= n or mp >= m:  # 포인터 값이 리스트 크기를 넘어가는 경우
        result.extend(n_lst[np:])  # 남은 값들을 리스트에 추가
        result.extend(m_lst[mp:])  # 남은 값들을 리스트에 추가
        break
    else:
        if n_lst[np] <= m_lst[mp]:  # 두 리스트를 가리키고 있는 포인터 값 비교
            result.append(n_lst[np])
            np += 1
        else:
            result.append(m_lst[mp])
            mp += 1

for x in result:
    print(x, end=" ")


# Solution_3
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0  # pointer 변수를 0으로 초기화
c = []

while p1 < n and p2 < m:  # 두 포인터 중 하나가 한 리스트 자료를 끝까지 탐색하면 종료
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:  # 남은 자료를 확인한 후 slicing을 이용하여 리스트에 추가
    c += a[p1:]
if p2 < m:
    c += b[p2:]

for x in c:
    print(x, end=" ")


# test_case 1
# n = 3
# list = 1 3 5
# m = 5
# list = 2 3 6 7 9
# result : 1 2 3 3 5 6 7 9

# test_case 2
# n = 10
# list = 1 10 27 39 50 61 65 70 93 93
# m = 7
# list = 7 51 65 66 70 82 93
# result : 1 7 10 27 39 50 51 61 65 65 66 70 70 82 93 93 93

# test_case 3
# n = 9
# list = 14 24 35 38 45 69 78 96 97
# m = 13
# list = 1 15 27 29 40 50 58 63 70 74 75 82 99
# result : 1 14 15 24 27 29 35 38 40 45 50 58 63 69 70 74 75 78 82 96 97 99
