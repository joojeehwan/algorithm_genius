from copy import deepcopy

N = 4
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


init_grid = [[0] * 4 for _ in range(N)]
# 물고기의 row, col, direction
init_fish_stock = [[0, 0, 0] for _ in range(N ** 2 + 1)]
init_shark_r, init_shark_c, init_shark_d = 0, 0, 0
answer = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(0, 2*N, 2):
        num, d = line[j], line[j+1]-1
        init_fish_stock[num] = [i, j//2, d]
        init_grid[i][j//2] = num

# 처음에 상어가 (0, 0)에 있는 물고기를 먹는다.
init_num = init_grid[0][0]
init_shark_d = init_fish_stock[init_num][2]
answer += init_num
init_grid[0][0] = -1 # 상어는 -1
init_fish_stock[init_num] = []


def print_grid(grid):
    print("############# 그리드 출력 ##########")
    for line in grid:
        print(*line)

def print_fish(fish):
    print("%%%%%%%%%%% 물고기 출력 %%%%%%%%%%")
    for i in range(1, 17):
        print(i, fish[i])


def in_range(x, y, grid):
    if not (0 <= x < N and 0 <= y < N):
        # 범위 밖
        return False
    if grid[x][y] == -1:
        # 상어 있음
        return False
    return True



def fish_move(fish, grid):
    # 물고기 번호 순으로 이동
    now_grid = deepcopy(grid)
    now_fish = deepcopy(fish)
    for f_idx in range(1, 17):
        if not now_fish[f_idx]:
            continue
        row, col, drct = now_fish[f_idx]

        # 8방향을 돌면서
        for d in range(8):
            # 가능한 방향을 찾는다.
            new_dir = (drct + d) % 8
            new_row = row + dr[new_dir]
            new_col = col + dc[new_dir]
            if not in_range(new_row, new_col, now_grid):
                continue
            # 이동할 수 있다.
            # 다른 물고기가 있다면 위치를 바꿔주어야함
            if now_grid[new_row][new_col]:
                original_fish = now_grid[new_row][new_col]
                now_grid[row][col] = original_fish
                now_fish[original_fish] = [row, col, now_fish[original_fish][2]]
            else:
                now_grid[row][col] = 0
            now_grid[new_row][new_col] = f_idx
            # 위치, 방향 업데이트
            now_fish[f_idx] = [new_row, new_col, new_dir]
            break
    return now_fish, now_grid



def move(fish, grid, shark, eaten):
    global answer
    # 물고기가 이동한다.
    now_fish_stock, now_grid = fish_move(fish, grid)
    # print("*********** 물고기 이동 완료 *************")
    # print_fish(now_fish_stock)
    # print_grid(now_grid)
    # 상어가 이동해야한다.
    shark_r, shark_c, shark_d = shark
    possible_pos = []
    for step in range(1, 4):
        possible_r = shark_r + dr[shark_d] * step
        possible_c = shark_c + dc[shark_d] * step

        # 범위를 벗어나도 안됨
        if not(0 <= possible_r < N and 0 <= possible_c < N):
            continue
        # 물고기가 없으면 안됨
        if now_grid[possible_r][possible_c] == 0:
            continue
        possible_pos.append((possible_r, possible_c))

    if possible_pos:
        # print("********* 상어 방향 : ", shark_d," 이동 시도 : ", possible_pos)

        # 가능한 곳이 있다!
        now_grid[shark_r][shark_c] = 0
        for p_row, p_col in possible_pos:
            # 물고기 먹음, 상어 여기있음
            fish_idx = now_grid[p_row][p_col]
            now_grid[p_row][p_col] = -1
            # 방향 업데이트함
            shark_d = now_fish_stock[fish_idx][2]
            eaten += fish_idx
            now_fish_stock[fish_idx] = []
            # print("$$$$$$$$ 갈 수 있는 곳 중 한군데로 갔음 $$$$$$$$$")
            # print_fish(now_fish_stock)
            # print_grid(now_grid)
            move(now_fish_stock, now_grid, [p_row, p_col, shark_d], eaten)

            # 원상복구
            now_grid[p_row][p_col] = fish_idx
            eaten -= fish_idx
            now_fish_stock[fish_idx] = [p_row, p_col, shark_d]

            # print("$$$$$$$$ 다시 원상복구 해놨음 $$$$$$$$$")
            # print_fish(now_fish_stock)
            # print_grid(now_grid)
    else:
        # 최대값 비교
        # print("상어 집으로 가래!! 정답 : ", answer, " & 지금까지 : ", eaten)
        answer = max(answer, eaten)
        return

# print(" ^^^^^^^^^^^ 초기 정보 출력 ^^^^^^^^^^")
# print_grid(init_grid)
# print_fish(init_fish_stock)

move(init_fish_stock, init_grid, [init_shark_r, init_shark_c, init_shark_d], init_num)
print(answer)