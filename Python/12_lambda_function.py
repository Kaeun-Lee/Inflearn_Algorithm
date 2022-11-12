# 12. 람다 함수(익명 함수, 람다 표현식)

# 일반적인 함수
def plus_one(x):
    return x + 1


print(plus_one(1))


# 람다 함수 -> 호출하려면 변수에 할당해야 함
plus_two = lambda x: x + 2
print(plus_two(1))


# 람다 함수의 활용 -> 내장 함수의 인자, sorted 함수의 key 인자로 사용
# map(함수, 자료)
a = [1, 2, 3]
print(list(map(plus_one, a)))

print(list(map(lambda x: x + 1, a)))
