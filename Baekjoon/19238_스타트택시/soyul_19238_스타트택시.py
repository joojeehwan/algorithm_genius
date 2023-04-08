import sys
from collections import deque

N, M, gas = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi_i, taxi_j = map(int, sys.stdin.readline().split())
passenger = []
for _ in range(M):
    passenger.append(list(map(int, sys.stdin.readline().split())))

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 어떤 승객을 태울지 찾는 함수
def find(start_i, start_j):

    q = deque()
    q.append((start_i, start_j))
    visited = [[0] * N for _ in range(N)]
    visited[start_i][start_j] = 1

    while q:
        now_i, now_j = q.popleft()

        for k in range(4):
            next_i, next_j = now_i + di[k], now_j + dj[k]

            if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N:
                continue
            if visited[next_i][next_j] or MAP[next_i][next_j]:
                continue

            visited[next_i][next_j] = visited[now_i][now_j] + 1
            q.append((next_i, next_j))


    min_dis = visited[passenger[0][0]-1][passenger[0][1]-1]
    min_idx = 0
    if min_dis == 0:
        return -1, -1
    for i in range(1, len(passenger)):
        if visited[passenger[i][0]-1][passenger[i][1]-1] < min_dis:
            min_dis = visited[passenger[i][0]-1][passenger[i][1]-1]
            min_idx = i
        elif visited[passenger[i][0]-1][passenger[i][1]-1] == min_dis:
            if passenger[i][0] < passenger[min_idx][0]:
                min_dis = visited[passenger[i][0] - 1][passenger[i][1] - 1]
                min_idx = i
            elif passenger[i][0] == passenger[min_idx][0]:
                if passenger[i][1] < passenger[min_idx][1]:
                    min_dis = visited[passenger[i][0] - 1][passenger[i][1] - 1]
                    min_idx = i

    return min_dis, min_idx

# 승객을 목적지까지 태워보낼 때 거리를 찾는 함수
def distance(start_i, start_j, goal_i, goal_j):

    q = deque()
    q.append((start_i, start_j))
    visited = [[0] * N for _ in range(N)]
    visited[start_i][start_j] = 1

    while q:
        now_i, now_j = q.popleft()

        if visited[goal_i][goal_j]:
            return visited[goal_i][goal_j]

        for k in range(4):
            next_i, next_j = now_i + di[k], now_j + dj[k]

            if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N:
                continue
            if visited[next_i][next_j] or MAP[next_i][next_j]:
                continue

            visited[next_i][next_j] = visited[now_i][now_j] + 1
            q.append((next_i, next_j))

    # 목적지까지 못 갔다면
    return -1

flag = 1
for _ in range(M):
    min_dis, min_idx = find(taxi_i-1, taxi_j-1)
    if min_dis == -1:                           # 만약 승객을 태우러 못 갔다면
        flag = 0
        break
    to_gas = distance(passenger[min_idx][0]-1, passenger[min_idx][1]-1, passenger[min_idx][2]-1, passenger[min_idx][3]-1) - 1
    if to_gas == -2:                            # 승객을 목적지까지 데려다줄 수 없다면
        flag = 0
        break
    if min_dis - 1 + to_gas <= gas:             # 승객을 데리고 목적지까지 가는 데 연료가 충분하다면
        gas -= min_dis - 1
        gas += to_gas
        taxi_i, taxi_j = passenger[min_idx][2], passenger[min_idx][3]
        passenger.pop(min_idx)
    else:
        flag = 0
        break

if flag:
    print(gas)
else:
    print(-1)
