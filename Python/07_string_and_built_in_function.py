# 7. 문자열과 내장함수

# 대문자 or 소문자로 변경
msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)  # 원래 문자는 변하지 않음


# 찾는 문자의 idx, 개수 찾기
tmp = msg.upper()
print(tmp)  # IT IS TIME
print(tmp.find("T"))  # 가장 먼저 나오는 T의 idx. 없으면 -1을 리턴
print(tmp.count("T"))  # 문자 T의 개수


# 문자열 슬라이싱(부분 문자열)
print(msg[:2])
print(msg[3:5])


# 문자열 길이(공백 포함)
print(len(msg))


# 문자열 인덱싱
for i in range(len(msg)):
    print(msg[i], end=" ")
print()


# 문자열의 문자 하나하나에 접근
for x in msg:
    print(x, end=" ")
print()


# 대문자 or 소문자인지 확인
for x in msg:
    if x.isupper():  # x가 대문자면 True
        print(x, end=" ")
print()

for x in msg:
    if x.islower():
        print(x, end=" ")  # x가 소문자면 True
print()


# 공백 제거 후 출력
for x in msg:
    if x.isalpha():  # 알파벳일 때만 True
        print(x, end="")
print()


# ASCII 코드로 출력 -> A: 65, Z: 90, a: 97, z: 122
tmp = "AZ"
for x in tmp:
    print(ord(x))

tmp = "az"
for x in tmp:
    print(ord(x))


# ASCII 코드를 문자로 출력
tmp = 65
print(chr(tmp))
