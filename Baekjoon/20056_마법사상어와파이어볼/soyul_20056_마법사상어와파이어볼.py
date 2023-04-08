import sys

N, M, K = map(int, sys.stdin.readline().split())

# 방향
di = [-1, -1, 0, 1, 1, 1, 0, -1] # 위 부터 시계방향으로 45도씩
dj = [0, 1, 1, 1, 0, -1, -1, -1]

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs.append((r-1, c-1, m, s, d))

# K 번 이동
for _ in range(K):
    MAP = [[[] for _ in range(N)] for _ in range(N)]

    # 존재하는 모든 파이어볼 이동
    while fireballs:
        now_i, now_j, m, s, d = fireballs.pop(0)

        next_i = (now_i + di[d] * s) % N
        next_j = (now_j + dj[d] * s) % N
        MAP[next_i][next_j].append((m, s, d))

    # 파이어볼이 2개 이상인지 확인
    for i in range(N):
        for j in range(N):

            if len(MAP[i][j]) >= 2:             # 파이어볼이 2개 이상이면 조건대로 파이어볼 새로 설정
                weight = 0
                speed = 0
                odd = 0
                even = 0
                for k in range(len(MAP[i][j])):
                    weight += MAP[i][j][k][0]
                    speed += MAP[i][j][k][1]
                    if MAP[i][j][k][2] % 2:
                        even += 1
                    else:
                        odd += 1
                if odd == len(MAP[i][j]) or even == len(MAP[i][j]):
                    dir = (0, 2, 4, 6)
                else:
                    dir = (1, 3, 5, 7)
                weight //= 5
                speed //= len(MAP[i][j])

                # 질량이 0이면 소멸 아니면 이동
                if weight:
                    MAP[i][j] = []
                    for d in dir:
                        fireballs.append((i, j, weight, speed, d))
                        MAP[i][j].append((weight, speed, d))

            elif len(MAP[i][j]) == 1:
                fireballs.append((i, j) + MAP[i][j][0])

ans = 0
for ball in fireballs:
    ans += ball[2]

print(ans)

"""
4 4 2
1 2 13 4 3
1 4 12 3 7
4 1 2 5 7
4 2 6 3 0

25
"""