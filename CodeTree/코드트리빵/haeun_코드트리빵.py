"""
230118
- 해설봄. '최단거리'를 4방향 중 어떻게 찾아가라는지 모르겠어서, DFS를 사용해야하나 고민했음.
- 편의점을 기준으로 베이스캠프를 찾는 과정이 힌트였나봄. 편의점을 기준으로 내 위치를 찾아와서,
  그 위치의 상,좌,우,하 순으로 보면서 제일 짧은 거리의 위치를 찾으면 되는 것.
  역시 삼성에서 DFS가 나올리 없지..
- 사람이 아직 남은건 어떻게 체크하나 봤는데, 무조건 효율적으로 해보겠다고 따로 뺄 필요 없이
  어차피 m의 최대값은 30이니 다 하나씩 봐도 무방하다...
- 충격사건... people은 값이 변한다고 [r, c]로 저장하고 편의점은 값이 변하지 않는다고 (r, c)로
  저장해서 사람의 좌표와 편의점 좌표 동등비교가 이상하게 되었다.. 진짜 미침...^^...
"""
from collections import deque

# 최대값
INT_MAX = 987654321

n, m = map(int, input().split())

# 지도, 델타 배열
# 지도에서 갈 수 있는 곳은 0, 베이스캠프는 1, 갈 수 없는 곳은 2
grid = list(list(map(int, input().split())) for _ in range(n))
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 각 사람별 목표 편의점 위치, 현재 위치
stores = []
for _ in range(m):
    r, c = map(int, input().split())
    stores.append((r-1, c-1))
people = list((-1, -1) for _ in range(m))

# 현재 시간
cur_time = 0

# bfs에서 사용할 변수
visited = [[0] * n for _ in range(n)]


# 해당 좌표가 범위 내인지 본다.
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


# bfs 함수. 베이스캠프, 사람 다 필요 없고 "편의점" 기준으로만 계산하고 반환한다.
def bfs(i):
    s_r, s_c = stores[i]

    # 초기화를 이렇게 해주지 않으면.. 다른 변수로 사용한다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    visited[s_r][s_c] = 1
    q = deque([(s_r, s_c)])

    while q:
        now_r, now_c = q.popleft()

        for d in range(4):
            new_r, new_c = now_r + dr[d], now_c + dc[d]
            # 범위를 넘지 않고, 방문하지 않았고, 갈 수 있는 곳
            if in_range(new_r, new_c) and not visited[new_r][new_c] and grid[new_r][new_c] != 2:
                visited[new_r][new_c] = visited[now_r][now_c] + 1
                q.append((new_r, new_c))


# 1번, 2번 행동을 실행할 함수
def move_to_store():
    # 각 사람들을 보면서 움직일 사람인지 아닌지 체크한다.
    for idx in range(m):
        if people[idx] != (-1, -1) and people[idx] != stores[idx]:
            bfs(idx)
            p_r, p_c = people[idx]
            m_r, m_c = -1, -1
            min_distance = INT_MAX

            # 상,좌,우,하 중 갈 수 있는 곳을 찾는다.
            for d in range(4):
                n_r, n_c = p_r + dr[d], p_c + dc[d]
                if in_range(n_r, n_c) and 0 < visited[n_r][n_c] < min_distance:
                    m_r, m_c = n_r, n_c
                    min_distance = visited[n_r][n_c]

            # 최소거리로 간다.
            people[idx] = (m_r, m_c)

            # 여기가 편의점인지 본다.(2번 행동)
            if people[idx] == stores[idx]:
                grid[m_r][m_c] = 2


def basecamp(idx):
    # 가장 가까운 베이스 캠프를 찾는다.
    b_r, b_c = -1, -1
    min_distance = INT_MAX
    # 1. 우선 bfs를 돌린다.
    bfs(idx)
    # 2. 가장 가까운 베이스 캠프를 찾는다.
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1 and 0 < visited[row][col] < min_distance:
                b_r, b_c = row, col
                min_distance = visited[row][col]

    # 해당 베이스 캠프로 이동하고, 이제 그 곳은 갈 수 없는 곳이 된다.
    people[idx] = (b_r, b_c)
    grid[b_r][b_c] = 2


def done():
    for i in range(m):
        if people[i] != stores[i]:
            return False
    return True


# 모든 사람이 편의점에 갔다면 끝난다.
while not done():
    # 1분이 경과하고
    cur_time += 1

    # 1 & 2 번 행동 실행 => 격자에 사람이 있어야 한다.
    move_to_store()

    # cur_time <= m 이라면 cur_time 번째 사람이 베이스캠프에 간다.
    if cur_time <= m:
        basecamp(cur_time-1)



print(cur_time)