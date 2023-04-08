DIR_NUM = 4
OFFICE = 1

# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

# 각 위치의 시원함의 정도를 관리합니다.
# 처음에는 전부 0입니다.
coolness = [[0] * n for _ in range(n)]

# 시원함을 mix할 때
# 동시에 일어나는 처리를
# 편하게 하기 위해 사용될 배열입니다.
temp = [[0] * n for _ in range(n)]

# dx, dy 순서를 상좌우하로 설정합니다.
# 입력으로 주어지는 숫자에 맞추며,
# 4에서 현재 방향을 뺏을 때, 반대 방향이 나오도록 설정한 것입니다.
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# 현재 위치 (x, y)에서 해당 방향으로
# 이동한다 했을 때 벽이 있는지를 나타냅니다.
# 3차원 배열
block = [[[False] * DIR_NUM for _ in range(n)] for _ in range(n)]

# 시원함을 전파할 시
# 한 에어컨에 대해
# 겹쳐서 퍼지는 경우를 막기 위해
# visited 배열을 사용합니다.
visited = [[False] * n for _ in range(n)]

# 현재까지 흐른 시간(분)을 나타냅니다.
elapsed_time = 0


# (x, y)가 격자 내에 있는지를 판단합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# (dx, dy) 값으로부터
# move_dir값을 추출해냅니다.
def rev_dir(x_diff, y_diff):
    for i, (dx, dy) in enumerate(zip(dxs, dys)):
        if dx == x_diff and dy == y_diff:
            return i

    return -1


# (x, y)위치에서 move_dir 방향으로
# power 만큼의 시원함을 만들어줍니다.
# 이는 그 다음 칸에게도 영향을 끼칩니다.
def spread(x, y, move_dir, power):
    # power가 0이 되면 전파를 멈춥니다.
    if power == 0:
        return

    # 방문 체크를 하고, 해당 위치에 power를 더해줍니다.
    visited[x][y] = True
    coolness[x][y] += power

    # Case 1. 직진하여 전파되는 경우입니다.
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny) and not visited[nx][ny] and not block[x][y][move_dir]:
        spread(nx, ny, move_dir, power - 1)

    # Case 2. 대각선 방향으로 전파되는 경우입니다.
    if dxs[move_dir] == 0:
        # 현재 방향이 row 변동이 없는 경우 => 수평 이동(좌=1,우=2)
        for nx in [x + 1, x - 1]: # 다음 열의 위,중간,아래 를 봐야함.
            ny = y + dys[move_dir]  # 좌, 우 방향에 맞춰 열 이동
            # 꺾여 들어가는 곳에 전부 벽이 없는 경우에만 전파가 가능합니다.
            if in_range(nx, ny) and not visited[nx][ny] and \
                    not block[x][y][rev_dir(nx - x, 0)] and not block[nx][y][move_dir]:
                spread(nx, ny, move_dir, power - 1)

    else:
        # 현재 방향이 row 변동이 있는 경우 => 수직 이동(상=0,하=3)
        for ny in [y + 1, y - 1]:  # 아래 or 위 칸의 양 옆
            nx = x + dxs[move_dir]  # 아래 or 위
            # 꺾여 들어가는 곳에 전부 벽이 없는 경우에만 전파가 가능합니다.
            if in_range(nx, ny) and not visited[nx][ny] and \
                    not block[x][y][rev_dir(0, ny - y)] and not block[x][ny][move_dir]:
                # rev_dir(0, ny-y) 하면 (0, -1) 또는 (0, 1)이 나와서 좌(1) 우(2)가 나온다.
                # (x, y)에서 좌, 우 방향에 벽이 있는지 보는건 이해 완료
                # (x, ny)는 같은 줄의 양옆이고, 진행 방향으로 보면 벽이 막혀있는지 볼 수 있다.
                spread(nx, ny, move_dir, power - 1)


def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


# 에어컨에서 시원함을 발산합니다.
def blow():
    # 각 에어컨에 대해
    # 시원함을 발산합니다.
    for x in range(n):
        for y in range(n):
            # 에어컨에 대해
            # 해당 방향으로 시원함을
            # 만들어줍니다.
            if grid[x][y] >= 2:
                # move_dir = 에어컨 방향(상,좌,우,하)
                move_dir = (3 - grid[x][y]) if grid[x][y] <= 3 \
                    else (grid[x][y] - 2)

                nx, ny = x + dxs[move_dir], y + dys[move_dir]

                # 전파 전에 visited 값을 초기화해줍니다.
                clear_visited()
                # 세기 5에서 시작하여 계속 전파합니다.
                spread(nx, ny, move_dir, 5)


# (x, y) 위치는
# mix된 이후 시원함이
# 얼마가 되는지를 계산해줍니다.
def get_mixed_coolness(x, y):
    remaining_c = coolness[x][y]
    for i, (dx, dy) in enumerate(zip(dxs, dys)):
        nx, ny = x + dx, y + dy
        # 사이에 벽이 존재하지 않는 경우에만 mix가 일어납니다.
        if in_range(nx, ny) and not block[x][y][i]:
            # 현재의 시원함이 더 크다면, 그 차이를 4로 나눈 값 만큼 빠져나갑니다.
            if coolness[x][y] > coolness[nx][ny]:
                remaining_c -= (coolness[x][y] - coolness[nx][ny]) // 4
            # 그렇지 않다면, 반대로 그 차이를 4로 나눈 값만큼 받아오게 됩니다.
            else:
                remaining_c += (coolness[nx][ny] - coolness[x][y]) // 4

    return remaining_c


# 시원함이 mix됩니다.
def mix():
    # temp 배열을 초기화 해줍니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0

    # 각 칸마다 시원함이 mix된 이후의 결과를 받아옵니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = get_mixed_coolness(i, j)

    # temp 값을 coolness 배열에 다시 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            coolness[i][j] = temp[i][j]


# 외벽에 해당하는 칸인지를 판단합니다.
def is_outer_wall(x, y):
    return x == 0 or x == n - 1 or y == 0 or y == n - 1


# 외벽과 인접한 칸 중
# 시원함이 있는 곳에 대해서만
# 1만큼 시원함을 하락시킵니다.
def drop():
    for i in range(n):
        for j in range(n):
            if is_outer_wall(i, j) and coolness[i][j] > 0:
                coolness[i][j] -= 1


# 시원함이 생기는 과정을 반복합니다.
def simulate():
    global elapsed_time

    # Step1. 에어컨에서 시원함을 발산합니다.
    blow()

    # Step2. 시원함이 mix됩니다.
    mix()

    # Step3. 외벽과 인접한 칸의 시원함이 떨어집니다.
    drop()

    # 시간이 1분씩 증가합니다.
    elapsed_time += 1


# 종료해야 할 순간인지를 판단합니다.
# 모든 사무실의 시원함의 정도가 k 이상이거나,
# 흐른 시간이 100분을 넘게 되는지를 살펴봅니다.
def end():
    # 100분이 넘게 되면 종료해야 합니다.
    if elapsed_time > 100:
        return True

    # 사무실 중에
    # 시원함의 정도가 k 미만인 곳이
    # 단 하나라도 있으면, 아직 끝내면 안됩니다.
    for i in range(n):
        for j in range(n):
            if grid[i][j] == OFFICE and \
                    coolness[i][j] < k:
                return False

    # 모두 k 이상이므로, 종료해야 합니다.
    return True

# 벽 입력 처리
for _ in range(m):
    bx, by, bdir = tuple(map(int, input().split()))
    bx -= 1
    by -= 1

    # 현재 위치 (bx, by)에서
    # bdir 방향으로 나아가려고 했을 때
    # 벽이 있음을 표시해줍니다.
    block[bx][by][bdir] = True

    nx, ny = bx + dxs[bdir], by + dys[bdir]
    # 격자를 벗어나지 않는 칸과 벽을 사이에 두고 있다면,
    # 해당 칸에서 반대 방향(3-bdir)으로 진입하려고 할 때도
    # 벽이 있음을 표시해줍니다.
    if in_range(nx, ny):
        block[nx][ny][3 - bdir] = True

# 종료조건이 만족되기 전까지
# 계속 시뮬레이션을 반복합니다.
while not end():
    simulate()

# 출력:
if elapsed_time <= 100:
    print(elapsed_time)
else:
    print(-1)