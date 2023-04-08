from collections import deque


def solution(maps):
    row, col = len(maps), len(maps[0])
    start = (0, 0)  # 시작점
    end = (row - 1, col - 1)  # 도착점
    visited = [[row * col + 1 for _ in range(col)] for _ in range(row)]  # 방문 정보
    visited[start[0]][start[1]] = 1
    answer = -1

    # BFS
    queue = deque()
    queue.append(start)
    while queue:
        now_r, now_c = queue.popleft()
        for dr, dc in [(1, 0), (0, -1), (-1, 0), (0, -1)]:  # 남동북서
            new_r, new_c = now_r + dr, now_c + dc
            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:  # 맵 밖임
                continue
            if not maps[new_r][new_c]:  # 벽임
                continue
            if visited[new_r][new_c] <= visited[now_r][now_c] + 1:  # 기존 경로가 더 짧음
                continue
            if (new_r, new_c) == end:  # 도착점에 도착
                answer = visited[now_r][now_c] + 1
                return answer
            # 이동
            visited[new_r][new_c] = visited[now_r][now_c] + 1
            queue.append((new_r, new_c))
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))