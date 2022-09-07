N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
spells = list(tuple(map(int, input().split())) for _ in range(M))

shark_row, shark_col = N // 2, N // 2
# 마법에 필요한 방향
d1 = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
# 번호에 따른 움직임
d2 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 구슬 번호마다 깨진 수
blows = [0, 0, 0, 0]


def moving():
    moving_dir = 1
    moving_dis = 1
    now_row, now_col = shark_row, shark_col - 1
    # 달팽이 껍질 모양으로 움직임
    while not(now_row < 0 and now_col < 0):
        for _ in range(2):
            for _ in range(moving_dis):
                next_row = now_row + d2[moving_dir][0]
                next_col = now_col + d2[moving_dir][1]
                # 이번칸이 비었으면, 다음칸에서 당겨오기
                if grid[now_row][now_col] == 0:
                    grid[now_row][now_col] = grid[next_row][next_col]
                    grid[next_row][next_col] = 0
                now_row, now_col = next_row, next_col
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1






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

    # 구슬 변화


print(1*blows[1] + 2*blows[2] + 3*blows[3])