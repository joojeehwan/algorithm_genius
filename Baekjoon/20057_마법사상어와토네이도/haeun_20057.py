import sys

N = int(sys.stdin.readline())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

percent = [0.01, 0.01, 0.02, 0.02, 0.05, 0.07, 0.07, 0.1, 0.1, 0]
# 서 남 동 북
r = [0, 1, 0, -1]
c = [-1, 0, 1, 0]

# 서쪽 기준
dr = [-1, 1, -2, 2, 0, -1, 1, -1, 1, 0]
dc = [1, 1, 0, 0, -2, 0, 0, -1, -1, -1]

# N이 항상 홀수인 이유
row, col = N // 2, N // 2

# 현재 방향과 거리
direction, distance = 0, 1

# 격자 밖으로 날라간 모래
answer = 0

while True:
    if row < 0 or col < 0:
        break
    for _ in range(2):
        for _ in range(distance):
            # y 위치 찾기
            row, col = row + r[direction], col + c[direction]
            if row < 0 or col < 0:
                continue
            sand = grid[row][col]
            minus = 0

            for j in range(10):
                # 서 남 동 북에 따라 이동하는 곳 바꾸기
                if direction == 0:
                    move_row, move_col = row + dr[j], col + dc[j]  # 서쪽
                elif direction == 1:
                    move_row, move_col = row - dc[j], col + dr[j]  # 남쪽
                elif direction == 2:
                    move_row, move_col = row - dr[j], col - dc[j]  # 동쪽
                else:
                    move_row, move_col = row + dc[j], col - dr[j]  # 북쪽

                # a 값 구하기
                if j == 9:
                    # print(f"a를 구합니다. 모래 : {sand}, 덜은 양 : {minus}")
                    move_sand = sand - minus
                else:
                    move_sand = int(sand * percent[j])
                    minus += move_sand

                # 모래가 밖으로 나가는지 아닌지
                if not (0 <= move_row < N and 0 <= move_col < N):
                    answer += move_sand
                else:
                    grid[move_row][move_col] += move_sand
            # 10곳 다 돌았으면 이제 빼기
            grid[row][col] = 0
            # print(f"모래가 이동했습니다. 지금 방향 : { direction }, 지금 거리 : {distance}")
            # print(f"현재 위치 : {row}, {col}")
            # print(f"현재 격자 밖으로 나간 모래 : {answer}")
            # for line in grid:
            #     print(*line)
        direction = (direction + 1) % 4
    # 달팽이 껍질 모양으로 이동
    distance += 1

print(answer)