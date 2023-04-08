import sys
from collections import deque

# 1년이 지날때마다 얼음이 녹는 걸 구현하는 함수
def melt():

    cnt_sea = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if MAP[i][j] != 0:
                for k in range(4):
                    check_i = i + di[k]
                    check_j = j + dj[k]
                    if check_i < 0 or check_j < 0 or check_i >= n or check_j >= m:
                        continue
                    if MAP[check_i][check_j] == 0:              # 주위가 바다면 cnt += 1
                        cnt_sea[i][j] += 1

    # 바다와 인접한 만큼 빼주고 -면 0으로 만들어줌
    for i in range(n):
        for j in range(m):
            MAP[i][j] -= cnt_sea[i][j]
            if MAP[i][j] < 0:
                MAP[i][j] = 0

# 빙산이 덩어리로 분리되어있는지 확인하는 함수
def check():

    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if MAP[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    now_i, now_j = q.popleft()
                    for k in range(4):
                        next_i = now_i + di[k]
                        next_j = now_j + dj[k]

                        if next_i < 0 or next_j < 0 or next_i >= n or next_j >= m:
                            continue
                        if MAP[next_i][next_j] == 0:
                            continue
                        if visited[next_i][next_j]:
                            continue

                        visited[next_i][next_j] = 1
                        q.append((next_i, next_j))

    return cnt

n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

year = 0
ans = check()
while ans == 1:
    melt()
    ans = check()
    year += 1

if ans == 0:
    print(0)
else:
    print(year)