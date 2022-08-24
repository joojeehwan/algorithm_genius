import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(2**N)]
level = list(map(int, sys.stdin.readline().split()))

# 회전하는 함수
def rotate(n):
    rotate_MAP = [[0] * (2**N) for _ in range(2**N)]
    for x in range(0, 2**N, 2**n):
        for y in range(0, 2**N, 2**n):

            for i in range(2**n):
                for j in range(2**n):
                    rotate_MAP[x + j][y + 2 ** n - i - 1] = MAP[x + i][y + j]

    return rotate_MAP

for l in level:
    if l > 0:
        MAP = rotate(l)                 # 맵을 계속 회전시켜줌

    # 얼음을 녹여줌
    cnt_MAP = [[0] * (2**N) for _ in range(2**N)]
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    for i in range(2**N):
        for j in range(2**N):

            for k in range(4):
                cnt_i = i + di[k]
                cnt_j = j + dj[k]

                if cnt_i < 0 or cnt_i >= 2**N or cnt_j < 0 or cnt_j >= 2**N:
                    continue
                if not MAP[cnt_i][cnt_j]:
                    continue

                cnt_MAP[i][j] += 1

    for i in range(2 ** N):
        for j in range(2 ** N):
            if not MAP[i][j]:
                continue
            if cnt_MAP[i][j] < 3:
                MAP[i][j] -= 1


# 파이어스톰을 다 실행한 후 얼음 계산
ice_sum = 0
max_ice = 0

visited =[[0] * (2**N) for _ in range(2**N)]
for i in range(2**N):
    ice_sum += sum(MAP[i])
    for j in range(2**N):
        if MAP[i][j] and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            ice_cnt = 1

            while q:
                now_i, now_j = q.popleft()

                for k in range(4):
                    next_i = now_i + di[k]
                    next_j = now_j + dj[k]

                    if next_i < 0 or next_i >= 2**N or next_j < 0 or next_j >= 2**N:
                        continue
                    if visited[next_i][next_j]:
                        continue
                    if not MAP[next_i][next_j]:
                        continue

                    q.append((next_i, next_j))
                    visited[next_i][next_j] = 1
                    ice_cnt += 1

            max_ice = max(max_ice, ice_cnt)

print(ice_sum)
print(max_ice)

