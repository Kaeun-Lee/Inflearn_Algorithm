# 2. 이진 트리 순회(DFS : Depth First Search)

# 전위 순회 : 부모 -> 왼쪽 -> 오른쪽
# 중위 순회 : 왼쪽 -> 부모 -> 오른쪽
# 후위 순회 : 왼쪽 -> 오른쪽 -> 부모. 병합 정렬에 쓰임


# 1) 전위 순회
# My_Solution -> 시작 노드와, 깊이를 매개변수로 받음
def DFS(x, l):
    if l < 3:
        print(x)
        DFS(x * 2, l + 1)
        DFS(x * 2 + 1, l + 1)


if __name__ == "__main__":
    DFS(1, 0)

# Solution_2 -> if ~ else문 사용
def DFS(v):  # 매개 변수 v로 노드 값을 받음
    if v > 7:
        return
    else:
        print(v, end=" ")  # 호출 전 방문한 노드를 출력(전위 순회)
        DFS(v * 2)
        DFS(v * 2 + 1)


if __name__ == "__main__":
    DFS(1)


# 2) 중위 순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        print(v, end=" ")  # 왼쪽 노드 호출 후 방문한 노드를 출력(중위 순회)
        DFS(v * 2 + 1)


if __name__ == "__main__":
    DFS(1)


# 3) 후위 순회
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        DFS(v * 2 + 1)
        print(v, end=" ")  # 왼쪽, 오른쪽 노드 호출 후 방문한 노드를 출력(후위 순회)


if __name__ == "__main__":
    DFS(1)
