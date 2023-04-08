import sys
from collections import deque
from pprint import pprint

# 그룹을 만드는 함수
def make_group(now_i, now_j):

    group = [MAP[now_i][now_j], (now_i, now_j)]

    q = deque()
    q.append((now_i, now_j))
    visited[now_i][now_j] = check

    while q:
        now_i, now_j = q.popleft()

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어나거나 다른거면 pass 다른 숫자면 pass 지나갔던 곳이면 pass
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            if MAP[next_i][next_j] != MAP[now_i][now_j]:
                continue
            if visited[next_i][next_j]:
                continue

            visited[next_i][next_j] = check
            q.append((next_i, next_j))
            group.append((next_i, next_j))

    group_list.append(group)

# 조화로움을 계산하는 함수
def harmony(x, y):

    cnt = 0

    for now_i, now_j in group_list[x][1:]:
        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 맞닿아있는 변 계산
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            if visited[next_i][next_j] != -(y+1):
                continue

            cnt += 1

    return (len(group_list[x]) - 1 + len(group_list[y]) - 1) * group_list[x][0] * group_list[y][0] * cnt

# 회전하는 함수
def rotate():

    rotate_MAP = [[0] * n for _ in range(n)]

    m = n // 2

    # 1블럭
    for i in range(m):
        for j in range(m):
            rotate_MAP[i][j] = MAP[m-j-1][i]

    # 2블럭
    for i in range(m):
        for j in range(m+1, n):
            rotate_MAP[i][j] = MAP[n-j-1][m+i+1]

    # 3블럭
    for i in range(m+1, n):
        for j in range(m):
            rotate_MAP[i][j] = MAP[n-j-1][i-m-1]

    # 4블럭
    for i in range(m+1, n):
        for j in range(m+1,n):
            rotate_MAP[i][j] = MAP[n-(j-m)][i]

    # 가운데 세로
    for i in range(n):
        rotate_MAP[i][m] = MAP[m][n-i-1]

    # 가운데 가로
    for i in range(n):
        rotate_MAP[m][i] = MAP[i][m]

    return rotate_MAP

n = int(input())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

score = 0

for _ in range(4):

    group_list = []
    visited = [[0] * n for _ in range(n)]
    check = -1

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                make_group(i, j)
                check -= 1

    l = len(group_list)

    # 조합 만들어서 조화로움 계산
    for i in range(l):
        for j in range(i+1, l):
            score += harmony(i, j)

    MAP = rotate()
    pprint(MAP)
    print(score)

print(score)

"""[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 2, 1]]
250
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 2, 1],
 [1, 1, 1, 1, 1]]
450
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 2],
 [1, 1, 1, 1, 1]]
600
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 2]]
600
"""