from collections import deque

height, width = map(int, input().split())
MAP = list(list(input()) for _ in range(height))

land_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for row in range(height):
    for col in range(width):
        if MAP[row][col] == 'L':
            land_list.append((row, col))

answer = 0

for land in land_list:
    # 육지 모든 점 마다 다! 돌아야할 것 같다.
    queue = deque()
    visited = [[0] * width for _ in range(height)]
    queue.append(land)
    visited[land[0]][land[1]] = 1

    while queue:
        now = queue.popleft()
        now_row, now_col = now[0], now[1]

        for d in range(4):
            next_row = now_row + dx[d]
            next_col = now_col + dy[d]

            if 0 <= next_row < height and 0 <= next_col < width:
                if MAP[next_row][next_col] == "L" and not visited[next_row][next_col]:
                    queue.append((next_row, next_col))
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    if answer < visited[next_row][next_col]:
                        answer = visited[next_row][next_col]

print(answer-1)


