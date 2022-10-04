n, m, k, c = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(n))
answer = 0

# 상하좌우
mr = [-1, 1, 0, 0]
mc = [0, 0, -1, 1]

# 대각선 ↖,↗,↙,↘
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]


# 음수를 제초제 값으로 쓰기 위해 문자로 바꿈
for _r in range(n):
    for _c in range(n):
        if grid[_r][_c] == -1:
            grid[_r][_c] = 'w'


def tree_print():
    for line in grid:
        for value in line:
            print(f"{value:>5}", end="")
        print()


def tree_grow():
    # 모든 위치를 돌며 주위에 나무 수를 세고, 그만큼 성장한다.
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 'w' or grid[row][col] <= 0:
                continue
            neighbor_trees = 0
            for d in range(4):
                n_row = row + mr[d]
                n_col = col + mc[d]

                if 0 > n_row or n <= n_row or 0 > n_col or n <= n_col:
                    continue
                if grid[n_row][n_col] == 'w' or grid[n_row][n_col] <= 0:
                    continue
                neighbor_trees += 1

            grid[row][col] += neighbor_trees


def tree_breed():
    breed_tree = [[0] * n for _ in range(n)]

    # 나무 번식 진행
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 'w' or grid[row][col] <= 0:
                continue
            # 해당 위치에서 주변에 빈칸인 곳 저장
            around_empty = []
            for d in range(4):
                n_row = row + mr[d]
                n_col = col + mc[d]

                if 0 > n_row or n <= n_row or 0 > n_col or n <= n_col:
                    continue
                # 빈칸이 아니라면 번식할 수 없다.
                if grid[n_row][n_col] == 0:
                    around_empty.append((n_row, n_col))

            if not around_empty:
                continue
            around_empty_cnt = len(around_empty)
            divide_cnt = grid[row][col] // around_empty_cnt

            for e_row, e_col in around_empty:
                breed_tree[e_row][e_col] += divide_cnt

    # 번식된 나무 반영
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 'w':
                continue
            grid[row][col] += breed_tree[row][col]


def tree_kill():
    global answer
    # 가장 많은 나무를 죽이게 되는 개수, 위치
    max_kill_cnt = 0
    kill_row, kill_col = 0, 0

    for row in range(n):
        for col in range(n):
            # 벽이나 빈곳에는 제초제를 뿌릴 생각 안함
            if grid[row][col] == 'w' or grid[row][col] <= 0:
                continue
            kill_cnt = grid[row][col]
            for d in range(4):
                for step in range(1, k+1):
                    n_row = row + dr[d] * step
                    n_col = col + dc[d] * step
                    # 맵을 벗어난 경우
                    if 0 > n_row or n <= n_row or 0 > n_col or n <= n_col:
                        break
                    # 벽이거나 빈 곳이면 거기까지만
                    if grid[n_row][n_col] == 'w' or grid[n_row][n_col] <= 0:
                        break
                    kill_cnt += grid[n_row][n_col]

            if max_kill_cnt < kill_cnt:
                max_kill_cnt = kill_cnt
                kill_row, kill_col = row, col

    # 해당 위치 기준으로 제초제 뿌리기
    # 그 위치에 나무가 없는 경우 해당 위치에만 제초제를 뿌려야함.
    answer += max_kill_cnt
    if grid[kill_row][kill_col]:
        grid[kill_row][kill_col] = -c
        for d in range(4):
            for step in range(1, k+1):
                k_row = kill_row + dr[d] * step
                k_col = kill_col + dc[d] * step
                if 0 <= k_row < n and 0 <= k_col < n:
                    value = grid[k_row][k_col]
                    if value == 'w':
                        break
                    grid[k_row][k_col] = -c
                    # 아니 문제 설명이 좀 이상한것 같음....
                    if value <= 0:
                        break


def tree_heal():
    for row in range(n):
        for col in range(n):
            # 벽이 아니고, 제초제가 뿌려져서 음수 값인 경우
            if grid[row][col] != 'w' and grid[row][col] < 0:
                grid[row][col] += 1

# print("===========초기화============")
# tree_print()

for _ in range(m):
    tree_grow()
    # print("===========나무성장============")
    # tree_print()
    tree_breed()
    # print("=========== 나무번식 =============")
    # tree_print()
    tree_heal()
    tree_kill()
    # print("========== 제초제 뿌림 ======")
    # tree_print()

print(answer)