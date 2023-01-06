'''

4 * 4 격자판 // (x, y) == (row, col)

도둑말 : 1 ~ 16번호


[규칙]

1. 초기에 술래말은 (0, 0)에서 시작

2. 도둑말의 움직임
   - 도둑말은 번호가 작은 순서대로 이동하기 시작.
   - 본인이 가지고 있는 방향으로, 한 번에 이동에 "한칸" 이동
   - 빈 칸이나, 다른 도둑말이 있는 칸 => 이동 o // 술래말이 있는 칸, 격자 바깥 => 이동x
   - 이동할 수 있는 칸을 찾을 때 까지 45도로 반시계 방향으로 회전. if 찾지못해?! then 움직x
   - 이동했을 때, 그 칸에 다른 도둑말이 있다면 자리 change


3. 술래말의 움직임

    - 도둑말의 움직임이 모두 끝난 다음에 이동하기 시작
    - 도둑말이 가지고 있는 방향으로만, 한 번에 여러 칸도 이동 가능
    - 잡고자 하는 도둑말로 이동할 때 존재하는 도둑말은 잡지 x
    - 도둑말이 있는 없는 곳으로는 이동할 수 없다.
    - 술래말이 다른 도둑말을 잡은 뒤에는, 다시 도둑말이 번호 순서대로 움직임
    -

4. 술래말이 이동할 수 있는 곳에 도둑말이 더 이상 존재하지 않는다면 게임 끝. 해당 방향으로 이동했을 때, 더 이상 도둑말이 없을 때



청소년 상어 문제, 다른 사람들은 어떻게 풀었는지 풀이 3개 이상 확인할 것




7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2

'''

import copy

# [물고기번호, 방향]
MAP = [[None] * 4 for _ in range(4)]

result = 0

for i in range(4):

    # 한줄씩 입력받고,
    temp = map(int, input().split())

    # 그 입력받은 한줄에서 2개씩 묶어서, MAP에다가 넣기
    for j in range(4):
        # -1을 해주는 이유?! 델타 배열은 인덱스가 0 부터 시작 이것을 통일 하기 위함
        MAP[i][j] = [temp[j * 2], temp[j * 2 + 1] - 1]

# 8방향 정의 문제에 나온대로
# 상, 좌상, 좌,  ~   , 우, 우상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def turn_left(dir):
    # 문제에 주어진 인덱스에서 왼쪽으로 한 칸씪 이동하게 되면 그게 바로, 왼쪽으로 대각선 이동을 하게 하는 방향이 됨
    # dir의 숫자(인덱스)에 맞게끔 dr / dc를 세팅 해놨기 떄문에 가능한 것
    return (dir + 1) % 8


def find_horse(lst, index):
    for row in range(4):
        for col in range(4):
            if lst[row][col][0] == index:
                return (row, col)

    return None


# 도둑말 이동
def move_theifhorse(array, now_row, now_col):
    # now_row, now_col = 술래말의 좌표
    for i in range(1, 17):
        # 지금 n번 도둑말 어디있니!?
        position = find_horse(array, i)
        if position != None:
            row, col = position[0], position[1]
            dir = array[row][col][1]

            for _ in range(8):

                next_row = row + dr[dir]
                next_col = col + dc[dir]

                # 이동 후 범위체크

                if 0 <= next_row < 4 and 0 <= next_col < 4:

                    # 술래말이 있는 곳은 못간다.
                    if not (next_row == now_row and next_col == now_col):
                        array[row][col][1] = dir
                        # 자리 change
                        array[row][col], array[next_row][next_col] = array[next_row][next_col], array[now_row][now_col]
                        break
                # 이렇게 8번 하면, 모든 방향을 다 한번씩 보게 되는 것
                dir = turn_left(dir)


# 술래말이 이동할 수 있는 모든 위치 반환

def movesoolreemalReturnLst(array, now_row, now_col):
    positions = []
    dir = array[now_row][now_col][1]
    # "4"인 이유?! 술래말은 도둑말의 방향으로만 이동 가능. 따라서
    # MAP의 크기 4 * 4 이므로 술래말 기준 한칸씩 이동할 수 있는 최대는 4인것
    for i in range(4):
        now_row += dr[dir]
        now_col += dc[dir]

        if 0 <= now_row < 4 and 0 <= now_col < 4:
            if array[now_row][now_col][0] != -1:
                positions.append((now_col, now_col))

    return positions


# 모든 경우 탐색을 위한 dfs 함수, 처음 상어의 위치는 (0, 0) 고정

def dfs(array, now_row, now_col, total):
    global result

    # 재귀 lev마다 서로의 영역을 구분하기 위함.
    array = copy.deepcopy(array)

    total += array[now_row][now_col][0]

    array[now_row][now_col][0] = -1  # 물고기를 먹었으므로..!

    # 물고기 이동 함수
    move_theifhorse(array, now_row, now_col)

    # 상어 이동
    positions = movesoolreemalReturnLst(array, now_row, now_col)
    # dfs 종료 조건

    if len(positions) == 0:
        # total에 재귀를 타면서, 끝까지 온 값이 있으니! 그걸 기존에
        # 전역을오 관리하던 result와 비교 연산한것
        result = max(result, total)
        return
        # 다시 재귀 타는 조건 (상어 좌표 기준)

    for next_row, next_col in positions:
        dfs(array, next_row, next_col, total)


dfs(MAP, 0, 0, 0)
print(result)


