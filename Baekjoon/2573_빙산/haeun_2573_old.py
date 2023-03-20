import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer, year = 0, 0
icebergs = list()  # 빙산의 좌표(x, y)를 리스트에 저장

for r in range(N):
    for c in range(M):
        if grid[r][c]:
            icebergs.append((r, c))

while icebergs:
    melt_icebergs = list()  # 녹은 애들의 위치를 저장해두고 뺀다.
    for row, col in icebergs:
        sea = 0
        for d in range(4):
            around_row, around_col = row + dr[d], col + dc[d]
            if 0 <= around_row < N and 0 <= around_col < M:
                if grid[around_row][around_col] == 0:
                    sea += 1

        if grid[row][col] - sea <= 0:  # 녹았으면 그냥 빼버려 (0처리는 뒤에서)
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

    # 특이점. 처음 나온 빙산 덩어리만 본다.
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

    # 모든 빙산이 이어져있다면 connected가 빙산의 수와 같아야하지만,
    # 나뉘어있다면 첫 빙산 덩어리의 개수는 전체 빙산의 개수보다 적을 것이다.
    if connected < len(icebergs):
        answer = year
        break

print(answer)