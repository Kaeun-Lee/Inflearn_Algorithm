# 등호(=)를 넣지 않았기 때문에 arr[4]가 최솟값이 되었지만, 등호를 넣으면 arr[6]이 최솟값이 됨
# 순서나 index가 중요한 경우라면 등호(=)를 넣어줄 수도 있음!


# Solution 1 -> python에서 가장 큰 값을 저장(무한대)
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float("inf")

for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)


# Solution 2 -> 첫 번째 값을 min으로 저장한 후 1번 index부터 비교
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = arr[0]

for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)


# Solution 3
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arr_min = float("inf")  # python에서 가장 큰 값

for i in range(len(arr)):
    if arr[i] < arr_min:
        arr_min = arr[i]

print(arr_min)
