from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def solution(map):
    queue = deque([(0, 0)])
    N = len(map[0])
    M = len(map)
    visited = [[0] * N for _ in range(M)]
    visited[0][0] = 1

    while queue:
        now_r, now_c = queue.popleft()

        for d in range(4):
            new_r = now_r + dr[d]
            new_c = now_c + dc[d]

            if 0 <= new_r < M and 0 <= new_c < N:
                if not visited[new_r][new_c] and map[new_r][new_c]:
                    visited[new_r][new_c] = visited[now_r][now_c] + 1
                    queue.append((new_r, new_c))

    return visited[M-1][N-1] if visited[M-1][N-1] else -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))