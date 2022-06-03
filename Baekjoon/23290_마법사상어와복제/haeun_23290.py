"""
tqtqtqtqtq
tkddj rkwnrdmf qjtruqjflfQjsgoTdj^^
"""

# 물고기 개수 , 상어 연습 횟수
M, S = map(int, input().split())

# 물고기 이동 방향 델타.
# 왼쪽, 왼쪽위, 위, 오른쪽위, 오른쪽, 오른쪽아래, 아래, 왼쪽아래
fish_dr = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물고기 저장. 리스트로하니까 시간 초과나는 것 가틍ㅁ...
fish = dict()

# 물고기 냄새 저장할 2차원 배열, 값은 0 or 1 or 2
fish_smell = [[0]*4 for _ in range(4)]

# 물고기
for _ in range(M):
    r, c, d = list(map(int, input().split()))
    if fish.get((r-1, c-1)):
        fish[(r-1, c-1)].append(d-1)
    else:
        fish[(r-1, c-1)] = [d-1]

# 상어 이동 방향 델타. 상1 좌2 하3 우4
shark_dr = [-1, 0, 1, 0]
shark_dc = [0, -1, 0, 1]

# 상어
shark_row, shark_col = map(int, input().split())
shark_row -= 1
shark_col -= 1


# 물고기 이동
def move_fish(fish_row, fish_col, fish_dir):
    for j in range(8):
        # 45씩 반시계 회전
        # 0부터 시작하니까 방향을 일단 변화시키지 않고 찾아보는 것임
        new_fish_dir = (fish_dir - j) % 8
        next_r, next_c = fish_row + fish_dr[new_fish_dir], fish_col + fish_dc[new_fish_dir]
        if not(0 <= next_r < 4 and 0 <= next_c < 4):
            continue
        if fish_smell[next_r][next_c]:
            continue
        if next_r == shark_row and next_c == shark_col:
            continue
        # 이동할 수 있다면
        # 한마리씩 리스트로 보하면 느리고,
        # 좌표로 하면 한번 움직여버린게 다음에 또 움직이고
        # 한번 움직인 것들을 저장해두는 자료를 따로 만들거나...
        if moving_fish.get((next_r, next_c)):
            moving_fish[(next_r, next_c)].append(new_fish_dir)
        else:
            moving_fish[(next_r, next_c)] = [new_fish_dir]
        return
    if moving_fish.get((fish_row, fish_col)):
        moving_fish[(fish_row, fish_col)].append(fish_dir)
    else:
        moving_fish[(fish_row, fish_col)] = [fish_dir]
    return


# 상어 이동
def move_shark(s_row, s_col, step, path, eaten_fish):
    global max_eaten_fish_cnt
    global max_eaten_fish_path
    global shark_row
    global shark_col

    if step == 3:
        # print(path, eaten_fish)
        if max_eaten_fish_cnt < eaten_fish:
            max_eaten_fish_cnt = eaten_fish
            max_eaten_fish_path = path[:]
            shark_row, shark_col = s_row, s_col
        return

    # 64가지 방법에 대해 dfs로 찾아봐야함
    for shark_dir in range(4):
        next_row, next_col = s_row + shark_dr[shark_dir], s_col + shark_dc[shark_dir]
        if 0 <= next_row < 4 and 0 <= next_col < 4:
            eat_fish = 0
            if (next_row, next_col) not in path:
                if moving_fish.get((next_row, next_col)):
                    eat_fish = len(moving_fish.get((next_row, next_col)))
                move_shark(next_row, next_col, step + 1, path + [(next_row, next_col)], eaten_fish + eat_fish)
            else:
                move_shark(next_row, next_col, step + 1, path, eaten_fish)



# S번 동안 마법을 연습한다.
for turn in range(S):
    # 복제 마법 시전. 지금 딕셔너리를 복사해둔다.
    copy_fish = fish.copy()
    moving_fish = dict()
    fish_cnt = len(fish)

    # 모든 물고기가 한마리씩 이동한다.
    for fish_r, fish_c in fish:
        for fish_d in fish.get((fish_r, fish_c)):
            move_fish(fish_r, fish_c, fish_d)
    max_eaten_fish_path, max_eaten_fish_cnt = [], -1
    # print("물고기 움직임")
    # print(moving_fish)
    # 가장 물고기를 많이 제거하는 경로를 찾아온다.
    move_shark(shark_row, shark_col, 0, [], 0)
    # print("상어가 지나감")
    # print("상어 경로 ", max_eaten_fish_path)

    for shark_pos in max_eaten_fish_path:
        if moving_fish.get(shark_pos):
            moving_fish.pop(shark_pos)
            fish_smell[shark_pos[0]][shark_pos[1]] = 3
    # print("제거된 결과", moving_fish)
    # print("상어 위치", shark_row, shark_col)

    # 냄새 제거
    for r in range(4):
        for c in range(4):
            if fish_smell[r][c]:
                fish_smell[r][c] -= 1

    # 움직인 결과로 덮어씌운다.

    fish = moving_fish.copy()
    # print("복사해둔 원본", copy_fish)
    # 복제해둔 물고기들 copy_fish[copy] = [방향, 방향..] 보면서
    for copy in copy_fish:
        if fish.get(copy):
            # 현재 물고기 맵에 그 위치에 물고기가 있는지 보고 추가한다.
            fish[copy] += copy_fish.get(copy)
        else:
            fish[copy] = copy_fish.get(copy)
    # print(f"{turn}번째 연습 결과")
    # for line in fish:
    #     print(*line, fish.get(line))

# 연습 마침
fish_cnt = 0
for pos in fish:
    fish_cnt += len(fish.get(pos))
print(fish_cnt)