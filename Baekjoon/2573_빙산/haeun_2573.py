"""
이전 버전 : 540ms, 153420KB
새 버전 : 992ms, 209084KB (뭐야?)
"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

year = 0
icebergs = 1


def melting():
    visited = [[0] * M for _ in range(N)]
    minus = [[0] * M for _ in range(N)]

    # 빙하마다 바다 세기
    for r in range(1, N-1):
        for c in range(1, M-1):
            if not visited[r][c] and grid[r][c]:
                visited[r][c] = 1

                queue = deque([(r, c)])
                while queue:
                    row, col = queue.popleft()

                    for d in range(4):
                        around_row, around_col = row + dr[d], col + dc[d]
                        if 0 <= around_row < N and 0 <= around_col < M and not visited[around_row][around_col]:
                            if grid[around_row][around_col] == 0:
                                minus[row][col] += 1
                            else:
                                queue.append((around_row, around_col))
                                visited[around_row][around_col] = 1

    # 녹이기
    for r in range(1, N-1):
        for c in range(1, M-1):
            grid[r][c] = grid[r][c] - minus[r][c]
            if grid[r][c] <= 0: grid[r][c] = 0


def counting():
    visited = [[0] * M for _ in range(N)]
    count = 0
    # 빙하덩어리 세기

    for r in range(1, N-1):
        for c in range(1, M-1):
            if not visited[r][c] and grid[r][c]:
                count += 1
                visited[r][c] = 1

                queue = deque([(r, c)])
                while queue:
                    row, col = queue.popleft()

                    for d in range(4):
                        around_row, around_col = row + dr[d], col + dc[d]
                        if 0 <= around_row < N and 0 <= around_col < M and \
                                not visited[around_row][around_col] and grid[around_row][around_col] > 0:
                            queue.append((around_row, around_col))
                            visited[around_row][around_col] = 1
    return count


while icebergs == 1:
    melting()
    icebergs = counting()
    year += 1

print(year if icebergs > 0 else 0)
