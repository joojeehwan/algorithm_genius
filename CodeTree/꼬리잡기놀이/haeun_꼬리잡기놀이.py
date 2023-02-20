from collections import deque

# 입력
N, M, K = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))

# 루트 찾을 때 필요한 2차원 배열 (2, 4 때문에)
visited = [[0] * N for _ in range(N)]

# 방향 변수
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# 팀에 필요한 변수들
team_score = [0] * M
team_member = [0] * M
team_dir = [True] * M
team_route = list(deque() for _ in range(M))
team_num = [[-1] * N for _ in range(N)]


# 임시 출력 함수
# def print_team():
#     for tm in range(M):
#         print(f"{tm} 팀 => 인원 {team_member[tm]} , 방향 : {team_dir[tm]}, 점수 : {team_score[tm]}")
#         print(f"경로 + {team_route[tm]}")
#     print()


# 팀 경로 만들기
def make_team_route():
    # 머리를 찾을 때 마다 증가시킨다.
    team_idx = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                visited[r][c] = 1  # 방문 처리
                # 머리의 위치를 경로의 제일 처음에 저장한다.
                team_route[team_idx].append((r, c))
                team_member[team_idx] = 1  # 일단 한명 찾음

                # 경로를 찾아보도록 하자
                now_num = 1
                queue = deque([(r, c)])

                while queue:
                    now_r, now_c = queue.popleft()
                    team_num[now_r][now_c] = team_idx

                    for d in range(4):
                        next_r, next_c = now_r + dr[d], now_c + dc[d]
                        if not (0 <= next_r < N and 0 <= next_c < N): continue
                        # 같거나, 1이 높은 곳 이면서 방문하지 않은 곳은 하나 뿐이다.
                        if (now_num == board[next_r][next_c] or now_num + 1 == board[next_r][next_c]) and \
                                not visited[next_r][next_c]:

                            # 팀원 수도 계속 세줘야한다. 4는 팀원이 아니니깐 필요없어
                            now_num = board[next_r][next_c]
                            if now_num <= 3:
                                team_member[team_idx] += 1

                            queue.append((next_r, next_c))
                            team_route[team_idx].append((next_r, next_c))
                            visited[next_r][next_c] = 1
                            # 다른 방향은 볼 필요가 없다!
                            break
                team_idx += 1


# 움직여
def move():
    # 원형 배열
    for t in range(M):
        # 방향이 True면 처음 머리가 머리다.
        # 뒤에서 떼서 앞에 붙인다.
        if team_dir[t]:
            team_route[t].rotate(1)
        # 방향이 False면 처음 머리가 꼬리다.
        # 앞에서 떼서 뒤에 붙인다.
        else:
            team_route[t].rotate(-1)


def throw_ball(rnd):
    # [@@@@@ 디버깅으로 틀린 원인 찾아냄 @@@@@]
    # rnd // N 로 공의 방향을 정할 것이다.
    # 하지만 4N이 넘는 경우 4방향 인덱스를 벗어난다.
    # 이를 방지하기 위해 라운드 수를 0 ~ 4N-1 범위로 미리 나눠놓자.
    rnd %= 4*N
    b_dir = rnd // N
    # 방향에 따라 출발 위치가 다르다.
    b_row, b_col = 0, 0
    if b_dir == 0:
        b_row, b_col = rnd % N, 0
    elif b_dir == 1:
        b_row, b_col = N-1, rnd % N
    elif b_dir == 2:
        # [@@@@@ 디버깅으로 틀린 원인 찾아냄 @@@@@]
        # 라운드의 수가 올라갈 수록 행은 밑에서 위로 올라간다.
        # 행 계산식을 잘못 만들었다.(b_dir = 3 도 마찬가지)
        b_row, b_col = N * (rnd // N + 1) - rnd - 1, N-1
    elif b_dir == 3:
        b_row, b_col = 0, N * (rnd // N + 1) - rnd - 1

    # 행은 정해져있고, 열만 움직이면서 보면 된다.
    for _ in range(N):
        if team_num[b_row][b_col] >= 0:
            team_idx = team_num[b_row][b_col]
            team_cnt = team_member[team_idx]
            if (b_row, b_col) in team_route[team_idx]:
                person = team_route[team_idx].index((b_row, b_col))
                if person < team_cnt:
                    return team_idx, person
        b_row += dr[b_dir]
        b_col += dc[b_dir]
    return -1, -1


def get_score(team, idx):
    if team_dir[team]:
        # 처음 머리 방향이 유지된 상태다.
        team_score[team] += (idx + 1) ** 2
    else:
        # 처음 머리가 꼬리로 간 상태다. 뒤에서 부터 센다.
        # [@@@@@ 디버깅으로 틀린 원인 찾아냄 @@@@@]
        # 팀원수 - 인덱스에 + 1을 해서 틀렸다. 인덱스는 0부터라서 이게 맞다...
        team_score[team] += (team_member[team] - idx) ** 2
    # 볼에 맞았으니 방향을 바꾼다.
    team_dir[team] = not team_dir[team]


def solution():
    make_team_route()
    for rnd in range(K):
        move()
        team, index = throw_ball(rnd)
        if team >= 0:
            get_score(team, index)

    print(sum(team_score))


solution()