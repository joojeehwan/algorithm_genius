"""
- 풀이시간 3:08 , 시작 23:45 , 끝 2:53
- ㅅㅂ
"""

from collections import deque

N, M, K = map(int, input().split())
# [🤬] N을 M으로 쓰는 이상한 실수
grid = list(list(map(int, input().split())) for _ in range(N))

# 공격한 시점 기록
record = [[0] * M for _ in range(N)]

# 공격자, 대상자
a_r, a_c = -1, -1
v_r, v_c = -1, -1


# 부숴지지 않은 포탑의 수를 센다.
def count_alive():
    alive = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c]:
                alive += 1
    return alive


# 가장 공격력이 낮은 포탑들을 반환한다.
def find_weakest():
    weaks = []
    point = 5001

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                continue
            if grid[r][c] < point:
                point = grid[r][c]
                weaks = [(r, c)]
            elif grid[r][c] == point:
                weaks.append((r, c))

    return weaks


# 가장 공격력이 높은 포탑들을 반환한다.
def find_strongest():
    strongs = []
    point = 1

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                continue
            if r == a_r and c == a_c:
                continue
            if grid[r][c] > point:
                point = grid[r][c]
                strongs = [(r, c)]
            elif grid[r][c] == point:
                strongs.append((r, c))

    return strongs


# 공격력이 낮은 포탑들 중 최근에 공격한 포탑들을 반환한다.
def find_recents(weak_turrets):
    recents = []
    recent = -1
    for r, c in weak_turrets:
        if record[r][c] > recent:
            recent = record[r][c]
            recents = [(r, c)]
        elif record[r][c] == recent:
            recents.append((r, c))
    # 내 생각엔 아무리 생각해봐도 2개일 수 없지만
    # 가장 초기 시점이라고 생각하고 만든다...
    return recents


# 공격력이 높은 포탑들 중 가장 공격한지 오래된 포탑들을 반환한다.
def find_olds(strongs):
    olds = []
    old = 1001

    for r, c in strongs:
        if record[r][c] < old:
            old = record[r][c]
            olds = [(r, c)]
        elif record[r][c] == old:
            olds.append((r, c))
    # 내 생각엔 아무리 생각해봐도 2개일 수 없지만
    # 가장 초기 시점이라고 생각하고 만든다...
    return olds


# big_or_small => True면 합이 큰거, False면 합이 작은거
def find_row_col(turrets, big_or_small):
    row_col = []
    sum_r_c = 0 if big_or_small else 100

    if big_or_small:
        for r, c in turrets:
            if sum_r_c < r + c:
                sum_r_c = r+c
                row_col = [(r, c)]
            elif sum_r_c == r + c:
                row_col.append((r, c))
    else:
        for r, c in turrets:
            if sum_r_c > r + c:
                sum_r_c = r + c
                row_col = [(r, c)]
            elif sum_r_c == r + c:
                row_col.append((r, c))

    return row_col


# big이 True면 큰 열을 찾는 것이고, False면 작은 열을 찾는 것이다.
def find_col(turrets, big):
    num = 0 if big else 11

    col = [-1, -1]

    if big:
        for r, c in turrets:
            if c > num:
                num = c
                col = [r, c]
    else:
        for r, c in turrets:
            if c < num:
                num = c
                col = [r, c]

    return col


# 공격자 선정
# 부서지지 않은 포탑 중 가장 약한 포탑을 선정
def select_attacker():
    global a_r, a_c
    # 1. 공격력이 가장 낮아야 한다.
    weaks = find_weakest()

    # 2. 가장 최근에 공격한 포탑이어야 한다.
    weak_cnt = len(weaks)
    if weak_cnt > 1:
        recents = find_recents(weaks)
        # 3. 행+열의 합이 가장 큰 포탑이어야 한다.
        if len(recents) > 1:
            row_col_sums = find_row_col(recents, True)
            if len(row_col_sums) > 1:
                # 4. 열 값이 가장 큰 포탑이어야 한다.
                a_r, a_c = find_col(row_col_sums, True)
            else:
                a_r, a_c = row_col_sums[0]
        else:
            a_r, a_c = recents[0]
    else:
        a_r, a_c = weaks[0]



# 공격 당할 대상 찾기
# 미친거같음
def select_victim():
    global v_r, v_c
    # 1. 공격력이 가장 강해야 한다.
    strongs = find_strongest()

    strong_cnt = len(strongs)
    if strong_cnt > 1:
        # 2. 가장 공격한지 오래된 포탑이어야 한다.
        olds = find_olds(strongs)
        if len(olds) > 1:
            # 3. 행+열의 합이 가장 작은 포탑이어야 한다.
            row_col_sums = find_row_col(olds, False)
            if len(row_col_sums) > 1:
                # 4. 열 값이 가장 작은 포탑이어야 한다.
                v_r, v_c = find_col(row_col_sums, False)
            else:
                v_r, v_c = row_col_sums[0]
        else:
            v_r, v_c = olds[0]
    else:
        v_r, v_c = strongs[0]


# [🤬] 시간 초과
# dfs -> bfs로 변경
# 왜 시간초과 나고 난리야
def lazer():
    visited = [[0] * M for _ in range(N)]
    routes = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    q = deque([(a_r, a_c)])
    visited[a_r][a_c] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = (r + dr) % N
            nc = (c + dc) % M
            if visited[nr][nc]:
                continue
            if grid[nr][nc] == 0:
                continue
            visited[nr][nc] = 1
            routes[nr][nc] = [r, c]  # 경로 기록하기
            q.append((nr, nc))

    if visited[v_r][v_c]:
        # 레이저 공격
        pr, pc = routes[v_r][v_c]
        # [🤬] 와 pr != a_r and pc != a_c 했다가 미쳐버리는줄 진짜...
        while (pr, pc) != (a_r, a_c):
            diff = grid[pr][pc] - (grid[a_r][a_c] // 2)
            grid[pr][pc] = diff if diff > 0 else 0
            peace[pr][pc] = False
            pr, pc = routes[pr][pc]
        return True
    else:
        return False


# 공격자 위치, 대상자 위치
def attack_around():
    # dfs -> 시간 초과

    # 레이저인지, 포탄인지 정해야한다.
    # [🤬] 공격 도달점은 빼고 반환하니깐 바로 붙어있는 경우
    if not lazer():
        # 포탄 공격
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
            nr = (v_r + dr) % N
            nc = (v_c + dc) % M
            if nr == a_r and nc == a_c:
                continue
            if grid[nr][nc] == 0:
                continue
            diff = grid[nr][nc] - (grid[a_r][a_c] // 2)
            grid[nr][nc] = diff if diff > 0 else 0
            peace[nr][nc] = False


# 공격에 휘말리지 않은 애들은 +1
def fix_turret():
    for r in range(N):
        for c in range(M):
            if peace[r][c] and grid[r][c] > 0:
                grid[r][c] += 1


# 가장 공격력이 높은 포탑 그냥 따로 찾아줌
def find_answer():
    answer = 0
    for r in range(N):
        for c in range(M):
            answer = max(answer, grid[r][c])
    return answer


def solution():
    global peace
    time = 1
    while time <= K and count_alive() > 1:
        peace = [[True] * M for _ in range(N)]

        # 공격자 처리
        select_attacker()
        grid[a_r][a_c] += (N+M)
        peace[a_r][a_c] = False
        record[a_r][a_c] = time

        # 공격 대상자 찾기
        select_victim()

        # 레이저 / 포탄인지 판단하고 주의 포탑 처리
        attack_around()

        # 공격 대상자 처리(위에 레이저에서 짤림)
        diff = grid[v_r][v_c] - grid[a_r][a_c]
        grid[v_r][v_c] = diff if diff > 0 else 0
        peace[v_r][v_c] = False

        fix_turret()
        time += 1

    print(find_answer())

solution()