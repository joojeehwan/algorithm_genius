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
# 구슬 번호마다 깨진 수
blows = [0, 0, 0]


# 이동 가능성 확인
def moving():
    numbers = list()
    moving_dir, moving_dis = 0, 1
    now_row, now_col = shark_row, shark_col
    move = True
    # 달팽이 껍질 모양으로 움직임
    while move:
        for _ in range(2):
            for _ in range(moving_dis):
                now_row += d2[moving_dir][0]
                now_col += d2[moving_dir][1]
                if not (0 <= now_row < N and 0 <= now_col < N):
                    move = False
                    break
                now_num = grid[now_row][now_col]
                # 이번칸이 비었으면, 다음칸에서 당겨오기
                if now_num:
                    numbers.append(now_num)
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1

    num_cnt = len(numbers)
    new_grid = list([0] * N for _ in range(N))
    new_grid[shark_row][shark_col] = 9
    moving_dir, moving_dis, moving_idx = 0, 1, 0
    move = True
    now_row, now_col = shark_row, shark_col
    # 달팽이 껍질 모양으로 움직임
    while move:
        for _ in range(2):
            for _ in range(moving_dis):
                now_row += d2[moving_dir][0]
                now_col += d2[moving_dir][1]
                if not (0 <= now_row < N and 0 <= now_col < N) or moving_idx >= num_cnt:
                    move = False
                    break
                else:
                    new_grid[now_row][now_col] = numbers[moving_idx]
                    moving_idx += 1
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1
    return new_grid


# 연속성 확인
def check():
    moving_dir, moving_dis = 0, 1
    now_row, now_col = shark_row, shark_col
    # 마지막에 폭발할 구슬 위치 & 4개씩 저장해나갈 리스트
    bomb_sets, bomb_marbles = [[], [], []], [(now_row, now_col)]
    continuous_cnt = 1
    finding = True
    # 달팽이 껍질 모양으로 움직임
    while finding:
        for _ in range(2):
            for _ in range(moving_dis):
                next_row = now_row + d2[moving_dir][0]
                next_col = now_col + d2[moving_dir][1]
                if not (0 <= next_row < N and 0 <= next_col < N):
                    finding = False
                    break
                now_num, next_num = grid[now_row][now_col], grid[next_row][next_col]
                # 더 이상 구슬이 없다
                if now_num == 0:
                    finding = False
                    break
                elif now_num == next_num:
                    continuous_cnt += 1
                    bomb_marbles.append((next_row, next_col))
                elif now_num != next_num:
                    if continuous_cnt >= 4:
                        # 추가하고 초기화
                        bomb_sets[now_num-1] += bomb_marbles
                    continuous_cnt = 1
                    bomb_marbles = [(next_row, next_col)]
                now_row, now_col = next_row, next_col
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1

    return bomb_sets


# 구슬 폭.발
def bombing(bomb_list):
    for marble_idx in range(3):
        for bomb_row, bomb_col in bomb_list[marble_idx]:
            grid[bomb_row][bomb_col] = 0
        blows[marble_idx] += len(bomb_list[marble_idx])


# 구슬 변화
def changing():
    moving_dir, moving_dis = 0, 1
    now_row, now_col = shark_row, shark_col
    # 2개로 이루어진 한 쌍을 저장할 리스트
    groups = list()
    finding = True
    continuous_cnt = 1
    # 달팽이 껍질 모양으로 움직임
    while finding:
        for _ in range(2):
            for _ in range(moving_dis):
                next_row = now_row + d2[moving_dir][0]
                next_col = now_col + d2[moving_dir][1]
                if not (0 <= next_row < N and 0 <= next_col < N):
                    finding = False
                    break
                now_num, next_num = grid[now_row][now_col], grid[next_row][next_col]
                # 더 이상 구슬이 없다
                if now_num == 0:
                    finding = False
                    break
                if 1 <= now_num <= 3:
                    if now_num == next_num:
                        continuous_cnt += 1
                    else:
                        # 구슬의 연속된 개수, 구슬의 번호
                        groups += [continuous_cnt, now_num]
                        continuous_cnt = 1
                now_row, now_col = next_row, next_col
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1

    # 이제 다시 채워.. 아니 이 코드만 몇 번을 반복하는거야 지금 ㅡㅡ
    group_cnt = len(groups)
    moving_dir, moving_dis = 0, 1
    now_row, now_col = shark_row, shark_col
    move = True
    idx = 0
    changed_grid = list([0] * N for _ in range(N))
    changed_grid[shark_row][shark_col] = 9
    # 달팽이 껍질 모양으로 움직임
    while move:
        for _ in range(2):
            for _ in range(moving_dis):
                now_row += d2[moving_dir][0]
                now_col += d2[moving_dir][1]
                if not (0 <= now_row < N and 0 <= now_col < N) or idx >= group_cnt:
                    move = False
                    break
                else:
                    changed_grid[now_row][now_col] = groups[idx]
                    idx += 1
            moving_dir = (moving_dir + 1) % 4
        moving_dis += 1
    return changed_grid


# def printing():
#     print("---------------------------------")
#     for line in grid:
#         print(*line)
#     print("---------------------------------")


# 블리자드 마법 M번 실행
for cnt in range(M):
    direction, distance = spells[cnt]
    # 1. 방향, 거리만큼 구슬 파괴
    for dist in range(1, distance + 1):
        row = shark_row + d1[direction][0] * dist
        col = shark_col + d1[direction][1] * dist
        grid[row][col] = 0

    movable = True

    # 더 이상 이동, 폭발할 구슬이 없을 때 까지
    while movable:
        # 2. 구슬 이동
        grid = moving()
        # 3. 연속 체크
        continuous = check()
        if any(continuous):
            # 3-1. 구슬 폭발
            bombing(continuous)
        else:
            # 3-2. 구슬 이동 중지
            movable = False
    # 4. 구슬 변화
    grid = changing()

print(1 * blows[0] + 2 * blows[1] + 3 * blows[2])
