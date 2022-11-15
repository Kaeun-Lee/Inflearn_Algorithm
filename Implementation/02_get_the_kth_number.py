# 2. K번째 수
# 문제 : N개의 숫자로 이루어진 숫자열에서 s 번째부터 e 번째 까지의 수를
#        오름차순 정렬했을 때 k번째로 나타나는 숫자를 출력
# 조건 : 첫 번째 줄에 테스트 케이스 T(1 <= T <= 10)이 주어짐
#        각 케이스별
#        첫 번째 줄은 자연수 N(5 <= N <= 500), s, e, k가 차례로 주어짐
#        두 번째 줄에 N개의 숫자가 차례로 주어짐

# Solution
def kthNumber(number, s, e, k):
    result = sorted(number[s - 1 : e + 1])
    return result[k - 1]



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, s, e, k = map(int, input().split())
        number = list(map(int, input().split()))
        print(kthNumber(number, s, e, k))