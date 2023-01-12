# 5-1. [잠깐 지식] 전역변수와 지역변수

# 전역변수 : main script에 선언되는 변수. 공용. 모든 함수가 다 접근 및 변경할 수 있음


# 예시 1 -> 전역변수만 있는 경우
def DFS1():
    print(cnt)  # 자신의 지역변수인지 확인 후 아니라면 전역변수 출력


def DFS2():
    if cnt == 5:  # 자신의 지역변수인지 확인 후 아니라면 전역변수 출력
        print(cnt)


if __name__ == "__main__":
    cnt = 5  # 전역변수 생성 후 값 5를 할당
    DFS1()
    DFS2()
    print(cnt)


# 예시 2 -> 이름이 같은 변수가 있을 때, 지역변수가 전역변수보다 우선됨
def DFS1():
    cnt = 3  # 지역변수 생성 후 값 3을 할당
    print(cnt)  # 지역변수 출력


def DFS2():
    if cnt == 5:  # 전역변수 출력
        print(cnt)


if __name__ == "__main__":
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)


# 예시 3 -> cnt가 지역변수로 언어 번역이 됐는데 cnt에 값이 할당되지 않아 에러 발생
# def DFS1():
#     cnt = 3
#     print(cnt)


# def DFS2():
#     if cnt == 5:  # 지역변수 cnt에 값이 할당되지 않았는데 5와 비교했기 때문에 에러 발생
#         cnt = cnt + 1  # cnt가 지역변수화됨. 지역변수 생성 후 그 값을 참조하는 코드
#         print(cnt)


# if __name__ == "__main__":
#     cnt = 5
#     DFS1()
#     DFS2()
#     print(cnt)


# 예시 4 -> global로 전역변수 cnt를 가져와 에러 해결
def DFS1():
    cnt = 3  # 지역변수
    print(cnt)


def DFS2():
    global cnt  # 전역변수 cnt임을 미리 알려줌
    if cnt == 5:  # 전역변수 cnt
        cnt = cnt + 1  # 지역변수 cnt로 선언하지 않음. 전역변수 cnt에 1을 더해 전역변수의 값을 바꿈
        print(cnt)


if __name__ == "__main__":
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)  # 값이 바뀐 전역변수


# 리스트의 경우, 값이 바뀌어도 지역 리스트화되지 않고 전역 리스트를 참조해서 오류 없이 작동되는 이유?


# 예시 1 -> a[0] = 7은 새로운 지역 리스트를 생성하는 게 아니라 값만 변경함
def DFS():
    a[0] = 7  # 전역 리스트 a의 0번 idx 값을 7로 변경
    print(a)


if __name__ == "__main__":
    a = [1, 2, 3]  # 전역 리스트 a를 생성
    DFS()
    print(a)  # 0번 idx가 7로 변경된 전역 리스트 a를 출력


# 예시 2 -> 지역 리스트를 선언한 경우
def DFS():
    a = [7, 8]  # 지역 리스트 생성
    print(a)  # 지역 리스트 출력


if __name__ == "__main__":
    a = [1, 2, 3]  # 전역 리스트 a를 생성
    DFS()
    print(a)  # 전역 리스트 출력


# 예시 3 -> 리스트 a가 지역 리스트로 인식될 때 에러 발생
# def DFS():
#     a = a + [4]  # 지역 리스트 a에 아무 값도 할당되지 않아 참조할 수 없음
#     print(a)


# if __name__ == "__main__":
#     a = [1, 2, 3]  # 전역 리스트 a를 선언
#     DFS()
#     print(a)


# 예시 4 -> global로 전역 리스트 a를 가져와 에러 해결
def DFS():
    global a  # 전역 리스트 a임을 미리 알려줌
    a = a + [4]  # 전역 리스트 a에 [4]를 더함
    print(a)  # 변경된 전역 리스트 출력


if __name__ == "__main__":
    a = [1, 2, 3]  # 전역 리스트 a를 선언
    DFS()
    print(a)  # 변경된 전역 리스트 출력
