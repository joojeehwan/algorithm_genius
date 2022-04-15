import sys
from collections import deque

def bfs(now_i, now_j):

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    # 공백 큐 생성, 시작점 넣어주기, 방문표시
    q = deque()
    q.append((now_i, now_j, 0))
    visited[now_i][now_j] = 1

    while q:
        now_i, now_j, cnt = q.popleft()

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어났거나 지나갔던 곳이거나 육지가 아니면 pass
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                continue
            if visited[next_i][next_j]:
                continue
            if MAP[next_i][next_j] != 'L':
                continue

            visited[next_i][next_j] = visited[now_i][now_j] + 1
            q.append((next_i, next_j, cnt + 1))

    return cnt


n, m = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 'L':         # 육지면 bfs 진행
            visited = [[0] * m for _ in range(n)]
            ans = max(ans, bfs(i, j))

print(ans)