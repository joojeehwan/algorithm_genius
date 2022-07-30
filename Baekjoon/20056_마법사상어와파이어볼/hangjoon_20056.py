import sys


def moving(fireballs, size):
    # 1. 이동
    new_fireballs = []
    new_field = [[[] for _ in range(size)] for _ in range(size)]  # 1~2번 단계가 완전히 끝난 후의 좌표 정보
    for fb_r, fb_c, fb_m, fb_s, fb_d in fireballs:
        new_r = fb_r + direction[fb_d][0] * fb_s
        new_c = fb_c + direction[fb_d][1] * fb_s
        # 맵 끝과 끝은 연결되어 있음
        if new_r < 0 or new_r >= size:
            new_r = (new_r + size) % size
        if new_c < 0 or new_c >= size:
            new_c = (new_c + size) % size
        new_field[new_r][new_c].append((fb_m, fb_s, fb_d))

    # 2. 2개 이상의 파이어볼이 있는 경우
    for r in range(size):
        for c in range(size):
            if len(new_field[r][c]) >= 2:  # 합쳐지는 경우
                new_m = 0
                new_s = 0
                even_cnt = 0
                odd_cnt = 0
                # 질량, 속력, 방향 계산
                for now_m, now_s, now_d in new_field[r][c]:
                    new_m += now_m
                    new_s += now_s
                    if now_d % 2:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                new_m //= 5  # 새로운 질량
                if not new_m:  # 질량이 0이면 소멸
                    new_field[r][c] = []
                    continue
                new_s //= len(new_field[r][c])  # 새로운 속력
                if even_cnt == len(new_field[r][c]) or odd_cnt == len(new_field[r][c]): # 새로운 방향
                    new_d = [0, 2, 4, 6]
                else:
                    new_d = [1, 3, 5, 7]

                # 4개로 나눠진 파이어볼 기록
                new_field[r][c] = []
                for new_dd in new_d:
                    new_field[r][c].append((new_m, new_s, new_dd))
                    new_fireballs.append((r, c, new_m, new_s, new_dd))

            elif len(new_field[r][c]) == 1:  # 파이어볼이 하나 있는 경우
                # 하나의 파이어볼 기록
                new_fireball = (r, c, new_field[r][c][0][0], new_field[r][c][0][1], new_field[r][c][0][2])
                new_fireballs.append(new_fireball)

    return new_field, new_fireballs


size, f_num, moves = map(int, sys.stdin.readline().split())  # 격자 크기, 파이어볼 수, 이동 횟수
fireballs = [[] for _ in range(f_num)]  # 파이어볼 정보
field = [[[] for _ in range(size)] for _ in range(size)]  # 격자 정보
for i in range(f_num):
    r, c, m, s, d = map(int, sys.stdin.readline().split())  # 좌표(열, 행), 질량, 속력, 방향
    r, c = r - 1, c - 1  # 인덱싱
    field[r][c] = [m, s, d]
    fireballs[i] = (r, c, m, s, d)
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 방향 정보에 따른 이동 방향
ans = 0

for _ in range(moves):
    field, fireballs = moving(fireballs, size)  # 좌표정보와 파이어볼 정보 갱신
for r in range(size):
    for c in range(size):
        if field[r][c]:  # (r, c)에서 파이어볼 찾음
            for fb in field[r][c]:
                ans += fb[0]
print(ans)