# 3. K번째 큰 수
# 문제 : 1부터 100 사이의 자연수가 적힌 N장의 카드가 있고 같은 숫자의 카드가 여러 장 있을 수 있다
#        이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 한다. 기록한 값 중 K번째로 큰 수를 출력
#        *만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19...이고 K값이 3이라면 K번째 큰 값은 22이다
# 조건 : 첫 줄에 자연수 N(2 <= N <= 100)과 K(1 <= K <= 50)이 입력됨
#        그다음 줄에 N개의 카드값이 입력됨

# 회고 : 같은 숫자가 있으면 큰 숫자를 3장 내에 반복해서 사용 가능하다고 잘못 이해함
#        break문은 하나의 for문만 빠져나올 수 있다는 것을 몰랐음
#        3중 for문과 range로 index 위치만 +1 해주며 각 자리의 숫자들을 바꿔줘야 하는 것을 생각하지 못함
#        같은 숫자가 있으면 한 장만 가져야 함 -> set을 적용해서 하나의 숫자들로 만들고 내림차순 정렬해야 함

# My_Solution -> (실패) 3중 for문에서 바로 k == 3 일 때의 sum을 구하면, k번째 큰 수가 아니라 그냥 k번째 수를 가져옴
# 조건이 맞으면 NotImplementedError(선언되지 않은 에러)를 발생시켜 다중 for문을 빠져나옴
n, k = map(int, input().split())
numbers = list(map(int, input().split()))  # [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]
numbers = sorted(set(numbers), reverse=True)  # [65, 45, 42, 34, 33, 26, 23, 15, 13, 11]

# 3중 for문
count = 1
try:
    for i in range(len(numbers)):  # 0 ~ 8
        for j in range(i + 1, len(numbers)):  # 1 ~ 8
            for x in range(j + 1, len(numbers)):  # 2 ~ 8
                if count == k:
                    raise NotImplementedError
                else:
                    count += 1
except:
    print(numbers[i] + numbers[j] + numbers[x])


# Solution_1
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = set()
for i in range(n):
    for j in range(i + 1, n):
        for x in range(j + 1, n):
            result.add(numbers[i] + numbers[j] + numbers[x])
result = list(result)
result.sort(reverse=True)
print(result[k - 1])


# test case 1
# n, k = 10 3
# numbers = 13 15 34 23 45 65 33 11 26 42
# result = 143

# test case 2
# n, k = 10 3
# numbers = 18 54 46 52 28 22 23 53 28 40
# result = 152

# test case 3
# n, k = 30 7
# numbers = 23 26 50 17 34 35 50 22 53 41 42 44 43 49 37
#           50 28 31 15 37 38 33 48 40 17 42 29 53 23 39
# result = 150
