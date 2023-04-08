"""
바람이 이동하는 함수가 제일 어렵다.
[정답] 모든 사무실의 시원함이 k 이상이 되는 최소 시간(분). 100이 넘으면 -1을 출력한다.
[유의사항]
- 벽이 에어컨 바로 앞에 주어지는 경우는 없다.
- 벽이 외벽에 포함되는 경우는 없다.
- 에어컨 바로 앞이 격자를 벗어나는 경우는 없다.
- 사무실과 에어컨은 최소 1개씩 있다.
"""
from collections import deque
import math

N, M, K = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))  # 초기 정보. 1번 쓰고 버린다.
wall_list = list(list(map(int, input().split())) for _ in range(M))  # 벽 정보. 3차원 배열로 바꾼다. 0 => 위, 1 => 왼쪽

# 필요한 변수
answer = 0  # 100이 넘으면 -1이 되어야 한다.
air = []  # 에어컨 마다 (row, col, direction)을 저장한다. 고정
office = []  # 각 사무실의 좌표(row, col)를 저장한다. 고정
wall = [[[0] * 4 for _ in range(N)] for _ in range(N)]  # 각 좌표마다 [좌, 상, 우, 하] 에 벽이 있는지 체크한다. 고정
cool = [[0] * N for _ in range(N)]   # 가장 핵심 변수. 모든 변동은 여기서 일어난다.

# 입력값을 기준으로 새로 데이터를 가공한다.
for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            office.append((r, c))  # 사무실
        elif grid[r][c] > 1:
            air.append((r, c, grid[r][c] - 2))  # 방향을 0부터 시작하도록 맞춘다.

# 벽 처리
for r, c, d in wall_list:
    r -= 1  # 입력 1부터 시작 그만!!
    c -= 1
    if d == 0:
        # (r, c)의 위에 벽이 있다. 참고로 벽이 외벽에 있는 경우는 없으므로 벗어나는지 체크 안한다.
        wall[r][c][1] = wall[r-1][c][3] = 1
    else:
        # (r, c)의 왼쪽에 벽이 있다.
        wall[r][c][0] = wall[r][c-1][2] = 1

# 델타 (좌-상-우-하)
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def print_wall():
    print(" | | | | | | | | | |벽| | | | | | | | | | | |")
    for line in wall:
        for w in line:
            print(*w, end=" | ")
        print()
    print()


def print_cool():
    print(" ~ ~ ~ ~ ~ ~ 시~원~함 ~ ~ ~ ~ ~ ~ ")
    for c in cool:
        print(*c)
    print()


# 종료 확인 함수
# 모든 사무실의 시원함이 k 이상인지 확인한다.
def is_finish():
    for x, y in office:
        if cool[x][y] < K:
            return False
    return True


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


# delta의 차이를 통해 대각선 위치에 갈 수 있는지 판단할 때,
# 수직 이동일 경우 지금 좌, 우 인지
# 수평 이동일 경우 지금 상, 하 인지 판단.
def dia_dir(dx, dy):
    for d in range(4):
        if dx == dr[d] and dy == dc[d]:
            return d


# 한개의 위치당 3개의 위치에 갈 수 있는지 본다.
# 하드코딩...
def check(row, col, air_d):
    next_pos = []

    # 이 위치에서 에어컨 방향으로 바로 다음에 벽이 있는지와, 범위 체크 (직진)
    if not wall[row][col][air_d] and in_range(row+dr[air_d], col+dc[air_d]):
        next_pos.append([True, row+dr[air_d], col+dc[air_d]])
    else:
        next_pos.append([False])

    # 대각선 2 자리 가능한지 체크
    # air_d = [좌, 상, 우, 하]
    if air_d % 2 == 0:  # 에어컨 방향이 수평 이동인 경우
        n_col = col + dc[air_d]  # 다음 열로 넘어간건 2자리 모두 똑같다.
        for n_row in [row-1, row+1]:  # 다음 열의 위, 아래를 본다.
            if in_range(n_row, n_col) and not wall[row][col][dia_dir(n_row - row, 0)]\
                    and not wall[n_row][col][air_d]:
                next_pos.append([True, n_row, n_col])
            else:
                next_pos.append([False])
    else: # 에어컨 방향이 수직 이동인 경우
        n_row = row + dr[air_d]  # 다음 행으로 넘어간건 2자리 모두 똑같다.
        for n_col in [col - 1, col + 1]:  # 다음 행의 양 옆을 본다.
            if in_range(n_row, n_col) and not wall[row][col][dia_dir(0, n_col-col)] \
                    and not wall[row][n_col][air_d]:
                next_pos.append([True, n_row, n_col])
            else:
                next_pos.append([False])

    return next_pos


# 1. 모든 에어컨에서 바람이 나온다.(끝판왕)
def wind():
    plus = [[0] * N for _ in range(N)]  # 모든 에어컨의 결과를 저장할 배열이 필요하다.
    for ar, ac, ad in air:
        # 에어컨 바로 앞에 있는 위치이다.
        q = deque([(ar+dr[ad], ac+dc[ad], 5)])

        while q:
            r, c, v = q.popleft()
            plus[r][c] += v
            pos = check(r, c, ad)  # 한 위치당 3개의 위치를 본다.
            if v > 1:
                for p in pos:
                    if p[0] and (p[1], p[2], v-1) not in q:
                        q.append((p[1], p[2], v-1))

    for r in range(N):
        for c in range(N):
            cool[r][c] += plus[r][c]


# 2. 시원함이 '동시에' 섞인다.
def mix():
    res = [[0] * N for _ in range(N)]  # 섞인 결과

    for r in range(N):
        for c in range(N):
            v = cool[r][c]

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if not in_range(nr, nc):
                    continue
                if wall[r][c][d]:
                    continue
                nv = cool[nr][nc]
                diff = math.ceil(abs(v - nv) // 4)
                if nv > v:
                    # [체크!] diff를 (r,c)와 (nr,nc)에 둘 다 반영해주느라 visited 배열을 사용했는데
                    # 지금 내 위치에만 해준다면 굳이 필요 없다.
                    res[r][c] += diff
                else:
                    res[r][c] -= diff

    for r in range(N):
        for c in range(N):
            cool[r][c] += res[r][c]


def edge():
    for c in range(N):
        cool[0][c] = cool[0][c] - 1 if cool[0][c]-1 > 0 else 0
        cool[N-1][c] = cool[N-1][c] - 1 if cool[N-1][c]-1 > 0 else 0
    for r in range(1, N-1):
        cool[r][0] = cool[r][0] - 1 if cool[r][0]-1 > 0 else 0
        cool[r][N-1] = cool[r][N-1] - 1 if cool[r][N-1]-1 > 0 else 0





def solution():
    global answer
    # 종료 조건 => 모든 사무실의 시원함이 k 이상 OR 분이 100이 넘어감.
    while not is_finish():
        if answer >= 100:
            print(-1)
            return
        # 1. 모든 에어컨에서 바람이 나온다.
        wind()
        # 2. 시원함이 섞인다.
        mix()
        # 3. 외벽 칸의 시원함이 1씩 감소한다.
        edge()
        answer += 1
    print(answer)


solution()