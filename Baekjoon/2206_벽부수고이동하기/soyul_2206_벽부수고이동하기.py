import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]       # 3차원 배열 행, 열, 벽뚫었는지 여부
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0))             # 시작점과 벽 뚫었는지 확인하는 flag
    visited[0][0][0] = 1

    while q:
        now_i, now_j, flag = q.popleft()

        if now_i == N-1 and now_j == M-1:
            return visited[now_i][now_j][flag]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어나거나 지나간 곳이면 pass
            if next_i < 0 or next_j < 0 or next_j >= M or next_i >= N:
                continue
            if visited[next_i][next_j][flag]:
                continue

            # 벽을 만나면
            if MAP[next_i][next_j] == 1:
                if not flag:
                    q.append((next_i, next_j, 1))
                    visited[next_i][next_j][1] = visited[now_i][now_j][flag] + 1
            # 지나갈 수 있는곳이면
            if MAP[next_i][next_j] == 0:
                q.append((next_i, next_j, flag))
                visited[next_i][next_j][flag] = visited[now_i][now_j][flag] + 1

    # 끝까지 못갔다면 -1
    return -1

print(bfs())