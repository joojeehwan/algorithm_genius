import sys

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 새로운 구름을 만들어줌
def make_cloud():
    new_cloud = []

    for i in range(N):
        for j in range(N):
            if visited[i][j]:           # 이전에 구름이었으면 안됨
                continue
            if MAP[i][j] >= 2:          # 구름이 만들어지면서 2씩 줄어듬
                MAP[i][j] -= 2
                new_cloud.append([i, j])

    return new_cloud

# 구름이동방향 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())

    visited = [[0] * N for _ in range(N)]

    # 처음 4구역에 있던 구름을 이동시키고 비를 내림
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + di[d-1] * s) % N
        cloud[i][1] = (cloud[i][1] + dj[d-1] * s) % N
        MAP[cloud[i][0]][cloud[i][1]] += 1
        visited[cloud[i][0]][cloud[i][1]] = 1

    # 대각선 방향에 물이 있는지 확인하고 그만큼 더해줌
    for i, j in cloud:

        for k in range(1, 9, 2):
            check_i = i + di[k]
            check_j = j + dj[k]

            if check_i < 0 or check_i >= N or check_j < 0 or check_j >= N:
                continue
            if MAP[check_i][check_j]:
                MAP[i][j] += 1

    cloud = make_cloud()        # 새로운 구름 만들기

answer = 0
for i in range(N):
    answer += sum(MAP[i])

print(answer)
