'''

백준의 상어 중학교와 같은 문제,,

어떤식으로 풀었는지, 다시 한번 복기


'''


# 내 풀이

from collections import deque

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]



#델타 배열 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def calcPoint():

    point = 0
    max_area = []
    max_red = 0

    #색깔마다, bfs를 돌리기 위함. 각각의 색 모두 확인해야 하자나!
    for color in range(1, m + 1) :

        #다른 색깔마다 갱신
        visited = [[False] * 20 for _ in range(20)]
        for row in range(n):
            for col in range(n):
                if not visited[row][col] and MAP[row][col] == color:

                    q = deque
                    q.append((row, col))
                    #우선순위 결정을 위한 장치 => 여러가지 색중에서, 폭탄이 터진 범위가 같아질 때 판단을 해야 하자나. 그때를 위해, 폭탄이 터지는 (row, col)을 기록
                    result_lst = [[row, col]]
                    red = 0
                    visited[row][col] = True

                    while q:

                        now_row, now_col = q.popleft()

                        for dir in range(4):
                            next_row = now_row + dr[dir]
                            next_col = now_col + dc[dir]

                            #범위 체크
                            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                                continue

                            #방문하지 않은 곳, 갈 수 있는 곳(빨간색, 혹은 같은 색깔)
                            if not visited[next_row][next_col] and (MAP[next_row][next_col] == color or MAP[next_row][next_col] == 0):

                                q.append([next_row, next_col])
                                visited[next_row][next_col] = True
                                result_lst.append([next_row, next_col])
                                point += 1
                                if MAP[next_row][next_col] == 0:
                                    red += 1
                            # 가장 많이 인접해 있는, 숫자를 가지는 것을 기록하기 위함.
                            # 3가지 case 존재 모두 나열
                    if len(max_area) < len(result_lst) or (len(max_area) == len(result_lst) and max_red < red) or (len(max_area) == len(result_lst) and max_red == red and max_area[0] < result_lst[0]):
                        max_area = result_lst[:]
                        max_red = red

            # 2개 이상이 되지 않는 것은 counting 하지 않는다.
        if len(max_area) >= 2:
            point = len(max_area) * len(max_area)
            # 블록 제거
            for row, col in max_area:
                MAP[row][col] = -2
        return point

def gravity() :
    global MAP

    #각각의 column마다 확인할것.
    for col in range(n):
        blank = 0
        #아래에서 위로 올라간다.
        for row in range(n-1, -1, -1):
            #공백(-2)이면, 공백의 수 만큼 counting
            if MAP[row][col]  == -2 :
                blank += 1
            #검은색을 만나면, 다시 초기화
            elif MAP[row][col] == -1:
                blank = 0

            else:
                #옮기기, 공백의 수 만큼! 위에서 아래로 중력이 적용이 된다.
                if blank != 0 : #맨처음에 바로 들어오자마자, else문이 안타도록 하기 위함.
                    MAP[row + blank][col] = MAP[row][col]
                    MAP[row][col] = -2


#하은이가 알려준 중력방식..! 좋다

MAX_WIDTH = 3
bucket = [[]]
# 해설지에 있던 중력 적용 함수. 계산이 훨씬 쉬운 것 같다.
def gravity():
    # 변경된 값을 기존 배열에 복사붙여넣기 위해 만듬
    for i in range(n + 1):
        for j in range(1, MAX_WIDTH + 1):
            temp[i][j] = 0

    # 여기가 중력 내려가는 부분!!!!!
    for j in range(1, MAX_WIDTH + 1):
        # 기존 배열은 계속 위로 올라가면서
        # POINT !! 새로운 배열에는 index값을 따로 두어서
        # 기존 배열에 값이 있는 경우에만 넣고 index 변경
        last_idx = n
        for i in range(n, -1, -1):
            if bucket[i][j]:
                temp[last_idx][j] = bucket[i][j]
                last_idx -= 1

    # 다시 temp 배열을 옮겨줍니다.
    for i in range(n + 1):
        for j in range(1, MAX_WIDTH + 1):
            bucket[i][j] = temp[i][j]

#반시계 방향 회전
def rotate() :
    global MAP

    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[n - 1 - j][i] = MAP[i][j]

    MAP = temp[:]




point = 0
curPoint = 0

#python은 do - while 이 없다.
# 대신에 아래처럼 사용하면 된다.
while True :
    curPoint = calcPoint()
    point += curPoint
    gravity()
    rotate()
    gravity()
    if curPoint != 0 :
        continue
    break

print(point)

# 코드 트리 해설 풀이

from collections import deque

RED = 0
ROCK = -1
EMPTY = -2
EMPTY_BUNDLE = (-1, -1, -1, -1)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [
    [EMPTY for _ in range(n)]
    for _ in range(n)
]

bfs_q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 같은 색이거나, 빨간색 폭탄인 경우에만 이동이 가능합니다.
def can_go(x, y, color):
    return in_range(x, y) and not visited[x][y] and (
            grid[x][y] == color or grid[x][y] == RED
    )


def bfs(x, y, color):
    # visited 값을 초기화합니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # 시작점을 표시합니다.
    visited[x][y] = True
    bfs_q.append((x, y))

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            if can_go(new_x, new_y, color):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True


# (x, y) 지점을 시작으로 bundle 정보를 계산해 반환합니다.
def get_bundle(x, y):
    # Step1. (x, y)를 시작으로 bfs 탐색을 진행합니다.
    bfs(x, y, grid[x][y]);

    # Step2. bundle 정보를 계산해 반환합니다.
    bomb_cnt, red_cnt = 0, 0
    standard = (-1, -1)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                continue

            bomb_cnt += 1

            if grid[i][j] == RED:
                red_cnt += 1
            elif (i, -j) > standard:
                standard = (i, -j)

    std_x, std_y = standard;
    return (bomb_cnt, -red_cnt, std_x, std_y)


# 우선순위에 따라 쉽게 계산하기 위해
# (폭탄 묶음의 크기, -빨간색 폭탄의 수, 행 번호, -열 번호)
# 순서대로 값을 넣어줍니다.
def find_best_bundle():
    best_bundle = EMPTY_BUNDLE

    # 빨간색이 아닌 폭탄들에 대해서만 전부 탐색합니다.
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 1:
                bundle = get_bundle(i, j)
                if bundle > best_bundle:
                    best_bundle = bundle

    return best_bundle


def remove():
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                grid[i][j] = EMPTY


def gravity():
    # Step1.
    # 중력 작용을 쉽게 구현하기 위해
    # temp 배열을 활용합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = EMPTY

    # Step2.
    for j in range(n):
        # 아래에서 위로 올라오면서
        # 해당 위치에 폭탄이 있는 경우에만 temp에
        # 쌓아주는 식으로 코드를 작성할 수 있습니다.

        # 단, 돌이 있는 경우에는
        # 위에부터 쌓일 수 있도록 합니다.
        last_idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] == EMPTY:
                continue
            if grid[i][j] == ROCK:
                last_idx = i
            temp[last_idx][j] = grid[i][j]
            last_idx -= 1

    # Step3. 다시 temp 배열을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


# 반시계 방향으로 90' 만큼 회전합니다.
def rotate():
    # Step1.
    # 회전 과정을 쉽게 구현하기 위해
    # temp 배열을 활용합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = EMPTY

    # Step2.
    # 기존 격자를 반시계 방향으로 90도 회전했을 때의 결과를
    # temp에 저장해줍니다.
    for j in range(n - 1, -1, -1):
        for i in range(n):
            temp[n - 1 - j][i] = grid[i][j]

    # Step3.
    # 다시 temp 배열을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def clean(x, y):
    # Step1. (x, y)를 시작으로 지워야할 폭탄 묶음을 표시합니다.
    bfs(x, y, grid[x][y])

    # Step2. 폭탄들을 전부 지워줍니다.
    remove()

    # Step3. 중력이 작용합니다.
    gravity()


def simulate():
    global ans

    # Step1. 크기가 최대인 폭탄 묶음을 찾습니다.
    best_bundle = find_best_bundle()
    bomb_cnt, _, x, y = best_bundle

    # 만약 폭탄 묶음이 없다면, 종료합니다.
    if best_bundle == EMPTY_BUNDLE or bomb_cnt <= 1:
        return False

    # Step2. 선택된 폭탄 묶음에 해당하는 폭탄들을 전부 제거 후
    #        중력이 작용합니다.
    ans += bomb_cnt * bomb_cnt
    clean(x, -y)

    # Step3. 반시계 방향으로 90' 만큼 회전합니다.
    rotate()

    # Step4. 중력이 작용합니다.
    gravity()

    return True


# 끝나기 전까지 시뮬레이션을 반복합니다.
while True:
    keep_going = simulate()

    if not keep_going:
        break

print(ans)