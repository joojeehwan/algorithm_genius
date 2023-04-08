import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 치즈가 다 녹는데 걸리는 시간, 한시간 전 치즈 조각 칸 개수
hour = 0
last_cnt = 0

# 공기 체크
while 1:

    q = deque()
    q.append((0, 0))            # 0, 0 은 무조건 공기
    air = [[0] * M for _ in range(N)]       # 공기임을 확인하는 배열
    air[0][0] = 1

    while q:
        now_i, now_j = q.popleft()

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어나거나 검사한곳이면 pass
            if next_i < 0 or next_j < 0 or next_i >= N or next_j >= M:
                continue
            if air[next_i][next_j]:
                continue

            # 공기랑 맞닿아있는 치즈면 표시해줌
            if MAP[next_i][next_j]:
                MAP[next_i][next_j] += 1
            else:
                q.append((next_i, next_j))
                air[next_i][next_j] = 1

    hour += 1
    cnt = 0                     # 남은 치즈 개수
    melt_cheese = 0             # 녹은 치즈 개수
    # 치즈 녹이기
    for i in range(1, N-1):
        for j in range(1, M-1):
            if MAP[i][j] >= 2:      # 공기와 접촉한 칸은 녹여줌
                MAP[i][j] = 0
                melt_cheese += 1
            elif MAP[i][j]:             # 마지막 한시간 전에 남아있는 치즈 개수 세줌
                cnt += 1

    if cnt:
        last_cnt = cnt

    if not cnt:
        break

print(hour)
if hour == 1:                       # 만약에 1시간만에 치즈가 다 녹았다면 녹은 치즈의 개수를 그대로 프린트
    print(melt_cheese)
else:
    print(last_cnt)