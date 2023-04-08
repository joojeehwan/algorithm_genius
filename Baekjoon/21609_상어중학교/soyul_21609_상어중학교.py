import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

"""
크기가 가장 큰 블록 그룹을 찾는다.
검은색 블록(-1)은 포함되면 안 되고, 무지개 블록(0)은 얼마나 들어있든 상관없다. 
그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹
그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것
그 것도 여러개이면 열이 가장 큰 것을 찾는다.
(기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록)
"""

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 가장 큰 블록 찾기
def group():

    visited = [[0] * N for _ in range(N)]
    group_block = []
    rainbow_cnt = 0
    standard = (0, 0)
    check = 0

    for i in range(N):
        for j in range(N):
            if MAP[i][j] > 0:               # bfs를 이용하여 시작
                standard_i, standard_j = i, j                           # 기준블록
                color = MAP[i][j]
                rainbow = 0
                check += 1
                group = []

                q = deque()
                q.append((i, j))
                group.append((i, j))
                visited[i][j] = check

                while q:
                    now_i, now_j = q.popleft()

                    for k in range(4):
                        next_i = now_i + di[k]
                        next_j = now_j + dj[k]

                        # 범위를 벗어나거나 검은색 블록이거나 지나간 곳이거나 다른 색이면 안됨
                        if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N:
                            continue
                        if MAP[next_i][next_j] <= -1:
                            continue
                        if visited[next_i][next_j] == check:
                            continue
                        if MAP[next_i][next_j] > 0 and MAP[next_i][next_j] != color:
                            continue

                        if MAP[next_i][next_j] == 0:        # 무지개블록이면 카운트 추가
                            rainbow += 1
                        if MAP[next_i][next_j]:             # 색깔블록이면 기준블록 갱신
                            if next_i < standard_i:
                                standard_i, standard_j = next_i, next_j
                            elif next_i == standard_i:
                                if next_j < standard_j:
                                    standard_i, standard_j = next_i, next_j


                        q.append((next_i, next_j))
                        visited[next_i][next_j] = check
                        group.append((next_i, next_j))

                if len(group) < 2:
                    continue

                # 블록은 무조건 큰 것으로 크기가 같다면 비교
                if len(group) > len(group_block):
                    group_block = group
                    rainbow_cnt = rainbow
                    standard = (standard_i, standard_j)
                elif len(group) == len(group_block):            # 크기가 같으면 무지개블록 개수 체크
                   if rainbow > rainbow_cnt:
                        group_block = group
                        rainbow_cnt = rainbow
                        standard = (standard_i, standard_j)
                   elif rainbow == rainbow_cnt:
                       if standard_i > standard[0]:
                            group_block = group
                            rainbow_cnt = rainbow
                            standard = (standard_i, standard_j)
                       elif standard_i == standard[0]:
                           if standard_j > standard[1]:
                               group_block = group
                               rainbow_cnt = rainbow
                               standard = (standard_i, standard_j)


    return group_block

# 그룹의 블록들을 파괴하는 함수
def remove_block(group_block):
    for i, j in group_block:
        MAP[i][j] = -5

# 중력작용으로 블록을 다 떨어트리는 함수
def gravity():

    for i in range(N-2, -1, -1):
        for j in range(N):
            if MAP[i][j] >= 0:
                k = i
                while k < N-1:                 # 바닥을 만날때까지
                    k += 1
                    if k == N-1 and MAP[k][j] == -5:
                        MAP[k][j] = MAP[i][j]
                        MAP[i][j] = -5
                    if MAP[k][j] >= -1:               # 무언가 만나면
                        if k == i + 1:
                            break
                        MAP[k - 1][j] = MAP[i][j]
                        MAP[i][j] = -5
                        break

# 반시계방향으로 회전하는 함수
# 맨 윗줄부터 채워나가는 방식
def rotate():

    new_MAP = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_MAP[i][j] = MAP[j][N-i-1]

    return new_MAP



score = 0
while 1:
    group_block = group()
    if not len(group_block):
        break

    # 블록 파괴 및 점수
    score += len(group_block) ** 2
    remove_block(group_block)

    # 중력작용
    gravity()

    # 반시계 후 중력
    MAP = rotate()
    gravity()

print(score)