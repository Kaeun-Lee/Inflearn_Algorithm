# 전위 순회(preorder traverse)

def DFS(v):  # v : vertex(=node)
    if v > 7:  # 최대 노드를 넘어가면 종료
        return
    else: 
        print(v, end=' ')  # DFS 호출 전 출력
        DFS(v * 2)         # 왼쪽 자식 노드 호출
        DFS(v * 2 + 1)     # 오른쪽 자식 노드 호출


# 중위 순회(inorder traverse)
def DFS(v):  
    if v > 7:  # 최대 노드를 넘어가면 종료
        return
    else: 
        DFS(v * 2)         # 왼쪽 자식 노드 호출
        print(v, end=' ')  # 왼쪽 자식이 처리된 후 출력
        DFS(v * 2 + 1)     # 오른쪽 자식 노드 호출


# 후위 순회(postorder traverse) -> 병합 정렬에 사용
def DFS(v):  
    if v > 7:  # 최대 노드를 넘어가면 종료
        return
    else: 
        DFS(v * 2)         # 왼쪽 자식 노드 호출
        DFS(v * 2 + 1)     # 오른쪽 자식 노드 호출
        print(v, end=' ')  # 왼쪽, 오른쪽 자식이 다 처리된 후 철력

if __name__ == "__main__":
    DFS(1)