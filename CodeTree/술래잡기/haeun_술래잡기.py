# 격자 크기, 도망자 수, 나무의 수, 턴 수
N, M, H, K = map(int, input().split())

# 상-우-하-좌(달팽이 방향 순서)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 처음에 도망자 방향을 2차원 배열에 기록했더니 한 자리에 여러명인 경우가 커버가 안됨.
run_pos = [(0, 0) for _ in range(M)]  # 도망자 위치 배열[(x, y), (x, y)..]
run_dir = [0] * M  # 도망자 방향 배열[1, 2, 1, 2, 2 ..]

# 나무 유무를 판별하는 2차원 배열
tree = [[0] * N for _ in range(N)]

# 술래 변수 설정
s_row, s_col = (N-1) // 2, (N-1) // 2  # 술래의 위치
s_dir = 0  # 술래의 방향 (0상, 1우, 2하, 3좌)
s_snail = True  # True : 센터 -> 0,0 / False : 0,0 -> 센터
s_dis = 0  # 술래가 현재 이동한 거리 (s_dis_max에 도달하면 0으로 리셋)
s_dis_max = 1  # 술래가 현재 이동할 수 있는 최대 거리
s_max_cnt = 0  # 술래가 s_dis_max에 도달한 횟수. 2번 도달하면 s_dis_max값이 바뀐다.


# def print_run():
#     grid = [[0] * N for _ in range(N)]
#     print("----------도망자------------")
#     run = len(run_pos)
#     for i in range(run):
#         r, c = run_pos[i]
#         grid[r][c] += 1
#
#     for line in grid:
#         print(*line)
#
#     # for i in range(run):
#     #     print(f"{i + 1}번째 도망자 위치 : {run_pos[i]}, 방향 : {run_dir[i]}")
#
#
# def print_sulae():
#     grid = [[0] * N for _ in range(N)]
#     print("------------술래------------")
#     print(f"술래 위치 : {s_row}행 {s_col}열")
#     print(f"술래 방향 : {s_dir}, 달팽이 : {s_snail}")
#     print(f"술래 거리 : {s_dis}, 최대값 : {s_dis_max}, 도달 횟수 : {s_max_cnt}")
#     grid[s_row][s_col] = 1
#     for line in grid:
#         print(*line)



def init():
    # 도망자 입력
    for i in range(M):
        x, y, d = map(int, input().split())
        # d가 1이면 초기값이 오른쪽, 2면 아래쪽이 된다.
        # 달팽이 방향에 맞춰 만든 delta배열에 그대로 사용할 수 있다.
        run_pos[i] = (x-1, y-1)
        run_dir[i] = d

    # 나무 입력
    for _ in range(H):
        x, y = map(int, input().split())
        tree[x-1][y-1] = 1


def runaway_move():
    # 도망자 이동
    runs = len(run_pos)
    for i in range(runs):
        row, col = run_pos[i]
        d = run_dir[i]
        if abs(s_row - row) + abs(s_col - col) <= 3:
            next_r, next_c = row + dr[d], col + dc[d]
            if 0 <= next_r < N and 0 <= next_c < N:
                if (s_row, s_col) != (next_r, next_c):
                    run_pos[i] = (next_r, next_c)
            else:
                d = (d + 2) % 4
                run_dir[i] = d
                next_r, next_c = row + dr[d], col + dc[d]
                if (s_row, s_col) != (next_r, next_c):
                    run_pos[i] = (next_r, next_c)


def s_move():
    global s_row, s_col, s_snail, s_dir, s_dis, s_dis_max, s_max_cnt

    # 술래 방향으로 한칸 이동
    s_row += dr[s_dir]
    s_col += dc[s_dir]

    # 현재 이동한 거리 증가
    s_dis += 1
    if s_dis == s_dis_max:
        s_dis = 0  # 현재 이동 거리 초기화(0부터 다시 셀거니깐)
        s_dir = (s_dir + 1 if s_snail else s_dir-1) % 4  # 목적지 방향에 따라 술래의 방향도 다르게 바뀜
        s_max_cnt += 1  # 현재 가능한 최대 거리에 도달했다면 횟수 증가
        if s_max_cnt == 2:
            s_max_cnt = 0  # 초기화
            # 2번 도달했다면 최대 거리 늘려야함
            s_dis_max += 1 if s_snail else -1

    if (s_row, s_col) == (0, 0):
        # 아래로 내려가고, 역으로 돌아간다.
        s_dir, s_snail = 2, False
        s_dis, s_dis_max = 0, N-1
        s_max_cnt = -1  # 역 방향은 N-1을 아래, 오른쪽, 위로 3번 가야한다.
    elif (s_row, s_col) == ((N-1)//2, (N-1)//2):
        # 위로 올라가고, 정방향으로 간다.
        s_dir, s_snail = 0, True
        s_dis, s_dis_max = 0, 1


def s_catch(turn):
    run = len(run_pos)
    caught = []
    for i in range(3):
        # 시야 위치
        row, col = s_row + i * dr[s_dir], s_col + i * dc[s_dir]
        if 0 <= row < N and 0 <= col < N and not tree[row][col]:
            # 트리가 있지 않은 경우
            # 한 자리에 여러명이 있을 수 있으므로, 그냥 list.index를 쓰면 안된다.
            for idx in range(run):
                if (row, col) == run_pos[idx]:
                    caught.append(idx)

    # 잡은 순서 정렬안해줘서 틀림...
    # list니까 뒤에서부터 제거하면 된다고 생각했는데, 애초에 caught에 들어가는 idx가
    # 순서대로 들어가고 있을리 없었던 것이다.
    caught.sort(reverse=True)
    for dead in caught:
        # 찾은 도망자를 제거한다.
        run_pos.pop(dead)
        run_dir.pop(dead)

    return turn * len(caught)


def solution():
    answer = 0
    init()
    for turn in range(1, K+1):
        runaway_move()
        s_move()
        answer += s_catch(turn)
    print(answer)


solution()