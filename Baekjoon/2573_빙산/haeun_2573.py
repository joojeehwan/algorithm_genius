"""
pypy로 안하면 해결 안됨

"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer, year = 0, 0
icebergs = list()

for r in range(N):
    for c in range(M):
        if grid[r][c]:
            icebergs.append((r, c))

while icebergs:
    melt_icebergs = list()
    for row, col in icebergs:
        sea = 0
        for d in range(4):
            around_row, around_col = row + dr[d], col + dc[d]
            if 0 <= around_row < N and 0 <= around_col < M:
                if grid[around_row][around_col] == 0:
                    sea += 1

        if grid[row][col] - sea <= 0:
            melt_icebergs.append((row, col))
        else:
            grid[row][col] -= sea

    year += 1

    for melt_row, melt_col in melt_icebergs:
        grid[melt_row][melt_col] = 0
        icebergs.remove((melt_row, melt_col))

    if not icebergs:
        break

    queue = deque()
    queue.append((icebergs[0]))
    visited = [[0] * M for _ in range(N)]
    visited[icebergs[0][0]][icebergs[0][1]] = 1
    connected = 1

    while queue:
        row, col = queue.pop()
        for d in range(4):
            around_row, around_col = row + dr[d], col + dc[d]
            if 0 <= around_row < N and 0 <= around_col < M:
                if not visited[around_row][around_col]:
                    if grid[around_row][around_col]:
                        visited[around_row][around_col] = 1
                        connected += 1
                        queue.append((around_row, around_col))

    if connected < len(icebergs):
        answer = year
        break

print(answer)
