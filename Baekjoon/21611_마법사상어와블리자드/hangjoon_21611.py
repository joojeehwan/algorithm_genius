from collections import deque
import sys


def blizzard(r, c, d, s, field):
    dr, dc = MD[d]
    while s:
        r, c = r + dr, c + dc
        field[r][c] = 0  # 구슬 파괴
        s -= 1
    return field, True


def find_blanks(r, c, field):
    d = 0  # 순회 방향 (BD에 따라 순회)
    s = 1  # 이동 거리 (순회 방향이 홀수번째가 될 때마다 +1)
    flat_field = []
    # 순회하면서 1차원으로 변환, 빈 칸은 제외
    while r >= 0 and c >= 0:
        now_s = s
        while now_s:  # 거리만큼
            now_s -= 1
            now_ball = field[r][c]
            # 복사
            if now_ball:  # 구슬이 있는 경우만
                flat_field.append(now_ball)
            # 다음 좌표
            r += BD[d][0]
            c += BD[d][1]
        # 방향, 거리 업데이트
        d = (d + 1) % 4
        if d % 2:  # 홀수번 째 = 거리 추가
            s += 1
    return flat_field


def explode(bomb, ff):
    now = 0  # 현재 위치
    exist = False  # 빈칸 여부
    while now < len(ff):
        now_ball = ff[now]
        cnt = 1  # 연속 수
        for i in range(1, len(ff) - now + 1):
            if now + i >= len(ff) or now_ball != ff[now + i]:  # 조건 만족 x
                now += i
                break
            else:  # 같은 구슬이 연속됨
                cnt += 1
                continue
        if cnt >= 4:  # 4개가 연속 됨
            ff = ff[:now-cnt] + ff[now:]
            bomb[now_ball] += cnt
            exist = True  # 폭발이 있었으면 빈칸이 생김
            now -= cnt
    return ff, exist, bomb


def change_balls(ff):
    now = 0  # 현재 위치
    new_ff = []
    while now < len(ff):
        cnt = 0  # 연속 수
        # 연속된 수 탐색
        for next in range(now, len(ff)):
            if ff[now] == ff[next]:
                cnt += 1
            else:
                next -= 1
                break
        # 삽입
        new_ff.append(cnt)
        new_ff.append(ff[now])
        # 다음 위치
        now = next + 1
    return new_ff


def insert_balls(r, c, size, ff):
    d = 0  # 순회 방향 (BD에 따라 순회)
    s = 1  # 이동 거리 (순회 방향이 홀수번째가 될 때마다 +1)
    # 순회하면서 다시 자리에 넣기
    new_field = [[0] * size for _ in range(size)]
    while ff and r >= 0 and c >= 0:
        now_s = s
        while ff and now_s and r >= 0 and c >= 0:  # 거리만큼
            now_s -= 1
            # 새 구슬 넣기
            now_ball = ff.pop(0)
            new_field[r][c] = now_ball
            # 다음 좌표
            r += BD[d][0]
            c += BD[d][1]
        # 방향, 거리 업데이트
        d = (d + 1) % 4
        if d % 2:  # 홀수번 째 = 거리 추가
            s += 1
    return new_field


size, magic = map(int, sys.stdin.readline().split())  # 맵 크기, 마법 횟수
field = [[] for _ in range(size)]  # 맵 정보
for i in range(size):
    field[i] = list(map(int, sys.stdin.readline().split()))
magic_lst = [[] for _ in range(magic)]  # 마법 정보
for i in range(magic):
    magic_lst[i] = list(map(int, input().split()))

MD = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 마법 방향 (북남서동)
BD = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 구슬 순회 방향 (남동북서)
ex_balls = [0] * 4  # 폭발한 구슬 리스트
for d, s in magic_lst:  # d(방향=(1(북), 2(남), 3(서), 4(동)), s(거리)
    now_r, now_c = size // 2, size // 2  # 초기 위치

    # 1. 블리자드 마법 사용
    field, isBlank = blizzard(now_r, now_c, d, s, field)

    # 2. 구슬 정보를 1차원으로 변환
    flat_field = find_blanks(now_r, now_c - 1, field)

    # 3. 구슬 폭발 + 이동
    while isBlank:
        flat_field, isBlank, ex_balls = explode(ex_balls, flat_field)

    # 4. 구슬 변환
    flat_field = change_balls(flat_field)

    # 5. 순회하면서 다시 자리에 넣기
    field = insert_balls(now_r, now_c - 1, size, flat_field)

ans = ex_balls[1] + ex_balls[2] * 2 + ex_balls[3] * 3
print(ans)