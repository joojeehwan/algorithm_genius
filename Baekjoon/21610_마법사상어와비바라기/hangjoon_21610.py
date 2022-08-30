import sys
from collections import deque


def move_clouds(move, clouds):
    move_d, move_s = move
    move_row, move_col = DIRECTION[move_d]
    cf = [[0] * size for _ in range(size)]  # 기존 구름의 위치 저장용
    for _ in range(len(clouds)):
        cloud = clouds.popleft()
        new_row, new_col = (cloud[0] + move_s * move_row) % size, (cloud[1] + move_s * move_col) % size
        clouds.append((new_row, new_col))
        cf[new_row][new_col] = 1
    return cf


def water_bug(c_row, c_col):
    cnt = 0  # 주변 물 바구니 수
    for dr, dc in M_DIRECTION:
        new_row, new_col = c_row + dr, c_col + dc
        if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size:  # 맵 밖임
            continue
        if not field[new_row][new_col]:  # 바구니에 물이 없음
            continue
        cnt += 1
    field[c_row][c_col] += cnt


def make_clouds(size, cloud_field):
    new_clouds = deque()
    for row in range(size):
        for col in range(size):
            if field[row][col] >= 2 and not cloud_field[row][col]:  # 구름이 없었던 곳 + 물이 2 이상
                new_clouds.append((row, col))
                field[row][col] -= 2
    return new_clouds


size, moves = map(int, sys.stdin.readline().split())  # 격자 크기, 이동 횟수
field = [[] for _ in range(size)]  # 맵 정보 (바구니에 저장되어 있는 물의 양)
for row in range(size):
    field[row] = list(map(int, sys.stdin.readline().split()))
move_lst = []  # 이동 정보 (방향, 거리)
for i in range(moves):
    move_lst.append(tuple(map(int, sys.stdin.readline().split())))
DIRECTION = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  # 방향 정보에 따른 이동 방향

# 0. 비바라기 시전
clouds = deque([(size - 1, 0), (size - 1, 1), (size - 2, 0), (size - 2, 1)])  # 구름 위치 정보

for move in move_lst:
    # 1. 구름 이동 + 비 내리기
    cloud_field = move_clouds(move, clouds)

    # 2. 비 내리기
    for c_row, c_col in clouds:
        field[c_row][c_col] += 1

    # 3. 물복사 버그 마법
    M_DIRECTION = [(-1, -1), (-1, 1), (1, 1), (1, -1)]  # 마법을 위한 확인용 대각선 방향
    for c_row, c_col in clouds:
        water_bug(c_row, c_col)

    # 4. 구름 생성
    clouds = make_clouds(size, cloud_field)

# 물 양 계산
ans = 0
for row in field:
    ans += sum(row)
print(ans)