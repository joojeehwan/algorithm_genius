from collections import deque


def solution(n, wires):
    ans = 987654321
    # 간선 하나씩 잘라보며 비교
    for i in range(len(wires)):
        # 간선 하나 자른 트리 생성
        tree = [[] for _ in range(n + 1)]
        visited = [0] * (n + 1)  # 노드 방문 정보
        for wire in (wires[:i] + wires[i+1:]):
            tree[wire[0]].append(wire[1])
            tree[wire[1]].append(wire[0])
        for idx, starting in enumerate(tree):
            if starting:  # 연결된 노드 찾음
                visited[idx] = 1
                queue = deque()
                for start in starting:  # 찾은 노드를 중심으로 연결된 노드들 탐색 (BFS)
                    queue.append(start)
                while queue:
                    now = queue.popleft()
                    if visited[now]:
                        continue
                    visited[now] = 1
                    for new in tree[now]:
                        if visited[new]:  # 이미 방문함
                            continue
                        queue.append(new)
                break  # 하나의 트리를 찾으면 다른 트리에 연결된 노드의 수도 계산 가능
        ans = min(ans, abs(n - (n - sum(visited)) - (n - sum(visited))))
    return ans


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
print(solution(3, [[1,2],[2,3]]))
print(solution(6, [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]))