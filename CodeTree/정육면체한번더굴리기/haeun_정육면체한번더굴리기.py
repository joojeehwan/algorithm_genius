"""
풀이시간 : 57분 42초
"""

from collections import deque

N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
answer = 0

# 우 상 좌 하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# 주사위 정보
dice = [[0, 1, 0],
        [4, 2, 3],
        [0, 6, 0],
        [0, 5, 0]]

# 주사위 행, 열, 방향
d_row, d_col, d_dir = 0, 0, 0


def print_dice():
    print("주사위")
    for line in dice:
        print(*line)


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def roll_right():
    new_dice = [[0, 0, 0] for _ in range(4)]

    # 유지
    new_dice[1][1], new_dice[3][1] = dice[1][1], dice[3][1]

    # 이동
    for r, c in [(0, 1), (1, 2), (2, 1), (1, 0)]:
        new_dice[c][2 - r] = dice[r][c]

    # 복사
    for r in range(4):
        dice[r] = new_dice[r]


def roll_left():
    new_dice = [[0, 0, 0] for _ in range(4)]

    # 유지
    new_dice[1][1], new_dice[3][1] = dice[1][1], dice[3][1]

    # 이동
    for r, c in [(0, 1), (1, 2), (2, 1), (1, 0)]:
        new_dice[2 - c][r] = dice[r][c]

    # 복사
    for r in range(4):
        dice[r] = new_dice[r]


def roll_up():
    temp = dice[0][1]
    for r in range(4):
        temp, dice[3 - r][1] = dice[3 - r][1], temp


def roll_down():
    temp = dice[0][1]
    for r in range(4):
        temp, dice[(r + 1) % 4][1] = dice[(r + 1) % 4][1], temp


def move():
    global d_row, d_col, d_dir

    # 다음 위치가 반대면 방향 바꾸기
    if not in_range(d_row + dr[d_dir], d_col + dc[d_dir]):
        d_dir = (d_dir + 2) % 4

    d_row += dr[d_dir]
    d_col += dc[d_dir]

    # 바라보는 면 바뀜
    if d_dir == 0:
        roll_right()
    elif d_dir == 1:
        roll_up()
    elif d_dir == 2:
        roll_left()
    elif d_dir == 3:
        roll_down()


# 격자 점수 얻기
def score():
    global answer
    visited = [[False] * N for _ in range(N)]
    q = deque()
    num = grid[d_row][d_col]

    q.append((d_row, d_col))
    visited[d_row][d_col] = True
    cnt = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not in_range(nr, nc):
                continue
            if grid[nr][nc] != num:
                continue
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            q.append((nr, nc))
            cnt += 1

    answer += num * cnt


def cal_direction():
    global d_dir
    # 주사위 아랫면
    dice_num = dice[2][1]

    # 주사위 위치 숫자
    grid_num = grid[d_row][d_col]

    if dice_num > grid_num:
        # 90도 시계방향 = 우 하 좌 상
        d_dir = (d_dir - 1) % 4
    elif dice_num < grid_num:
        # 90도 반시계방향 = 우 상 좌 하
        d_dir = (d_dir + 1) % 4


def solution():
    for _ in range(M):
        move()  # 주사위 움직임
        score()  # 격자판 점수 얻기
        cal_direction()  # 방향 전환

    print(answer)

solution()
