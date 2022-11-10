'''

"매주 삼성 기출 하나씩 풀기" 프로젝트
11/7 - 12


어?! 이 문제 그건데?!

마법사상어와 블리자드?!

이거 문제 풀이 한번 읽어보고, 다시 풀어보자

'''


# 코드 트리 답변

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

spiral_points = list()

ans = 0


def search_spiral():
    # 나선이 돌아가는 순서대로
    # 왼쪽 아래 오른쪽 위 방향이 되도록 정의합니다.
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

    # 시작 위치와 방향,
    # 해당 방향으로 이동할 횟수를 설정합니다.
    curr_x, curr_y = n // 2, n // 2
    move_dir, move_num = 0, 1

    while curr_x or curr_y:
        # move_num 만큼 이동합니다.
        for _ in range(move_num):
            curr_x += dxs[move_dir]
            curr_y += dys[move_dir]
            spiral_points.append((curr_x, curr_y))

            # 이동하는 도중 (0, 0)으로 오게 되면,
            # 움직이는 것을 종료합니다.
            if not curr_x and not curr_y:
                break

        # 방향을 바꿉니다.
        move_dir = (move_dir + 1) % 4
        # 만약 현재 방향이 왼쪽 혹은 오른쪽이 된 경우에는
        # 특정 방향으로 움직여야 할 횟수를 1 증가시킵니다.
        if move_dir == 0 or move_dir == 2:
            move_num += 1


def pull():
    # Step 1. temp 배열을 초기화합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0

    # Step2. 나선 순서대로 보며
    #        비어있지 않은 값들을 temp에 채워줍니다.
    temp_idx = 0
    for gx, gy in spiral_points:
        if grid[gx][gy]:
            tx, ty = spiral_points[temp_idx]
            temp[tx][ty] = grid[gx][gy]
            temp_idx += 1

    # Step 3. temp 값을 다시 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def attack(d, p):
    global ans

    # 문제에서 주어진 순서대로 → ↓ ← ↑
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # Step 1. d 방향으로 p마리의 몬스터를 제거합니다.
    center_x, center_y = n // 2, n // 2
    for dist in range(1, p + 1):
        nx = center_x + dxs[d] * dist
        ny = center_y + dys[d] * dist

        ans += grid[nx][ny]
        grid[nx][ny] = 0

    # Step2. 비어 있는 자리를 당겨서 채워줍니다.
    pull()


def get_num_by_spiral_idx(spiral_idx):
    x, y = spiral_points[spiral_idx]
    return grid[x][y]


# start_idx로부터 연속하여 같은 숫자로 이루어져 있는
# 가장 끝 index를 찾아 반환합니다.
def get_end_idx_of_same_num(start_idx):
    end_idx = start_idx + 1
    curr_num = get_num_by_spiral_idx(start_idx)
    end_of_array = len(spiral_points)

    while end_idx < end_of_array:
        if get_num_by_spiral_idx(end_idx) == curr_num:
            end_idx += 1
        else:
            break

    return end_idx - 1


def remove(start_idx, end_idx):
    global ans

    for i in range(start_idx, end_idx + 1):
        x, y = spiral_points[i]
        ans += grid[x][y]
        grid[x][y] = 0


# 4번 이상 반복하여 나오는 구간을 지워줍니다.
def bomb():
    did_explode = False
    curr_idx = 0
    end_of_array = len(spiral_points)

    while curr_idx < end_of_array:
        end_idx = get_end_idx_of_same_num(curr_idx)
        curr_num = get_num_by_spiral_idx(curr_idx)

        # 맨 끝에 도달하게 되면, 더이상 진행하지 않습니다.
        if curr_num == 0:
            break

        if end_idx - curr_idx + 1 >= 4:
            # 연속한 숫자의 개수가 4개 이상이면
            # 해당 구간을 지워줍니다.
            remove(curr_idx, end_idx)
            did_explode = True

        # 그 다음 구간의 시작값으로 변경해줍니다.
        curr_idx = end_idx + 1

    return did_explode


# 4번 이상 반복하여 나오는 구간을 계속 지워줍니다.
def organize():
    while True:
        # 4번 이상 나오는 구간을 터뜨려봅니다.
        keep_going = bomb()

        if not keep_going:
            break

        # 지운 이후에는 다시 당겨서 채워줍니다.
        pull()


def look_and_say():
    # Step 1. temp 배열을 초기화합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0

    # Step2. 보고 말하며 temp에 해당 값을 기록합니다.
    temp_idx = 0
    curr_idx = 0
    end_of_array = len(spiral_points)

    while curr_idx < end_of_array:
        end_idx = get_end_idx_of_same_num(curr_idx)

        # 연속하여 나온 숫자의 개수와 숫자 종류 값을 계산합니다.
        contiguous_cnt = end_idx - curr_idx + 1
        curr_num = get_num_by_spiral_idx(curr_idx)

        # 맨 끝에 도달하게 되면, 더이상 진행하지 않습니다.
        if curr_num == 0:
            break

        # temp에 (개수, 종류) 순서대로 기록해줍니다.
        # 만약 격자를 벗어나면 종료합니다.
        if temp_idx >= end_of_array:
            break

        tx, ty = spiral_points[temp_idx]
        temp[tx][ty] = contiguous_cnt
        temp_idx += 1

        if temp_idx >= end_of_array:
            break

        tx, ty = spiral_points[temp_idx]
        temp[tx][ty] = curr_num
        temp_idx += 1

        # 그 다음 구간의 시작값으로 변경해줍니다.
        curr_idx = end_idx + 1

    # Step 3. temp 값을 다시 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def simulate(d, p):
    # Step 1. 공격하여 몬스터를 제거합니다.
    attack(d, p)

    # Step 2. 4번 이상 반복하여 나오는 구간을 계속 지워줍니다.
    organize()

    # Step 3. 보고 말하기 행동을 진행합니다.
    look_and_say()


# 중심 탑을 기준으로 나선 모양으로 회전했을 때
# 지나게 되는 위치의 좌표들을 순서대로 기록해 놓습니다.
search_spiral()

# m번에 걸쳐 시뮬레이션을 진행합니다.
for _ in range(m):
    d, p = tuple(map(int, input().split()))

    simulate(d, p)

print(ans)