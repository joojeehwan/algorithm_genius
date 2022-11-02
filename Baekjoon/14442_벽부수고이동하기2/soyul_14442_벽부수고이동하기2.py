import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while q:
        now_i, now_j, cnt = q.popleft()

        if now_i == N-1 and now_j == M-1:
            return visited[now_i][now_j][cnt]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어나거나 지나갔던 곳이면 패스
            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
                continue
            if visited[next_i][next_j][cnt]:
                continue

            # 벽을 만나면
            if MAP[next_i][next_j]:
                # 벽을 뚫을 수 있는 횟수가 남아있다면
                if cnt < K and visited[next_i][next_j][cnt+1] == 0:
                    q.append((next_i, next_j, cnt+1))
                    visited[next_i][next_j][cnt+1] = visited[now_i][now_j][cnt] + 1

            # 그냥 갈 수 있는 곳이라면
            if MAP[next_i][next_j] == 0:
                q.append((next_i, next_j, cnt))
                visited[next_i][next_j][cnt] = visited[now_i][now_j][cnt] + 1


    return -1

print(bfs())