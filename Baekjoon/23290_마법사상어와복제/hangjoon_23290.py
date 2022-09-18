import sys


def move_shark(sr, sc, distance=0, direction='', cnt=0, move=[]):
    # 상어 위치(r, c), 이동 거리, 움직인 방향 기록, 먹은 물고기 수
    global f_cnt, shark_direction, new_shark, eaten
    # 종료조건
    if distance == 3:
        if f_cnt < cnt or (f_cnt == cnt and shark_direction > direction):
            f_cnt = cnt
            new_shark = (sr, sc)
            shark_direction = direction
            eaten = move[:]
        return
    # 진행 중
    for d in range(4):
        # 이동할 위치 결정
        new_r, new_c = sr + shark_D[d][0], sc + shark_D[d][1]
        if new_r < 0 or new_r >= 4 or new_c < 0 or new_c >= 4:  # 맵 밖임
            continue
        # 물고기 먹기
        if new_field[new_r][new_c] and (new_r, new_c) not in move:
            move.append((new_r, new_c))
            move_shark(new_r, new_c, distance + 1, direction + str(d), cnt + len(new_field[new_r][new_c]))
            # 복원
            move.pop()
        else:
            move_shark(new_r, new_c, distance + 1, direction + str(d), cnt)


fishes, trainings = map(int, sys.stdin.readline().split())  # 물고기 수, 연습 수
field = [[[] for _ in range(4)] for _ in range(4)]  # 격자 상태
for fish in range(fishes):
    r, c, d = map(int, input().split())  # 물고기의 위치, 방향
    field[r - 1][c - 1].append(d - 1)
DIRECTION = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  # d에 따른 물고기 방향
shark_D = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 상어의 이동 방향
shark_r, shark_c = map(int, input().split())  # 상어 위치
shark = (shark_r - 1, shark_c - 1)
smell = [[0] * 4 for _ in range(4)]  # 물고기 냄새 상태
# print('----- 초기 격자 상태 -----')
# for f in field:
#     print(f)
# print()

for _ in range(trainings):
    # print(f'<<<<< {_} 번째 연습 >>>>>')
    # print()
    new_field = [[[] for _ in range(4)] for _ in range(4)]
    # 1. 물고기 이동
    for r in range(4):
        for c in range(4):
            if field[r][c]:  # 물고기가 있다면
                for fd in field[r][c]:
                    # 어디로 이동할지 결정
                    for d_cnt in range(8):
                        new_fd = (fd - d_cnt) % 8
                        new_fr, new_fc = r + DIRECTION[new_fd][0], c + DIRECTION[new_fd][1]
                        if new_fr < 0 or new_fr >= 4 or new_fc < 0 or new_fc >= 4:  # 맵 밖임
                            continue
                        if smell[new_fr][new_fc]:  # 물고기 냄새 있음
                            continue
                        if shark == (new_fr, new_fc):  # 상어 있음
                            continue
                        new_field[new_fr][new_fc].append(new_fd)  # 이동 가능
                        break
                    else:  # 이동 불가능
                        new_field[r][c].append(fd)
    # print(f'----- 물고기 이동 후 -----')
    # for f in field:
    #     print(f)
    # print()

    # 2. 상어 이동 (DFS)
    f_cnt = 0  # 먹은 물고기 수
    new_shark = (-1, -1)  # 이동 후 상어 위치
    shark_direction = '999'  # 상어의 방향 사전 순
    eaten = []  # 상어의 식사 기록
    move_shark(shark[0] , shark[1])
    shark = new_shark
    for er, ec in eaten:
        new_field[er][ec] = []
        smell[er][ec] = 3
    # print('----- 상어 이동 후 -----')
    # print(new_shark, shark_direction, eaten)
    # for f in new_field:
    #     print(f)
    # print()

    # 3. 냄새 희미해지기
    for r in range(4):
        for c in range(4):
            if smell[r][c]:
                smell[r][c] -= 1
    # print('----- 냄새 희미해진 후 -----')
    # for s in smell:
    #     print(s)
    # print()

    # 4. 복제 마법
    for r in range(4):
        for c in range(4):
            field[r][c] += new_field[r][c]
    # print('----- 복제 마법 후 -----')
    # for f in field:
    #     print(f)
    # print()


# 물고기 수 세기
ans = 0
for r in range(4):
    for c in range(4):
        if field[r][c]:
            ans += len(field[r][c])
print(ans)