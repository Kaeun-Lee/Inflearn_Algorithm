# 4. 두 리스트 합치기
# 문제 : 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력
# 조건 : 첫 번째 줄에 첫 번째 리스트의 크기 N(1 <= N <100)이 주어짐
#        두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어짐
#        세 번째 줄에 두 번째 리스트의 크기 M(1 <= M <= 100)이 주어짐
#        네 번째 줄에 M개의 리스트으 원소가 오름차순으로 주어짐
#        각 리스트의 원소는 int형 변수의 크기를 넘지 않음
# 회고 :

# sort() : sort() 함수로 호출했을 때 시간 복잡도는 nlogn임
#          sort()는 퀵 정렬로 만들어지고 퀵 정렬의 시간 복잡도는 가장 빠른 게 nlogn임

# My_Solution -> 리스트의 extend로 두 리스트를 합침
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


# test_case 1
# n = 3
# list = 1 3 5
# m = 5
# list = 2 3 6 7 9
# result : 1 2 3 3 5 6 7 9
