N, M, K = map(int, input().split())

grid = list(list(map(int, input().split())) for _ in range(N))
priority = [list() for _ in range(M+1)]
sharks = [[0, 0, 0] for _ in range(M+1)] # index = 상어번호 | 행, 열, 방향
left_shark = M-1
answer = 0
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

# 냄새 빠지기 까지 남은 시간
time = [[0] * N for _ in range(N)]

# 각 상어의 초기 방향 저장
dirs = list(map(int, input().split()))
for i in range(M):
    sharks[i+1][2] = dirs[i]

# 각 상어의 번호에 따라 5줄씩 우선순위 저장(방향 1,2,3,4 그대로 쓰려고)
for i in range(1, M+1):
    priority[i].append([0, 0, 0, 0])
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))

# 각 상어의 위치 + 냄새 기록 + 냄새 시간 K 초기화
for x in range(N):
    for y in range(N):
        if grid[x][y]:
            num = grid[x][y]
            sharks[num][0], sharks[num][1] = x, y
            time[x][y] = K

while left_shark:
    answer += 1
    # 냄새를 빼준다.
    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                grid[r][c] -= 1

    # 상어를 이동한다. 빈곳에는 동시에 여러 마리가 갈 수 있어서 바로 grid에 기록하면 안된다.
    moving = dict()
    for s_idx in range(1, M+1):
        if not sharks[s_idx]:
            continue
        s_row, s_col, s_dir = sharks[s_idx]
        move_priority = priority[s_idx][s_dir]
        empty_found = False

        for d in move_priority:
            new_row = s_row + dr[d]
            new_col = s_col + dc[d]
            if not (0 <= new_row < N and 0 <= new_col < N):
                continue
            # 빈칸이 있는지 본다.
            if not grid[new_row][new_col]:
                if moving.get((new_row, new_col)):
                    moving[(new_row, new_col)].append((s_idx, d))
                else:
                    moving[(new_row, new_col)] = [(s_idx, d)]
                empty_found = True
                break
        # 빈칸이 없다면 자신의 냄새가 있는 곳으로 가야한다.
        if not empty_found:
            for d in move_priority:
                new_row = s_row + dr[d]
                new_col = s_col + dc[d]
                if not (0 <= new_row < N and 0 <= new_col < N):
                    continue
                # 자기 냄새와 같은지 본다.
                if grid[new_row][new_col] == s_idx:
                    # 새로 업데이트 해준다. 굳이 또 움직여줄 필요는 없다.
                    sharks[s_idx] = [new_row, new_col, d]
                    time[new_row][new_col] = K
                    break

    for m_row, m_col in moving:
        here_sharks = moving.get((m_row, m_col))
        if len(here_sharks) > 1:
            s_idx, m_dir = 999, 0
            for s_i, s_d in here_sharks:
                if s_i < s_idx:
                    s_idx, m_dir = s_i, s_d

            for s_i, s_d in here_sharks:
                if s_i != s_idx:
                    sharks[s_i] = []
                    left_shark -= 1
        else:
            s_idx, m_dir = here_sharks[0]
        grid[m_row][m_col] = s_idx
        time[m_row][m_col] = K
        sharks[s_idx] = [m_row, m_col, m_dir]

print(answer)