"""
하루종일 시간 + 테케 4에서 틀려서 포기함.
"""

import sys
from collections import deque
from copy import deepcopy

sys.stdin = open("input.txt", "r")

N, M, K = map(int, sys.stdin.readline().split())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

ball_dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 동 북 서 남
c_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
rc_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 북 서 남 동


class Team:
    def __init__(self, team_head, team_tail, team_body, team_direction):
        self.h_r = team_head[0]
        self.h_c = team_head[1]
        self.t_r = team_tail[0]
        self.t_c = team_tail[1]
        self.body = team_body
        self.direction = team_direction


def print_grid():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for line in grid:
        print(*line)

    for i in range(M):
        team = teams[i]
        print(f"{i+1}번 팀정보 => 머리 : {team.h_r, team.h_c} / 꼬리 : {team.t_r, team.t_c} / 몸통 : {team.body} / 방향 : {team.direction}")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")


def move():
    moved_grid = deepcopy(grid)
    for idx in range(M):
        team = teams[idx]
        r, c = team.h_r, team.h_c
        body, body_size = team.body[:], len(team.body)
        # 시계방향 / 반시계방향
        if team.direction == 1:
            dirs = c_dir
        else:
            dirs = rc_dir
        d = 0

        # 머리의 방향
        for _ in range(4):
            n_r = r + dirs[d][0]
            n_c = c + dirs[d][1]
            if 0 <= n_r < N and 0 <= n_c < N and grid[n_r][n_c] != 0:
                # 머리 이동
                moved_grid[n_r][n_c] = 1
                grid[r][c] = 4
                team.h_r, team.h_c = n_r, n_c
                break
            d = (d+1) % 4

        # 몸통 한 칸씩 이동
        for b_idx in range(body_size):
            for _ in range(4):
                r, c = body[b_idx][0], body[b_idx][1]
                new_r = r + dirs[d][0]
                new_c = c + dirs[d][1]
                if 0 <= new_r < N and 0 <= new_c < N and grid[new_r][new_c] in [1, 4]:
                    body[b_idx] = (new_r, new_c)
                    moved_grid[new_r][new_c] = 2
                    grid[r][c] = 4
                    break
                d = (d+1) % 4
        last_body = team.body[body_size-1]
        grid[last_body[0]][last_body[1]] = 2
        team.body = body

        # 꼬리 이동
        for _ in range(4):
            new_tail_r = team.t_r + dirs[d][0]
            new_tail_c = team.t_c + dirs[d][1]
            if 0 <= new_tail_r < N and 0 <= new_tail_c < N:
                if grid[new_tail_r][new_tail_c] == 2:
                    moved_grid[new_tail_r][new_tail_c] = 3
                    if moved_grid[team.t_r][team.t_c] != 1:
                        moved_grid[team.t_r][team.t_c] = 4
                    team.t_r, team.t_c = new_tail_r, new_tail_c
                    break
            d = (d + 1) % 4

    return moved_grid


def throw(now_round):
    global answer
    # 어떤 방향인지
    edge = now_round // N
    # 어느 줄인지
    line = now_round % N

    first_r, first_c = -1, -1
    # 오른쪽으로
    if edge == 0:
        for ball_col in range(N):
            if 1 <= grid[line][ball_col] <= 3:
                first_r, first_c = line, ball_col
                print(now_round+1, "판 →→→→→→→→→→→→→→→→→→→→→→→", first_r, first_c)
                break
    # 위쪽으로
    elif edge == 1:
        for ball_row in range(N-1, -1, -1):
            if 1 <= grid[ball_row][line] <= 3:
                first_r, first_c = ball_row, line
                print(now_round+1, "판 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑",first_r, first_c)
                break
    # 왼쪽으로
    elif edge == 2:
        for ball_col in range(N-1, -1, -1):
            if 1 <= grid[line][ball_col] <= 3:
                first_r, first_c = line, ball_col
                print(now_round+1, "판 ←←←←←←←←←←←←←←←←←←←←←←←", first_r, first_c)
                break
    # 아래쪽으로
    else:
        for ball_row in range(N):
            if 1 <= grid[ball_row][line] <= 3:
                first_r, first_c = ball_row, line
                print(now_round+1, "판 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓", first_r, first_c)
                break

    if (first_r, first_c) != (-1, -1):
        answer += get_score(first_r, first_c)
        print("@@@@@@@@@@@@ 현재 점수 : ", answer)
    else:
        print(f"~~~~~~~~~~~~ {now_round+1}판은 미스 ~~~~~~~~~~~")


def get_score(find_r, find_c):
    # 어느 팀 소속인지 찾아야한다.
    found = False
    score = 0
    for i in range(M):
        team = teams[i]
        team_body = team.body
        body_size = len(team_body)
        if team.h_r == find_r and team.h_c == find_c:
            print(i+1, "번 팀의 머리에 맞았네요")
            score, found = 1, True
        elif team.t_r == find_r and team.t_c == find_c:
            print(i+1, "번 팀의 꼬리에 맞았네요")
            score, found = body_size + 2, True
        else:
            for idx in range(body_size):
                if team_body[idx][0] == find_r and team_body[idx][1] == find_c:
                    score, found = body_size + 1, True
                    print(i+1, "번 팀의몸통에 맞았네요")
                    break
        if found:
            # 뒤집기
            team.direction = -team.direction
            temp_r, temp_c = team.h_r, team.h_c
            team.h_r, team.h_c = team.t_r, team.t_c
            team.t_r, team.t_c = temp_r, temp_c
            grid[team.h_r][team.h_c] = 1
            grid[team.t_r][team.t_c] = 3
            team.body = team_body[body_size-1:: -1]
            break

    return score ** 2

teams, team_idx = list([] for _ in range(M)), 0
visited = [[0] * N for _ in range(N)]
answer = 0


## 맵을 돌며 팀 정보를 저장한다.
for r in range(N):
    for c in range(N):
        value = grid[r][c]
        if not value:
            # 0이면 넘어가기
            continue
        if visited[r][c]:
            # 이미 갔던 곳이면 넘어가기
            continue
        # 이제 하나의 팀 정보를 저장할 것이다.
        # 연결된 1,2,3,4를 찾아서 저장해야한다.
        q = deque([(r, c)])
        visited[r][c] = 1

        head_r, head_c = 0, 0
        tail_r, tail_c = 0, 0
        body = []
        cnt = 0

        while q:
            row, col = q.popleft()
            value = grid[row][col]

            if 0 < value < 4:
                cnt += 1
            # 머리 저장
            if value == 1:
                head_r, head_c = row, col
            elif value == 3:
                # 꼬리 기록
                tail_r, tail_c = row, col
            elif value == 2:
                body.append((row, col))
            for dr, dc in c_dir:
                next_row = row + dr
                next_col = col + dc

                if 0 <= next_row < N and 0 <= next_col < N \
                        and not visited[next_row][next_col] \
                        and grid[next_row][next_col]:
                    # 격자 안에 있으며, 방문한 적도 없고, 0이 아니라면 팀 탐색 가능
                    visited[next_row][next_col] = 1
                    q.append((next_row, next_col))
                    break
        # 팀 정보 저장하기, 우선 처음엔 그냥 다 시계방향으로 저장
        teams[team_idx] = Team((head_r, head_c), (tail_r, tail_c), body, 1)
        team_idx += 1

# 이제서야 초기화 끝
print_grid()
print("////////////// 초기화 했습니다 //////////////")
for game in range(K):
    # 팀마다 머리를 따라 한칸씩 이동
    grid = deepcopy(move())
    print("-------------- 움직였습니다 ------------")
    print_grid()
    # 공 던지기
    throw(game)
    print("------------ 공 던졌습니다 ------------")
    print_grid()

print(answer)