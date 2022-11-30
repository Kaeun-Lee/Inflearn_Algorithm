# 3. K 번째 큰 수
# 문제 : 1부터 100 사이의 자연수가 적힌 N 장의 카드가 있고 같은 숫자의 카드가 여러 장 있을 수 있다
#        이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 한다. 기록한 값 중 K 번째로 큰 수를 출력
#        *만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19...이고 K 값이 3이라면 K 번째 큰 값은 22이다
# 조건 : 첫 줄에 자연수 N(2 <= N <= 100)과 K(1 <= K <= 50)이 입력됨
#      : 그다음 줄에 N 개의 카드값이 입력됨

# 회고 : 그리드. 문제를 잘 못 알았음. 같은 숫자가 있으면 한 장만 가져야 함 -> set을 적용해서 하나의 숫자들로 만들고 내림차순 정렬하기
#        문제 3중 for문과 range로 index 위치만 +1 해주며 각 자리의 숫자들을 바꿔줘야하는 것을 생각하지 못함.



# My_Solution

n, k = map(int, input().split())
numbers = list(map(int, input().split()))  # [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]
numbers = sorted(set(numbers), reverse=True)  # [65, 45, 42, 34, 33, 26, 23, 15, 13, 11]

# 3중 for문
sum = 0
count = 0
for i in range(n):
    for j in range(i + 1, n):
        for x in range(j + 1, n):
            count += 1
            if count == k:
                sum += numbers[i]
                sum += numbers[j]
                sum += numbers[x]
                print(sum)
                break


# Solution_2
# n, k = map(int, input().split())
# numbers = list(map(int, input().split()))
# result = set()
# for i in range(n):
#     for j in range(i + 1, n):
#         for x in range(j + 1, n):
#             result.add(numbers[i] + numbers[j] + numbers[x])
# result = list(result)
# result.sort(reverse=True)
# print(result[k - 1])