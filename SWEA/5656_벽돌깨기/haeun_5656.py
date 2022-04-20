import copy
from collections import deque

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 처음에 모든 벽돌의 개수를 구하는 함수
def all_bricks(bricks):
    count = 0
    for row in range(H):
        for col in range(W):
            if bricks[row][col]:
                count += 1
    return count


# 구슬을 명중시킬 위치를 찾는 함수(총 W만큼 위치를 찾는다)
def get_start_points(bricks):
    # 각 col의 제일 위에 있는 숫자를 찾으면 된다.
    # 한 가로줄에서만 찾는게 아니라 ^^..
    starts = []
    for c in range(W):
        for r in range(H):
            if bricks[r][c]:  #한 col에서 찾았으면 다음 col로 넘어감
                starts.append((r, c))
                break
    return starts


# 벽돌을 부수는 함수. BFS로 연속적으로 부술 수 있도록 하였다.
def break_bricks(row, col, bricks):
    if bricks[row][col] == 1:
        # 본인만 폭파하고 가세요
        bricks[row][col] = 0
        return 1
    queue = deque()
    queue.append((row, col))
    broken_bricks_cnt = 0

    while queue:
        now = queue.popleft()
        now_row, now_col = now[0], now[1]
        value = bricks[now_row][now_col]
        if value == 0:
            continue
        broken_bricks_cnt += 1
        bricks[now_row][now_col] = 0

        for distance in range(1, value):
            for d in range(4):
                # 바보같이 distance 곱하는거 까먹었다.
                next_row = now_row + distance * dr[d]
                next_col = now_col + distance * dc[d]
                if 0 <= next_row < H and 0 <= next_col < W:
                    brick_num = bricks[next_row][next_col]
                    if brick_num == 1:
                        broken_bricks_cnt += 1
                        bricks[next_row][next_col] = 0
                    elif brick_num > 1:
                        # 반복이 상당했다. 하지만 deque를 set으로 만들 수도 없고..^^
                        if (next_row, next_col) not in queue:
                            queue.append((next_row, next_col))
    # 부순 벽돌의 개수를 반환한다.
    return broken_bricks_cnt


# 부순 후 벽돌들을 중간에 비지 않도록 끌어내린다. 이전 코드 참고함.
def falling(bricks):
    for col in range(W):
        empty = 0
        for row in range(H - 1, -1, -1):
            if bricks[row][col] == 0:
                empty += 1
            else:
                # 누적된 떨어진 값을 바로 사용...
                # 매번 구해줄 필요가 없는 것이다.
                bricks[row + empty][col] = bricks[row][col]
        for row in range(empty):
            bricks[row][col] = 0


# 구슬을 명중시키는 함수
def drop(count, break_cnt, bricks, path):
    global answer
    global all_bricks_cnt
    if count == N:
        answer = max(answer, break_cnt)
        return

    start_points = get_start_points(bricks)  # 맨 위의 시작할 지점(들)
    # 모든 벽돌이 부숴져서 명중시킬 벽돌이 없다면 answer를 모든 벽돌 수로 설정한다. -> 출력은 0이 됨
    if not start_points:
        answer = all_bricks_cnt
        return
    for start in start_points:
        now_bricks = copy.deepcopy(bricks)  # 2차원 배열 복사해야함. 이 맵을 마구 바꿔서 사용해야하는데, 이후에 다시 복구시킬 방법 X
        now_broken_bricks = break_bricks(start[0], start[1], now_bricks)
        falling(now_bricks)
        drop(count+1, break_cnt + now_broken_bricks, now_bricks, path + [start[1]])


for tc in range(T):
    N, W, H = map(int, input().split())
    MAP = list(list(map(int, input().split())) for _ in range(H))
    all_bricks_cnt = all_bricks(MAP)
    answer = 0
    drop(0, 0, MAP, [])
    print(f"#{tc+1} {all_bricks_cnt - answer}")