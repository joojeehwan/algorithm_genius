from collections import deque
import sys


def rotate(lst, size):
    new_lst = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            new_lst[col][size - row - 1] = lst[row][col]
    return new_lst


size, firestorms = map(int, sys.stdin.readline().split())  # 격자 크기, 파이어스톰 수
size = 2 ** size
field = [[] for _ in range(size)]  # 격자 상태
for row in range(size):
    field[row] = list(map(int, sys.stdin.readline().split()))
levels = list(map(int, sys.stdin.readline().split()))  # 파이어스톰 단계 리스트

for level in levels:
    window_size = 2 ** level  # 부분 격자 크기
    new_field = [[] for _ in range(size)]  # 회전한 후의 새로운 격자
    for row in range(0, size, window_size):
        for col in range(0, size, window_size):
            # 1. 구역 나누기
            temp = []
            for r in range(window_size):
                temp.append(field[row + r][col: col + window_size])

            # 2. 회전하기
            for r in range(window_size):
                for c in range(window_size):
                    field[row + c][col + window_size - r - 1] = temp[r][c]

    # 3. 얼음 녹이기
    melting = [[0] * size for _ in range(size)]  # 녹을 좌표 리스트
    for row in range(size):
        for col in range(size):
            cnt = 0  # 인접한 얼음 수
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if row + dr < 0 or row + dr >= size or col + dc < 0 or col + dc >= size:  # 맵 밖임
                    continue
                if field[row + dr][col + dc]:  # 얼음이 있으면
                    cnt += 1
            if cnt < 3:
                melting[row][col] = 1
    for row in range(size):
        for col in range(size):
            if melting[row][col]:
                field[row][col] = max(0, field[row][col] - 1)

all_ice = 0  # 남아있는 얼음의 합
biggest_size = 0  # 남아있는 얼음 중 가장 큰 덩어리의 크기
visited = [[0] * size for _ in range(size)]
# BFS
for row in range(size):
    for col in range(size):
        if not visited[row][col] and field[row][col]:
            queue = deque()
            queue.append((row, col))
            cnt = 0  # 이 덩어리의 크기
            while queue:
                now_r, now_c = queue.popleft()
                visited[now_r][now_c] = 1
                all_ice += field[now_r][now_c]
                cnt += 1
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_r, new_c = now_r + dr, now_c + dc
                    if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:  # 맵 밖임
                        continue
                    if visited[new_r][new_c]:  # 이미 방문함
                        continue
                    if not field[new_r][new_c]:  # 얼음이 아님
                        continue
                    queue.append((new_r, new_c))
                    visited[new_r][new_c] = 1
            biggest_size = max(biggest_size, cnt)
print(all_ice)
print(biggest_size)