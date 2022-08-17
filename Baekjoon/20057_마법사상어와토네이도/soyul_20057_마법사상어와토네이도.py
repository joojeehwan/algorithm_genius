import sys
import math

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

now_i, now_j = N // 2, N // 2

di = [0, 1, 0, -1]             # 좌 하 우 상
dj = [-1, 0, 1, 0]

# 토네이도 모래바람 방향 좌 하 우 상
tornado_di = [[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],   # 두칸 위, 한칸위 왼쪽, 한칸위, 한칸위오른, 두칸왼쪽, 한칸아래왼쪽, 한칸아래, 한칸아래오른쪽, 두칸아래, 왼쪽(알파)
              [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],   # 두칸왼쪽, 한칸왼쪽아래, 한칸왼, 한칸왼위, 두칸아래, 한칸오른아래, 한칸오른, 한칸오른위, 두칸오른, 한칸아래(알파)
              [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],   # 두칸 위, 한칸위 오른, 한칸위, 한칸위왼, 두칸오른, 한칸아래오른, 한칸아래, 한칸아래왼, 두칸아래, 오른(알파)
              [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]]   # 두칸왼, 한칸왼위, 한칸왼, 한칸왼아래, 두칸위, 한칸오른위, 한칸오른, 한칸오른아래, 두칸오른, 한칸위(알파)
tornado_dj = [[0, -1, 0, 1, -2, -1, 0, 1, 0, -1],
              [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
              [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
              [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0]]
tornado_per = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]

out_sand = 0    # 격자 바깥으로 나간 모래들

# 토네이도를 이동시키는 함수
def tornado(now_i, now_j, dir):
    global out_sand

    sand = 0        # 총 날아간 모래들

    # 토네이도로 날아간 모래들
    for k in range(9):
        sand_i = now_i + tornado_di[dir][k]
        sand_j = now_j + tornado_dj[dir][k]

        if sand_i < 0 or sand_i >= N or sand_j < 0 or sand_j >= N:
            out_sand += math.trunc(MAP[now_i][now_j] * tornado_per[k])
            sand += math.trunc(MAP[now_i][now_j] * tornado_per[k])
            continue

        MAP[sand_i][sand_j] += math.trunc(MAP[now_i][now_j] * tornado_per[k])
        sand += math.trunc(MAP[now_i][now_j] * tornado_per[k])

    # 알파 계산
    a_i = now_i + tornado_di[dir][-1]
    a_j = now_j + tornado_dj[dir][-1]
    if a_i < 0 or a_j < 0 or a_i >= N or a_j >= N:
        out_sand += MAP[now_i][now_j] - sand
    else:
        MAP[a_i][a_j] += MAP[now_i][now_j] - sand
    MAP[now_i][now_j] = 0

    return

k = 1
dir = 0                         # 토네이도 이동 방향
flag = 1
while flag:
    # 중심에서부터 달팽이 모양으로 돌아가는 좌표 구현
    for _ in range(2):
        if flag == 0:
            break
        for _ in range(k):
            now_i = now_i + di[dir % 4]
            now_j = now_j + dj[dir % 4]

            if now_i == 0 and now_j == -1:
                flag = 0
                break
            tornado(now_i, now_j, dir % 4)              # 토네이도가 향할 곳이 now_i, now_j, 방향도 함께 넘겨줌

        dir += 1
    k += 1

print(out_sand)