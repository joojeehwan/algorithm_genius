"""
푼 시간 : 3시간
시간 : 2615ms
공간 : 62MB
"""
from collections import deque

N = int(input())  # 격자의 크기 입력값
art = [list(map(int, input().split())) for _ in range(N)]  # N*N 격자의 색상 입력값

answer = 0  # 예술성 총 점수 저장(초기 + 1회 + 2회 + 3회)

# 델타배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 범위 내에 있는지 확인하는 함수
def in_range(row, col):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False


# 각 그룹의 정보를 저장하는 함수. 그림을 회전할 때마다 다시 저장해야한다.
def init(group, g_pos, g_num, g_cnt, g_idx):
    visited = [[False] * N for _ in range(N)]  # BFS 탐색에 필요한 2차원 방문 배열

    for row in range(N):
        for col in range(N):
            # 방문하지 않은 곳이 있다면, 새로운 그룹의 시작이다.
            if not visited[row][col]:
                visited[row][col] = True
                cnt = 1  # 해당 그룹에 몇개의 칸이 있는지 세야한다.
                color = art[row][col]  # 해당 그룹의 색상

                g_pos.append((row, col))  # 해당 그룹의 첫 위치를 저장한다.
                g_num.append(color)  # 해당 그룹의 색상을 저장한다.
                g_idx[row][col] = group  # 2차원 배열에 그룹의 idx를 저장한다.

                # BFS로 현재 그룹을 찾는다.
                queue = deque([(row, col)])
                while queue:
                    r, c = queue.popleft()

                    for d in range(4):
                        n_r, n_c = r + dr[d], c + dc[d]
                        if in_range(n_r, n_c) and not visited[n_r][n_c] and art[n_r][n_c] == color:
                            visited[n_r][n_c] = True
                            cnt += 1
                            g_idx[n_r][n_c] = group
                            queue.append((n_r, n_c))

                # 하나의 그룹 찾기를 완성했다.
                g_cnt.append(cnt)
                group += 1

    return group

# 2개의 그룹이 맞닿은 변의 개수를 센다.
def connected_edge(a, b, g_pos, g_idx):
    edge = 0

    # 그룹 a를 기준으로 BFS를 돈다.
    visited = [[False] * N for _ in range(N)]
    visited[g_pos[a][0]][g_pos[a][1]] = True
    queue = deque([g_pos[a]])  # g_pos는 각 그룹의 가장 왼쪽, 상단의 위치를 저장해둔 배열이다.

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            n_r, n_c = r + dr[d], c + dc[d]
            if in_range(n_r, n_c) and not visited[n_r][n_c]:
                # 지금 보는 곳이 a 그룹이라면 queue에 추가한다.
                if g_idx[n_r][n_c] == a:
                    visited[n_r][n_c] = True
                    queue.append((n_r, n_c))
                # b 그룹이라면 맞닿은 변의 개수를 늘려준다.
                elif g_idx[n_r][n_c] == b:
                    edge += 1

    return edge


# 회전한다.
def rotate():
    # 회전한 뒤 옮길 2차원 배열
    rotated = [[0] * N for _ in range(N)]

    # 십자형 반시계 90도 회전.반시계 공식 : r, c => (N-1)-c, r
    # N//2 행을 N//2열에 밑에서부터 위로 저장
    for col in range(N):
        rotated[(N-1)-col][N//2] = art[N//2][col]
    # N//2 열을 N//2행에 왼쪽에서 오른쪽으로 저장
    for row in range(N):
        rotated[N//2][row] = art[row][N//2]

    # 십자형을 제외한 4개의 구역을 시계 90도 회전. 시계 공식 : r, c => c, (N-1)-r
    for s_r in [0, N//2+1]:
        for s_c in [0, N//2+1]:
            for r in range(N//2):
                for c in range(N//2):
                    rotated[s_r+c][s_c+N//2-1-r] = art[s_r+r][s_c+c]

    for i in range(N):
        art[i] = rotated[i][:]


# 각 그룹을 2개씩 뽑아서 점수를 계산한다.
def scoring(group, g_cnt, g_num, g_pos, g_idx):
    global answer
    group_pair = []
    used = [False] * group  # 조합을 위한 체크 변수
    # 그룹에서 2개를 조합으로 뽑아야한다.
    for a in range(group-1):
        used[a] = True
        for b in range(1, group):
            if not used[b]:
                group_pair.append((a, b))

    for a, b in group_pair:
        edges = connected_edge(a, b, g_pos, g_idx)

        if edges:
            # 점수 = (a 칸수 + b 칸수) * a 숫자 * b 숫자 * a와 b가 맞닿은 변의 수
            answer += (g_cnt[a] + g_cnt[b]) * g_num[a] * g_num[b] * edges


def solution():
    for _ in range(4):
        # 그룹과 관련된 변수. 회전하고 매번 새로 저장해야한다.
        g_num = []  # 각 그룹별 색상(숫자)
        g_cnt = []  # 각 그룹별 칸의 수
        g_idx = [[-1] * N for _ in range(N)]  # 각 위치별 그룹 인덱스
        g_pos = []  # 각 그룹별 시작 위치 [(x, y), (x, y)..] => 이후 그룹간의 맞닿은 변을 BFS로 찾을 때 속도를 줄이기 위함.

        group = init(0, g_pos, g_num, g_cnt, g_idx) # 그룹의 인덱스

        scoring(group, g_cnt, g_num, g_pos, g_idx)
        rotate()
    print(answer)


solution()
