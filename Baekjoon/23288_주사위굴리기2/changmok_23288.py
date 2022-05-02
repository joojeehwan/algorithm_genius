# 55분
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bottom(dice):
    return dice[3][1]


def move_dice(dice, direction):
    '''
    dice = [
                [0, a, 0],
                [b, top, d],
                [0, e, 0],
                [0, bottom, 0]
            ]
    '''
    # 0 : east
    if direction == 0:
        moved_dice = [
            [0, dice[0][1], 0],
            [dice[3][1], dice[1][0], dice[1][1]],
            [0, dice[2][1], 0],
            [0, dice[1][2], 0]
        ]
    # 1 : south
    elif direction == 1:
        moved_dice = [
            [0, dice[3][1], 0],
            [dice[1][0], dice[0][1], dice[1][2]],
            [0, dice[1][1], 0],
            [0, dice[2][1], 0],
        ]
    # 2 : west
    elif direction == 2:
        moved_dice = [
            [0, dice[0][1], 0],
            [dice[1][1], dice[1][2], dice[3][1]],
            [0, dice[2][1], 0],
            [0, dice[1][0], 0]
        ]
    # 3 : north
    elif direction == 3:
        moved_dice = [
            [0, dice[1][1], 0],
            [dice[1][0], dice[2][1], dice[1][2]],
            [0, dice[3][1], 0],
            [0, dice[0][1], 0],
        ]
    return moved_dice


def next_direction(dice, d):
    a = bottom(dice)



n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score_board = [[0] * m for _ in range(n)]
went = [[False] * m for _ in range(n)]
dice = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]
]

for r in range(n):
    for c in range(m):
        if score_board[r][c] == 0:
            q = deque()
            history = [(r, c)]
            q.append((r, c))
            went[r][c] = True
            while q:
                nowr, nowc = q.popleft()
                for delta in range(4):
                    nexr = nowr + dr[delta]
                    nexc = nowc + dc[delta]
                    if not (0 <= nexr < n and 0 <= nexc < m):
                        continue
                    if went[nexr][nexc]:
                        continue
                    if board[nowr][nowc] != board[nexr][nexc]:
                        continue
                    history.append((nexr, nexc))
                    q.append((nexr, nexc))
                    went[nexr][nexc] = True
            score_assign = len(history)
            for sr, sc in history:
                score_board[sr][sc] = score_assign

r = 0
c = 0
d = 0

total = 0

for _ in range(k):
    nr = r + dr[d]
    nc = c + dc[d]
    if not (0 <= nr < n and 0 <= nc < m):
        d = (d + 2) % 4
        nr = r + dr[d]
        nc = c + dc[d]
    r, c = nr, nc
    total += score_board[r][c] * board[r][c]
    dice = move_dice(dice, d)
    if bottom(dice) > board[r][c]:
        d = (d + 1) % 4
    elif bottom(dice) < board[r][c]:
        d = (d - 1) % 4

print(total)