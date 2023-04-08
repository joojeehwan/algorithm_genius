from copy import deepcopy

N = 4
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


_grid = [[0] * 4 for _ in range(N)]
# 물고기의 row, col, direction
_fish = [[0, 0, 0] for _ in range(N ** 2 + 1)]
answer = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(0, 2*N, 2):
        num, d = line[j], line[j+1]-1
        _fish[num] = [i, j//2, d]
        _grid[i][j//2] = num


def print_grid(grid):
    print("############# 그리드 출력 ##########")
    for line in grid:
        print(*line)

def print_fish(fish):
    print("%%%%%%%%%%% 물고기 출력 %%%%%%%%%%")
    for i in range(1, 17):
        print(i, fish[i])


def move(s_row, s_col, score, fish, grid):
    global answer

    eaten_fish = grid[s_row][s_col]
    score += eaten_fish
    answer = max(answer, score)
    s_dir = fish[eaten_fish][2]
    fish[eaten_fish] = []
    grid[s_row][s_col] = 0

    # 물고기가 이동한다.
    for f_idx in range(1, 17):
        if not fish[f_idx]:
            continue
        f_row, f_col, f_dir = fish[f_idx]

        # 8방향을 돌면서
        for d in range(8):
            # 가능한 방향을 찾는다.
            new_dir = (f_dir + d) % 8
            new_row = f_row + dr[new_dir]
            new_col = f_col + dc[new_dir]
            if not (0 <= new_row < N and 0 <= new_col < N):
                continue
            if new_row == s_row and new_col == s_col:  # 상어 있음
                continue
            # 방향 업데이트
            swap_idx = grid[new_row][new_col]
            fish[f_idx] = [new_row, new_col, new_dir]
            fish[swap_idx] = [f_row, f_col, fish[swap_idx][2]]
            grid[new_row][new_col], grid[f_row][f_col] = grid[f_row][f_col],  grid[new_row][new_col]
            break

    # 상어가 이동해야한다.
    for step in range(1, 4):
        possible_r = s_row + dr[s_dir] * step
        possible_c = s_col + dc[s_dir] * step

        # 범위를 벗어나도 안됨
        if not(0 <= possible_r < N and 0 <= possible_c < N):
            continue
        # 물고기가 없으면 안됨
        if grid[possible_r][possible_c] == 0:
            continue
        move(possible_r, possible_c, score, deepcopy(fish), deepcopy(grid))


move(0, 0, 0, _fish, _grid)
print(answer)