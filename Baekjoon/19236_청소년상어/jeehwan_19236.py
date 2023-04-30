'''

sol1)

청소년 상어

공간은 4x4로 고정한다.

1.
상어는 무조건 (0, 0)에 있는 물고기를 먹으며 시작하며, 먹은 물고기의 방향을 그대로 이어간다.

2.
물고기들은 번호가 작은 물고기부터 차례대호 움직인다. 
이동할 수 있는 칸?! 다른 물고기가 있는 칸 // 빈칸
이동할 수 없는 칸?! 상어가 있는 칸 // 격자 외 

각 물고기는 이동할 수 있는 칸을 찾을 떄까지 45도 반시계 방향 회전. 만약, 이동을 할 수없다면 이동하지 않는다.
각 물고기들은 차례마다 대각선을 포함한 8개 방향으로 한 칸씩 움직인다.

3.
상어는 방향은 고정이나 이동거리는 공간 내라면 상관없고,
먹은 물고기의 방향을 가지게 됨.
또한 이동중에 있는 물고기는 먹지 않는다.
다음 방향이 공간 밖으로 이동하거나 먹을 수 있는 물고기가 존재하지 않는다면 끝난다.
상어가 획득할 수 있는 점수의 최대를 구하시오.
점수는 상어가 잡아먹은 물고기의 번호만큼 획득한다.

1 > 3 > 2 > 3 > 2 ... 계속 반복 until?! 다음 방향이 공간 밖으로 이동하거나 먹을 수 있는 물고기가 존재하지 않는다면 끝난다.

7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2

'''

import copy

# 4 * 4크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블

MAP = [[None] * 4 for _ in range(4)]  # 4 * 4의 이차원 배열 / 각 row, col에에 [물고기 번호, 방향]을 저장


# 초기 데이터 세팅
for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기번호, 방향]을 저장 (0 ~ 7) index처리하기 편하기 위함 => 밑에 있는 델타 배열은 0번 부터 시작
        MAP[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# 8가지 방향 정의 =>
# 상 좌상, 좌, 좌하, 하, 우하 ,우, 우상 (문제에 정의된 순서대로 해야함!)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


# 현재 위치에서 위쪽으로 회전된 결과 반환 =>  이렇게 처리 해주는게 진짜 굿굿 % 연산으로 반복
# 방향 바꾸고, 경계값에선 다시 원점으로 돌아 올 수 있는 모듈러 연산
def turn_leff(dir):
    return (dir + 1) % 8


# 최종결과
result = 0


# 현재 배열에서 특정한 번호의 물고기 위치 찾기

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)

    return None


# 모든 물고기를 회전 및 이동시키는 함수 => 물고기 움직임
def move_all_fishes(array, now_row, now_col):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은번호 부터) 확인
    for i in range(1, 17):
        # 해당 믈고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            row, col = position[0], position[1]
            dir = array[row][col][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for _ in range(8):
                next_row = row + dr[dir]
                next_col = col + dc[dir]

                # 해당 방향으로 이동이 가능하다면 이동
                if 0 <= next_row and next_row < 4 and 0 <= next_col and next_col < 4:
                    # 상어가 있는 곳은 또 못간다!
                    if not (next_row == now_row and next_col == now_col):
                        # 방향은 그대로 가져가니깐 이렇게 함
                        array[row][col][1] = dir
                        array[row][col], array[next_row][next_col] = array[next_row][next_col], array[row][col]
                        break
                # 위에 있는 if 조건들을 통과하지 못하면 방향바꿔서 해야대니깐
                dir = turn_leff(dir)


# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환 => 상어 움직임
ㅣ
def get_possible_positions(array, now_row, now_col):
    positions = []
    dir = array[now_row][now_col][1]

    # 상어가 가지고 있는 현재 방향으로 계속 이동 시키기
    for i in range(4):
        now_row += dr[dir]
        now_col += dc[dir]
        # 범위를 벗어나지 않는지 확인
        if 0 <= now_row and now_row < 4 and 0 <= now_col and now_col < 4:
            # 물고기가 존재하는 경우
            if array[now_row][now_col][0] != -1:
                positions.append((now_row, now_col))

    return positions


# 모든 경우를 탐색하기 위한 dfs함수, 처음 상어의 위치 now_row, now_col = (0, 0)
def dfs(array, now_row, now_col, total):
    global result
    array = copy.deepcopy(array)  # 리스트를 통째로 복사

    total += array[now_row][now_col][0]  # 현재 위치의 물고기 먹기
    array[now_row][now_col][0] = -1  # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_row, now_col)  # 전체 물고기 이동

    # 이제 다시 상어가 이동할 차례! 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_row, now_col)

    # dfs 완료 조건
    if len(positions) == 0:
        result = max(result, total)  # 최대값 저장
        return

    # 모든 이동할 수 있는 위치로 재귀적 수행
    # 새롭게 다시 함수를 시작하는 dfs의 시작 부분
    for next_row, next_col in positions:
        dfs(array, next_row, next_col, total)


dfs(MAP, 0, 0, 0)
print(result)



