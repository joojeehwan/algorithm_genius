"""
- 풀이시간 3:54, 시작 19:25 , 끝 23:19
- 걍 짜증나
"""
# 입력 처리

N, M, K = map(int, input().split())
maze = list(list(map(int, input().split())) for _ in range(N))

runners = list()
for i in range(M):
    r_row, r_col = map(int, input().split())
    # 입력에 장난질 좀 stop...
    runners.append([r_row - 1, r_col - 1])

e_row, e_col = map(int, input().split())
# 입력에 장난질 좀 stop...
e_row -= 1
e_col -= 1
maze[e_row][e_col] = -1

# 전역 변수
answer = 0  # 러너들이 움직인 거리
left = [True] * M  # 해당 러너가 미로에 남아있는지
dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]


def in_range(_r, _c):
    return 0 <= _r < N and 0 <= _c < N


# 모든 러너가 동시에 움직인다.
def move():
    global answer
    for idx in range(M):
        # 탈출했는지 확인한다.
        if left[idx]:
            r, c = runners[idx]
            # 상하좌우로 1칸 움직일 수 있다.
            for d in range(4):
                # 상, 하로 움직이는 것을 우선시한다.
                nr = r + dr[d]
                nc = c + dc[d]

                # 탈출한 경우
                if e_row == nr and e_col == nc:
                    left[idx] = False
                    # [🤬] 탈출한 것도 움직인 거리에 포함해야됨
                    answer += 1
                    continue
                if not in_range(nr, nc):
                    continue
                # 벽이 있는 곳에는 갈 수 없다.
                if 1 <= maze[nr][nc] <= 9:
                    continue
                # 현재 머물렀던 칸 보다 출구가 가까워야한다.
                if abs(e_row - r) + abs(e_col - c) < abs(e_row - nr) + abs(e_col - nc):
                    continue
                # 움직일 수 없다면 움직이지 않는다.
                runners[idx] = [nr, nc]
                answer += 1
                break


# 출구와 참가자 최소 한명을 포함하는 가장 작은 정사각형을 찾는다.
# l, 시작점 (x, y)를 찾는다.
def find_smallest_square():
    l = 987654321
    x, y = N, N

    for idx in range(M):
        # 탈출한 러너는 볼 필요 없다.
        if left[idx]:
            r, c = runners[idx]
            # 현재 찾은 가장 짧은 거리와 같거나 더 짧아야 볼 가치가 있다.
            # 출구와 행, 열이 같은 경우는 다른 경우가 거리가 되어줄 것이며
            # 대각선인 경우 짧은걸로 하면 긴걸 커버 못하니깐 결국 긴걸로 해야한다.
            # 따라서 대각선에 있든 직선에 있든 결국 큰 차이가 나는 걸로 길이를 재야한다.
            # 차이 + 1을 해야 정사각형의 길이가 나온다.
            length = max(abs(e_row - r), abs(e_col - c)) + 1
            if length > l:
                continue

            # 좌상을 구한다.
            r1, c1 = min(e_row, r), min(e_col, c)
            # 우하를 구한다.
            r2, c2 = max(e_row, r), max(e_col, c)

            # 대각선인 경우
            # [🤬] 대각선이 아닌 경우만 구했더니 시작 지점을 제대로 못 찾음
            if e_row != r and e_col != c:
                # 행 차이가 더 크다 -> 열을 잘 골라야함
                if abs(e_row - r) > abs(e_col - c):
                    # 행 차이는 그 자체가 길이가 되었으므로, 행은 고정 됨
                    # 이제 좀 더 왼쪽에서 시작하는 열을 찾아야함
                    # 근데 더 오른쪽에 있는 열(c2)에서 길이를 뺀 값이 0보다 크면 거기서 시작하면 됨
                    # 근데 0을 넘어가 음수가 되어버리면 그냥 0부터 시작하면 됨
                    # [🤬] 여기도 그냥 0으로 바꿀지 말지만 계산했음. c1, c2도 아닌 값이 c1에 들어가야할 수 있음
                    c1 = c2 - length + 1 if c2 - length + 1 > 0 else 0
                # 열 차이가 더 크다 -> 행을 잘 골라야함
                elif abs(e_row - r) < abs(e_col - c):
                    # 열 차이는 그 자체가 길이가 되었으므로, 열은 고정 됨
                    # 이제 좀 더 위에서 시작하는 행을 골라야함
                    # 더 아래에 있는 행(r2)에서 길이를 뺀 값이 0보다 크면 거기서 시작하면 됨
                    # 근데 0을 넘어 음수가 되어버리면 그냥 0부터 시작하면 됨
                    # [🤬] 여기도 그냥 0으로 바꿀지 말지만 계산했음. r1, r2도 아닌 값이 r1에 들어가야할 수 있음
                    r1 = r2 - length + 1 if r2 - length + 1 > 0 else 0
                # 차이가 같으면 그냥 좌상을 반환하면 됨
            # 행이 같을때, 0 또는 r1 - length 중 골라야한다.
            elif e_row == r:
                # 만약 r1에서 length를 뺀게 0행보다 밑에 있으면 거기서 시작하는게 작은 정사각형을 만들 수 있다.
                # [🤬] 여기도 그냥 0으로 바꿀지 말지만 계산했음. r1, r2도 아닌 값이 r1에 들어가야할 수 있음
                r1 = r1 - length + 1 if r1 - length + 1 > 0 else 0
            # 열이 같은데, 0 또는 c1 - length 중 골라야한다.
            elif e_col == c:
                # 만약 열에서 길이를 뺀게 0열보다 오른쪽에 있으면 거기서 시작하는게 작은 정사각형을 만들 수 있다.
                # [🤬] 여기도 그냥 0으로 바꿀지 말지만 계산했음. c1, c2도 아닌 값이 c1에 들어가야할 수 있음
                c1 = c1 - length + 1 if c1 - length + 1 > 0 else 0

            # 길이가 적거나, 같은데 정사각형의 시작 위치가 더 위 or 왼쪽인 경우 업데이트
            if length < l or x > r1 or (x == r1 and y > c1):
                l = length
                x, y = r1, c1

    return l, x, y


# 시계방향으로 90도 회전한다. (r,c) => (c, l - r - 1)
# 회전된 벽은 내구도가 1씩 까인다.
def rotate_maze(l, x, y):
    global e_row, e_col
    rotated = [[0] * l for _ in range(l)]

    # 엇 사람은...?
    for i in range(M):
        if left[i] and x <= runners[i][0] <= x + l - 1 and y <= runners[i][1] <= y + l - 1:
            # [🤬] 러너 이동도 대충 계산함
            s_row = runners[i][0] - x
            s_col = runners[i][1] - y
            runners[i] = [x + s_col, y + l - s_row - 1]

    # 돌리기
    for i in range(l):
        for j in range(l):
            # [🤬] 인덱스 오류 엄청 남. 근데 시계방향 공식 문제가 아니라 위에서 정사각형 시작점 만드는거에서 문제가 자꾸 남
            rotated[j][l - 1 - i] = maze[x + i][y + j]
            if 1 <= rotated[j][l - i - 1] <= 9:
                rotated[j][l - i - 1] -= 1
            # 탈출구도 돌려지면 업데이트
            if maze[x + i][y + j] == -1:
                e_row, e_col = x + j, y + l - i - 1

    # 돌린거 다시 저장
    for i in range(l):
        for j in range(l):
            maze[x + i][y + j] = rotated[i][j]


def solution():
    global K
    # K초를 반복하거나, 모든 참가자가 탈출한다면
    while K:
        move()
        # [🤬] 탈출한거 처리 이상하게 함
        # move() 함수에서 탈출하지 않은 사람만 세서 반환하니깐, 그 사람이 탈출한 경우 다시 빼줘야 됨
        if True in left:
            # 다 탈출해버리면 작은 정사각형을 찾을 수 없다.
            l, x, y = find_smallest_square()
            rotate_maze(l, x, y)
            K -= 1
        else:
            # [🤬] 다 탈출했으면 끝내줘
            break

    print(answer)
    print(e_row + 1, e_col + 1)


solution()
