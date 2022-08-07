from collections import deque

def solution(n, wires):
    answer = 987654321
    tower = [[0]*(n+1) for _ in range(n+1)]

    for v1, v2 in wires:
        tower[v1][v2], tower[v2][v1] = 1, 1

    for v1, v2 in wires:
        # 연결 끊기
        tower[v1][v2], tower[v2][v1] = 0, 0
        from_v1, from_v2 = 0, 0

        visited = [0] * (n+1)
        for t in [v1, v2]:
            visited[t] = 1
            queue = deque([t])

            while queue:
                now = queue.popleft()

                for i in range(1, n+1):
                    if visited[i]:
                        continue
                    if tower[now][i]:
                        visited[i] = 1
                        queue.append(i)

            if t == v1:
                from_v1 = sum(visited)
            else:
                from_v2 = n - from_v1

        answer = min(answer, abs(from_v1 - from_v2))
        # 원상복구
        tower[v1][v2], tower[v2][v1] = 1, 1

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))