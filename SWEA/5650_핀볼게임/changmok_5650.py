# 18:49 시작 19:29 스탑 19:45 재개 21:09 첫 풀이 21:27 원하는 풀이


# 첫번째 풀이
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bounce(d, wall):
    wall_bound = [
        [],
        [2, 3, 1, 0],
        [1, 3, 0, 2],
        [3, 2, 0, 1],
        [2, 0, 3, 1],
        [2, 3, 0, 1]
    ]
    return wall_bound[wall][d]


def start(r, c, d):
    sr, sc = r, c
    score = 0
    while True:
        r += dr[d]
        c += dc[d]
        if not (0 <= r < n and 0 <= c < n):
            d = bounce(d, 5)
            score += 1
            continue
        if (r, c) == (sr, sc) or game[r][c] == -1:
            return score
        if 6 <= game[r][c]:
            if (r, c) == wormholes[game[r][c] - 6][0]:
                r, c = wormholes[game[r][c] - 6][1]
            else:
                r, c = wormholes[game[r][c] - 6][0]
            continue
        if 1 <= game[r][c] <= 5:
            d = bounce(d, game[r][c])
            score += 1
            continue


for t in range(1, int(input()) + 1):
    n = int(input())
    game = [list(map(int, input().split())) for _ in range(n)]
    highest = 0

    wormholes = [[] for _ in range(5)]
    blanks = []

    for row in range(n):
        for col in range(n):
            if game[row][col] == 0:
                blanks.append((row, col))
                continue
            if game[row][col] >= 6:
                wormholes[game[row][col] - 6].append((row, col))
                continue

    for blank in blanks:
        for direction in range(4):
            this_score = start(blank[0], blank[1], direction)
            highest = max(highest, this_score)

    print(f'#{t} {highest}')


# 원했던 백트래킹이 약간 가미된 풀이 (오히려 손해 (시박거))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bounce(d, wall):
    wall_bound = [
        [],
        [-1, -1, 1, 0],
        [1, -1, -1, 2],
        [3, 2, -1, -1],
        [-1, 0, 3, -1],
        [-1, -1, -1, -1]
    ]
    return wall_bound[wall][d]


def start(r, c, d):
    sr, sc = r, c
    score = 0
    while True:
        r += dr[d]
        c += dc[d]
        if not (0 <= r < n and 0 <= c < n):
            return 2 * score + 1, 2
        if (r, c) == (sr, sc) or game[r][c] == -1:
            return score, 1
        if game[r][c] >= 6:
            if (r, c) == wormholes[game[r][c] - 6][0]:
                r, c = wormholes[game[r][c]-6][1]
            else:
                r, c = wormholes[game[r][c]-6][0]
            continue
        if 1 <= game[r][c] <= 5:
            d = bounce(d, game[r][c])
            if d == -1:
                return 2 * score + 1, 2
            score += 1
            continue
        if game[r][c] == 0:
            if score_grid[d][r][c][0] and score_grid[d][r][c][1] == 2:
                return 2 * score + score_grid[d][r][c][0], 2
            continue


for t in range(1, int(input()) + 1):
    n = int(input())
    game = [list(map(int, input().split())) for _ in range(n)]
    highest = 0
    score_grid = [[[(0,)] * n for _ in range(n)]for __ in range(4)]

    wormholes = [[] for _ in range(5)]
    blanks = []

    for row in range(n):
        for col in range(n):
            if game[row][col] == 0:
                blanks.append((row, col))
                continue
            if game[row][col] >= 6:
                wormholes[game[row][col]-6].append((row, col))
                continue

    for blank in blanks:
        for direction in range(4):
            this_score, is_returning = start(blank[0], blank[1], direction)
            score_grid[direction][blank[0]][blank[1]] = (this_score, is_returning)
            highest = max(highest, this_score)

    print(f'#{t} {highest}')