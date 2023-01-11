# 2. 이진 트리 순회(DFS : Depth First Search)

# 1) 전위 순회(preorder traverse) : 부모 -> 왼쪽 -> 오른쪽
# My_Solution -> 시작 노드와, 깊이를 매개변수로 받음
def DFS(x, l):
    if l < 3:
        print(x)
        DFS(x * 2, l + 1)
        DFS(x * 2 + 1, l + 1)


if __name__ == "__main__":
    DFS(1, 0)

# Solution_2 -> if ~ else문 사용
def DFS(v):  # v : vertex(=node)
    if v > 7:  # 최대 node를 넘어가면 종료
        return
    else:
        print(v, end=" ")  # DFS 호출 전 출력
        DFS(v * 2)  # 왼쪽 자식 노드 호출
        DFS(v * 2 + 1)  # 오른쪽 자식 노드 호출


if __name__ == "__main__":
    DFS(1)


# 2) 중위 순회(inorder traverse) : 왼쪽 -> 부모 -> 오른쪽
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)  # 왼쪽 자식 노드 호출
        print(v, end=" ")  # 왼쪽 자식이 처리된 후 출력
        DFS(v * 2 + 1)  # 오른쪽 자식 노드 호출


if __name__ == "__main__":
    DFS(1)


# 3) 후위 순회(postorder traerse) : 왼쪽 -> 오른쪽 -> 부모. 병합 정렬에 사용
def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)  # 왼쪽 자식 노드 호출
        DFS(v * 2 + 1)  # 오른쪽 자식 노드 호출
        print(v, end=" ")  # 왼쪽, 오른쪽 자식이 다 처리된 후 출력


if __name__ == "__main__":
    DFS(1)
