
# MAP에 번호와 방향을 같이 넣어주고, fish에 번호에 해당하는 물고기 index를 넣어줌
MAP = [[] for _ in range(4)]
fish = [0] * 17
k = 0
for _ in range(4):
    lst = list(map(int, input().split()))
    for i in range(0, 8, 2):
        num, dir = lst[i], lst[i + 1] - 1
        MAP[k].append([num, dir])
        fish[num] = [k, i // 2]
    k += 1

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

# 상어가 0,0 의 물고기를 먹음
shark_i, shark_j, shark_dir = 0, 0, MAP[0][0][1]
eat = MAP[0][0][0]
fish[MAP[0][0][0]] = []
MAP[0][0] = -1

# 물고기를 이동시키는 함수
def move():

    # 1번부터 물고기를 이동시킴
    for i in range(1, 17):
        if not fish[i]:  # 물고기가 없으면 패스
            continue
        fish_i, fish_j = fish[i]
        dir = MAP[fish_i][fish_j][1]
        for k in range(8):
            next_i = fish_i + di[(dir + k) % 8]
            next_j = fish_j + dj[(dir + k) % 8]

            # MAP을 벗어나거나 상어가 있는 칸이면 이동 X
            if next_i < 0 or next_j < 0 or next_i >= 4 or next_j >= 4:
                continue
            if MAP[next_i][next_j] == -1:
                continue

            dir = (dir + k) % 8
            # 이동할 수 있으면 이동 (한 번만 하고 break)
            if MAP[next_i][next_j] == 0:  # 빈칸이면 바로이동
                MAP[next_i][next_j] = [MAP[fish_i][fish_j][0], dir]
                MAP[fish_i][fish_j] = 0
                fish[MAP[next_i][next_j][0]] = [next_i, next_j]
            else:
                temp = [MAP[fish_i][fish_j][0], dir]
                MAP[fish_i][fish_j] = MAP[next_i][next_j]
                MAP[next_i][next_j] = temp
                fish[MAP[fish_i][fish_j][0]] = [fish_i, fish_j]
                fish[MAP[next_i][next_j][0]] = [next_i, next_j]

            break

ans = eat

# 상어가 물고리를 잡아먹는 최대를 구하기 위한 dfs 함수
def dfs(now_i, now_j, dir, eat):
    global ans, MAP, fish

    move()  # 일단 물고기를 모두 이동시킴
    for k in range(1, 4):
        next_i = now_i + di[dir] * k
        next_j = now_j + dj[dir] * k

        # 범위를 벗어나거나 물고기가 없는 칸이면 이동불가
        if next_i < 0 or next_j < 0 or next_i >= 4 or next_j >= 4:
            ans = max(ans, eat)
            return
        if MAP[next_i][next_j] == 0:                # 먹을 물고기가 없으면 일단 다음 칸 검사
            continue

        # 배열 복사해두기
        dfs_MAP = [MAP[k][:] for k in range(4)]
        dfs_fish = fish[:]
        # 먹은 물고기의 번호와 방향을 기록해주고 먹은 건 -1로 바꿔줌
        eaten_fish = MAP[next_i][next_j]
        MAP[next_i][next_j] = -1
        MAP[now_i][now_j] = 0
        fish[eaten_fish[0]] = []
        dfs(next_i, next_j, eaten_fish[1], eat + eaten_fish[0])
        MAP, fish = dfs_MAP, dfs_fish       # 원상복구

dfs(shark_i, shark_j, shark_dir, eat)

print(ans)