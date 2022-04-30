"""
문제 읽으면서부터 머리 깨질 것 같았음
걸린시간 : 4시간 30분
메모리 : 30840
시간 : 940ms

중간에 포기하고싶었음
"""

chocolate = 0
finish = False
# 행, 열, 원하는 목표 온도
R, C, K = map(int, input().split())

# 방의 정보
room = list(list(map(int, input().split())) for _ in range(R))
heaters = []
check_points = []
for r in range(R):
    for c in range(C):
        num = room[r][c]
        if 1 <= num <= 4:
            heaters.append((r, c, num-1))
        elif num == 5:
            check_points.append((r, c))
        # 저장해놨으니 원본 필요 X 여기다가 온도계산 할거임
        room[r][c] = 0

# 히터의 방향에 따른 델타배열 오 / 왼 / 위 / 아
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 우좌상하 순서
# 오른쪽을 예시로 (바로 오른쪽위치와 있으면 안되는 벽) (바로 위 + 위에서오른쪽) (아래 + 아래에서오른쪽)
reachable = (
                (((0, 0, 1),), ((0, 0, 0), (-1, 0, 1)), ((1, 0, 0), (1, 0, 1))),
                (((0, -1, 1),), ((0, 0, 0), (-1, -1, 1)), ((1, 0, 0), (1, -1, 1))),
                (((0, 0, 0),), ((0, -1, 0), (0, -1, 1)), ((0, 0, 1), (0, 1, 0))),
                (((1, 0, 0),), ((0, -1, 1), (1, -1, 0)), ((0, 0, 1), (1, 1, 0))),
)

# 1자리당 3자리씩 볼 수 있다. 그때 우자상하 순서로 갈 수 있는 곳들 delta배열
delta = (
    ((0, 1), (-1, 1), (1, 1)),
    ((0, -1), (-1, -1), (1, -1)),
    ((-1, 0), (-1, -1), (-1, 1)),
    ((1, 0), (1, -1), (1, 1)),
)

# 온도 흩뿌릴때 오른쪽이랑 아래만 볼려고
temp_dr = [0, 1]
temp_dc = [1, 0]

# 벽의 정보
W = int(input())
walls = dict()

for _ in range(W):
    # 행, 열, 벽의 여부(0이면 윗줄에, 1이면 오른쪽에 벽)
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    if walls.get((x, y)):
        walls[(x, y)].append(t)
    else:
        walls[(x, y)] = [t]

# 대각선 2개랑 바로 붙어있는곳 갈 수 있는지 보기
def check_route(row, col, direction):
    next_pos = set()
    # 오른쪽 기준으로 (오른쪽), (위 + 위오른쪽), (아래 + 아래오른쪽)을 본다.
    for i in range(3):
        check_walls = reachable[direction][i]
        # 대각선의 경우 2번 다 봐야하기 때문에 check_wall = (row델타, col델타, 막히면 안되는 벽 타입)
        blocked = 0
        for check_row, check_col, wall_type in check_walls:
            # 대각선의 경우 2번 다 봐서 막혔는지 보려고
            # row델타, col델타, 막히면 안되는 벽 타입
            next_row, next_col = row + check_row, col + check_col
            # 그 위치에 그 벽타입이 없어야 하지만, 있다면 blocked 추가
            if walls.get((next_row, next_col)):
                if wall_type in walls.get((next_row, next_col)):
                    blocked += 1
            # 그 위치에 갈 수도 있으니까 어딘지 저장해야됨 ㅠㅠ 바로 옆인지 어느 대각선인지 지금은 모르니까
        # 1번이라도 막혔으면 거긴 못간다.
        if not blocked:
            # 중복으로 갈 수 있으니까 set로 처리
            new_row, new_col = row + delta[direction][i][0], col+ delta[direction][i][1]
            if 0 <= new_row < R and 0 <= new_col < C:
                next_pos.add((new_row, new_col))

    return next_pos


# 바람이 나온다
def heater_wind():
    for h_row, h_col, h_dir in heaters:
        # 항상 히터 방향의 젤 처음 위치에는 5가 추가됨
        row, col = h_row+dr[h_dir], h_col+dc[h_dir]
        room[row][col] += 5

        # 최대 3개가 담긴 set
        next_pos = check_route(row, col, h_dir)

        for step in range(4):
            new_next_pos = set()
            for next_row, next_col in next_pos:
                room[next_row][next_col] += 4 - step
                found_nexts = check_route(next_row, next_col, h_dir)
                for found in found_nexts:
                    new_next_pos.add(found)
            next_pos = new_next_pos

# 온도를 조절한다
def mix_temperature():
    differences = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            now_num = room[r][c]
            for d in range(2):
                # 오른쪽 또는 아래
                next_row, next_col = r + temp_dr[d], c + temp_dc[d]
                # 벽에 막힌 경우(오른쪽이다)
                if d == 0:
                    if walls.get((r, c)) and 1 in walls.get((r, c)):
                        continue
                # 벽에 막힌 경우(아래다)
                if d == 1:
                    if walls.get((r+1, c)) and 0 in walls.get((r+1, c)):
                        continue
                # 범위 내인 경우
                if next_row < R and next_col < C:
                    next_num = room[next_row][next_col]
                    if now_num > next_num:
                        diff = (now_num - next_num) // 4
                        differences[r][c] -= diff
                        differences[next_row][next_col] += diff
                    else:
                        diff = (next_num - now_num) // 4
                        differences[r][c] += diff
                        differences[next_row][next_col] -= diff

    # 차이를 적용한다.
    for row in range(R):
        for col in range(C):
            room[row][col] += differences[row][col]


# 가장자리 온도 1 감소한다
def edge_temp_down():
    for r in range(R):
        if r == 0 or r == R-1:
            for c in range(C):
                if room[r][c]:
                    room[r][c] -= 1
        else:
            if room[r][0]:
                room[r][0] -= 1
            if room[r][C-1]:
                room[r][C-1] -= 1

# 체크포인트 검사해라
def check():
    for row, col in check_points:
        if room[row][col] < K:
            return False
    return True


while not finish:
    if chocolate > 100:
        chocolate = 101
        break
    heater_wind()
    mix_temperature()
    edge_temp_down()
    chocolate += 1
    finish = check()

print(chocolate)
