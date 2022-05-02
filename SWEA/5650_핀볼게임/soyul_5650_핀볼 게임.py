def go(now_i, now_j, k):

    start_i = now_i
    start_j = now_j
    score = 0

    while 1:
        now_i += di[k]
        now_j += dj[k]

        # 벽 만나면 점수 + 1, 방향 반대로
        if now_i < 0 or now_i >= n or now_j < 0 or now_j >= n:
            dir = k
            if dir == 0 or dir == 2:
                k += 1
            if dir == 1 or dir == 3:
                k -= 1
            score += 1
            continue

        # 처음으로 돌아왔다면 게임 끝
        if now_i == start_i and now_j == start_j:
            return score

        # 블랙홀에 빠지면 게임 끝
        if MAP[now_i][now_j] == -1:
            return score

        # 벽에 부딪혔다면 점수 + 1, 방향 변경
        if MAP[now_i][now_j] >= 1 and MAP[now_i][now_j] <= 5:
            score += 1
            wall = MAP[now_i][now_j]
            k = direction(k, wall)
            continue

        # 웜홀에 빠졌다면 다음 웜홀로
        if MAP[now_i][now_j] >= 6:
            num = MAP[now_i][now_j]
            if worm[num][0] == (now_i, now_j):
                now_i, now_j = worm[num][1]
            else:
                now_i, now_j = worm[num][0]


# 방향을 결정해주는 함수
def direction(dir, wall):

    # 네모를 만났으면 무조건 반대방향
    if wall == 5:
        if dir == 0 or dir == 2:
            return dir + 1
        if dir == 1 or dir == 3:
            return dir - 1

    # 첫 번째 벽을 만나면
    if wall == 1:
        if dir == 0:
            return 1
        elif dir == 1:
            return 3
        elif dir == 2:
            return 0
        else:
            return 2

    if wall == 2:
        if dir == 0:
            return 1
        elif dir == 1:
            return 2
        elif dir == 2:
            return 3
        else:
            return 0

    if wall == 3:
        if dir == 0:
            return 2
        elif dir == 1:
            return 0
        elif dir == 2:
            return 3
        else:
            return 1

    if wall == 4:
        if dir == 0:
            return 3
        elif dir == 1:
            return 0
        elif dir == 2:
            return 1
        else:
            return 2

T = int(input())
for tc in range(T):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 0, 1, -1]          # 우, 좌, 하, 상
    dj = [1, -1, 0, 0]

    start = []
    worm = [[] for _ in range(11)]

    for i in range(n):
        for j in range(n):
            if not MAP[i][j]:
                start.append((i, j))
            if MAP[i][j] >= 6:
                worm[MAP[i][j]].append((i, j))

    # 핀볼게임 시작
    score = 0
    for s in start:
        for k in range(4):
            score = max(score, go(s[0], s[1], k))


    print(f'#{tc+1} {score}')
