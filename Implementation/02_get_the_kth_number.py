# 2. K번째 수
# 문제 : N개의 숫자로 이루어진 숫자열에서 s 번째부터 e 번째 까지의 수를
#        오름차순 정렬했을 때 k번째로 나타나는 숫자를 출력
# 조건 : 첫 번째 줄에 테스트 케이스 T(1 <= T <= 10)이 주어짐
#        각 케이스별
#        첫 번째 줄은 자연수 N(5 <= N <= 500), s, e, k가 차례로 주어짐
#        두 번째 줄에 N개의 숫자가 차례로 주어짐

# 회고 : 리스트 인덱싱에서 e를 입력하면 e - 1이 나오는데, 착각해서 e + 1을 입력했었음

# My_Solution
def kth_number(numbers, s, e, k):
    result = sorted(numbers[s - 1 : e])
    return result[k - 1]


# Solution_2
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    num = num[s - 1 : e]
    num.sort()
    print(f"#{t + 1}", num[k - 1])


if __name__ == "__main__":
    t = int(input())  # case의 개수
    for _ in range(t):  # case 별로 읽어음
        n, s, e, k = map(int, input().split())
        numbers = list(map(int, input().split()))
        print(f"#{_ + 1} ", kth_number(numbers, s, e, k))


# test case 1
# t = 2
# n, s, e, k = 6 2 5 3
# t1 numbers = 5 2 7 3 8 9
# n, s, e, k = 15 3 10 3
# t2 numbers = 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
# return : #1 7
#          #2 6


# test case 2
# t = 3
# n, s, e, k = 15 3 10 3
# t1 numbers = 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
# n, s, e, k = 6 2 5 3
# t2 numbers = 5 2 7 3 8 9
# n, s, e, k = 100 20 60 21
# t3 numbers = 148 810 785 695 201 113 382 234 50 567 586 345 725 614 633 882 671
#              748 330 705 899 147 947 436 442 963 918 492 948 691 429 591 509 629
#              227 884 963 939 998 606 343 359 743 573 810 911 292 529 530 584 345
#              88 110 66 818 898 358 749 428 116 638 650 965 394 780 445 816 312 968
#              225 653 426 356 565 609 442 60 678 314 50 264 469 518 155 328 170 421
#              981 951 329 907 616 954 412 658 395 355 345 784 242
# return : #1 6
#          #2 7
#          #3 584
