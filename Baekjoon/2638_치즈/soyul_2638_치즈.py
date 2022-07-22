import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

cnt = 0
while 1:
    q = deque()
    q.append((0, 0))
    air = [[0] * M for _ in range(N)]  # 공기인지 체크하는 배열
    air[0][0] = 1

    # bfs를 이용하여 바깥쪽 공기인 부분을 모두 표시 및 그 공기와 맞닿아있는 치즈 표시
    while q:
        now_i, now_j = q.popleft()
        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            if next_i < 0 or next_i >= N or next_j < 0 or next_j >= M:      # 범위를 벗어났거나 이미 체크한 곳이면 패스
                continue
            if air[next_i][next_j]:
                continue

            if MAP[next_i][next_j]:                 # 치즈면 공기와 맞닿아있다는 표시로 +1을 해줌
                MAP[next_i][next_j] += 1
            else:
                air[next_i][next_j] = 1
                q.append((next_i, next_j))

    flag = 1                        # 더 검사할 치즈가 남아있는지 확인할 flag
    for i in range(N):
        for j in range(M):
            if MAP[i][j] >= 3:              # 공기와 맞닿은 곳이 2개 이상이면 치즈 없어짐
                MAP[i][j] = 0
            elif MAP[i][j] > 0:             # 2개 미만이면 다시 원래대로 1로 표시
                flag = 0                    # 치즈가 남아있다는 뜻
                MAP[i][j] = 1

    cnt += 1

    if flag:
        break

print(cnt)