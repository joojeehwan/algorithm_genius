import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(2 ** N))
L = list(map(int, sys.stdin.readline().split()))
grid_size = 2 ** N

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def rotate(start_row, start_col, level):
    length = 2**level
    copy_grid = [[0]* length for _ in range(length)]

    # 임시 저장
    for row in range(length):
        for col in range(length):
            copy_grid[col][length-row-1] = grid[start_row+row][start_col+col]

    # 임시 저장 옮기기
    for row in range(length):
        for col in range(length):
            grid[start_row+row][start_col+col] = copy_grid[row][col]


for l in L:
    level_size = 2 ** l
    # 부분 격자로 나누기
    for r in range(0, grid_size - level_size + 1, level_size):
        for c in range(0, grid_size - level_size + 1, level_size):
            rotate(r, c, l)

    # 인접한 얼음 녹이기
    melt = []
    for r in range(grid_size):
        for c in range(grid_size):
            connected = 0
            for d in range(4):
                next_row = r + dr[d]
                next_col = c + dc[d]

                if 0 <= next_row < grid_size and 0 <= next_col < grid_size:
                    # 얼음일 경우
                    if grid[next_row][next_col] > 0:
                        connected += 1
            # 인접한 얼음이 2개 이하인 경우 1씩 녹는다.
            if connected <= 2:
                melt.append((r, c))

    for melt_r, melt_c in melt:
        if grid[melt_r][melt_c]:
            grid[melt_r][melt_c] -= 1

# Level 다 적용한 경우
total_ice, max_connected = 0, 0
visited = [[0] * grid_size for _ in range(grid_size)]
for r in range(grid_size):
    for c in range(grid_size):
        if not visited[r][c] and grid[r][c]:
            total_ice += grid[r][c]
            connected_cnt = 1
            visited[r][c] = 1
            con_queue = deque([(r, c)])

            while con_queue:
                now_r, now_c = con_queue.popleft()

                for d in range(4):
                    next_row = now_r + dr[d]
                    next_col = now_c + dc[d]

                    if 0 <= next_row < grid_size and 0 <= next_col < grid_size:
                        # 방문하지 않았고, 얼음일 경우
                        if not visited[next_row][next_col] \
                                and grid[next_row][next_col]:
                            visited[next_row][next_col] = 1
                            con_queue.append((next_row, next_col))
                            connected_cnt += 1
                            total_ice += grid[next_row][next_col]

            max_connected = max(connected_cnt, max_connected)

print(total_ice)
print(max_connected)