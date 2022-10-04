import sys

N, M = map(int, sys.stdin.readline().split())
bucket = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
moves = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(M))
clouds = [[0] * N for _ in range(N)]
# 구름 4개 원래 생성
clouds[N - 1][0], clouds[N - 1][1], clouds[N - 2][0], clouds[N - 2][1] = 1, 1, 1, 1

delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for direction, speed in moves:
    # 구름 이동
    add_water = []

    for r in range(N):
        for c in range(N):
            if clouds[r][c]:
                # 구름이 d 방향으로 s칸 이동한다.
                # 1번과 N번 행, 열은 이어져 있다.
                move_r = (r + delta[direction-1][0] * speed) % N
                move_c = (c + delta[direction-1][1] * speed) % N
                # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 증가한다.
                bucket[move_r][move_c] += 1
                # 물이 증가한 칸에서 물복사버그 마법을 시전한다.
                add_water.append((move_r, move_c))
                clouds[r][c] = 0

    # 물복사버그 마법 시전
    for r, c in add_water:
        dia_cnt = 0
        for d in range(4):
            # delta 배열에서 홀수가 대각선
            dia_r = r + delta[1 + 2*d][0]
            dia_c = c + delta[1 + 2*d][1]

            # 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아님
            if 0 <= dia_r < N and 0 <= dia_c < N and bucket[dia_r][dia_c]:
                # 물에 있는 바구니의 수 만큼 물의 양이 증가
                dia_cnt += 1

        # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수 만큼 (r, c)의 물 증가
        bucket[r][c] += dia_cnt

    # 구름 생성
    for r in range(N):
        for c in range(N):
            if bucket[r][c] >= 2:
                # 물의 양이 2 이상이라면 구름이 생기는데, 구름이 이동하고나서 사라진 구름이 아니어야함.
                if (r, c) not in add_water:
                    clouds[r][c] = 1
                    bucket[r][c] -= 2


answer = 0
for r in range(N):
    answer += sum(bucket[r])

print(answer)