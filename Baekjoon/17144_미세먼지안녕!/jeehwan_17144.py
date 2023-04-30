'''

공기 청정기 있는 곳 :  -1 (2번 위아래로 붙어져 있고, 가장 윗행, 아랫 행과 2칸 이상 떨어져 있다)

미세먼지 제로 : 0

미세먼지 있는 곳 : -1 ~ 1000




T 초가 지난 후의 미세먼지가 남아있는 양을 구하라



'''


R, C, T = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]

aircon = []

for row in range(R):
    for col in range(C):
        if MAP[row][col] == -1 :
            aircon.append((row, col))

ans = 0




#미세먼지 확산
def sand():

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    MAP_TEMP = [[0] * C for _ in range(R)]

    #2. 확산
    for row in range(R):
        for col in range(C):
            # 미세먼지 존재 -> 확산
            if MAP[row][col] > 0:
                cnt = 0
                for k in range(4):
                    next_row = row + dr[k]
                    next_col = col + dc[k]

                    if (0 <= next_row < R and 0 <= next_col < C) and (MAP[next_row][next_col] != -1):
                        #미세먼지 확산
                        MAP_TEMP[next_row][next_col] += (MAP[row][col] // 5)
                        cnt += 1
                # 확산 후 원래 미세먼지 양 계산
                MAP[row][col] = MAP[row][col] - (MAP[row][col] // 5 * cnt)

    # 3. 동시에 확산 진행
    for row in range(R) :
        for col in range(C):
            MAP[row][col] += MAP_TEMP[row][col]

    return

#위쪽 공기청정기 작동 => 반 시계 방향으로 작동
def up_fresh():

    #동, 북, 서, 남
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    dir = 0
    #위쪽 방향 공기 청정기
    row, col = aircon[0]

    up, col = row, 1

    prvious = 0

    while True:

        next_row = row + dr[dir]
        next_col = col + dc[dir]

        #다시 처음 위치로 돌아옴
        if row == up and col == 0:
            break
        # 맵 벗어나기 => 방향 바꾸면 된다.
        # (0 <= next_row < R and 0 < next_col < C)
        if next_row < 0 or next_row >= R or next_col < 0 or next_col >= C :
            dir += 1
            continue
        #바람이 불면, 미세먼지의 방향으로 모두 한칸 씩 이동, 두 변수의 값 교환
        MAP[row][col], prvious = prvious, MAP[row][col]

        #while문 안에서의 row, col 값을 갱신해
        row, col = next_row, next_col

    return

#아래쪽 공기 청정기 작동 => 시계 방향으로 작동

def down_fresh():
    # 동, 북, 서, 남
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    dir = 0
    # 위쪽 방향 공기 청정기
    row, col = aircon[1]

    down, col = row, 1

    prvious = 0

    while True:

        next_row = row + dr[dir]
        next_col = col + dc[dir]

        # 다시 처음 위치로 돌아옴
        if row == down and col == 0:
            break
        # 맵 벗어나기 => 방향 바꾸면 된다.
        # (0 <= next_row < R and 0 < next_col < C)
        if next_row < 0 or next_row >= R or next_col < 0 or next_col >= C:
            dir += 1
            continue
        # 바람이 불면, 미세먼지의 방향으로 모두 한칸 씩 이동, 두 변수의 값 교환
        MAP[row][col], prvious = prvious, MAP[row][col]

        # while문 안에서의 row, col 값을 갱신해
        row, col = next_row, next_col

    return

for _ in range(T):

    # 미세먼지 확산
    sand()
    # 공기청정기 작동
    up_fresh()
    down_fresh()

#남은 미세먼지의 양 계산
for row in range(R):
    for col in range(C):
        if MAP[row][col] > 0 :
            ans += MAP[row][col]

print(ans)