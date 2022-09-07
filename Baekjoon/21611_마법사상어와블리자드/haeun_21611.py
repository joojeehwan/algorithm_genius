N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
spells = list(tuple(map(int, input().split())) for _ in range(M))

# (1,1) ~ (N,N)이 아니라 (0,0) ~ (N-1, N-1)로 본다.
shark_row, shark_col = N // 2, N // 2
# 이동, 파괴 등에서 시작점을 위해 상어 자리를 구슬 번호가 아닌 수로 채운다.
grid[shark_row][shark_col] = 9
# 마법에 필요한 방향
d1 = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
# 번호에 따른 움직임에 필요한 방향
d2 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 구슬 번호마다 깨진 수(0번은 제외)
blows = [0, 0, 0, 0]


def moving():
    moving_dir, moving_dis = 0, 1
    now_row, now_col = shark_row, shark_col
    # 달팽이 껍질 모양으로 움직임
    while not(now_row <= 0 and now_col <= 0):
        for _ in range(2):
            for _ in range(moving_dis):
                next_row = now_row + d2[moving_dir][0]
                next_col = now_col + d2[moving_dir][1]
                now_num, next_num = grid[now_row][now_col], grid[next_row][next_col]
                # 이번칸이 비었으면, 다음칸에서 당겨오기
                if now_num == 0 and next_num:
                    grid[now_row][now_col] = next_num
                    grid[next_row][next_col] = 0
                elif now_num == 0 and next_num == 0:
                    # 둘 다 비었다면 더 이상 이동이 불가능하다.
                    return
                now_row, now_col = next_row, next_col
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1


def bombing():
    moving_dir, moving_dis = 0, 1
    now_row, now_col = shark_row, shark_col
    # 마지막에 폭발할 구슬 위치 & 4개씩 저장해나갈 리스트
    bomb_sets, bomb_marbles = list(), list()
    continuous_cnt = 1
    finding = True
    # 달팽이 껍질 모양으로 움직임
    while finding and not (now_row <= 0 and now_col <= 0):
        for _ in range(2):
            for _ in range(moving_dis):
                next_row = now_row + d2[moving_dir][0]
                next_col = now_col + d2[moving_dir][1]
                now_num, next_num = grid[now_row][now_col], grid[next_row][next_col]
                # 더 이상 구슬이 없다
                if now_num == 0:
                    finding = False
                    break
                elif now_num == next_num:
                    continuous_cnt += 1
                    bomb_marbles.append((next_row, next_col))
                    if continuous_cnt == 4:
                        # 추가하고 초기화
                        bomb_sets += bomb_marbles
                        bomb_marbles = list()
                        continuous_cnt = 1
                elif now_num != next_num:
                    continuous_cnt = 1
                    bomb_marbles = list()
                now_row, now_col = next_row, next_col
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1

    # 폭발시킬게 없다면 끝
    if not bomb_sets:
        return

    # 구슬 폭.발
    for bomb_row, bomb_col in bomb_sets:
        grid[bomb_row][bomb_col] = 0


def changing():



# 블리자드 마법 M번 실행
for cnt in range(M):
    direction, distance = spells[cnt]
    # 방향, 거리만큼 구슬 파괴
    for dist in range(1, distance+1):
        row = shark_row + d1[direction][0] * dist
        col = shark_col + d1[direction][1] * dist
        grid[row][col] = 0

    for line in grid:
        print(*line)
    # 더 이상 이동, 폭발할 구슬이 없을 때 까지
    # 구슬 이동
    moving()
    for line in grid:
        print(*line)
    # 구슬 폭발
    bombing()
    # 구슬 변화


print(1*blows[1] + 2*blows[2] + 3*blows[3])