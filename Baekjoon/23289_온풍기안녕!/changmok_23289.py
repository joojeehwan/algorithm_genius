R, C, K = map(int, input().split())
room = list(list(map(int, input().split())) for _ in range(R))
heaters = []
watchlist = []
chocolate = 0
watchlist_warmed = False
for r in range(R):
    for c in range(C):
        num = room[r][c]
        if 1 <= num <= 4:
            heaters.append((r, c, num-1))
        elif num == 5:
            watchlist.append((r, c))
        room[r][c] = 0

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

reachable = (
                (((0, 0, 1),), ((0, 0, 0), (-1, 0, 1)), ((1, 0, 0), (1, 0, 1))),
                (((0, -1, 1),), ((0, 0, 0), (-1, -1, 1)), ((1, 0, 0), (1, -1, 1))),
                (((0, 0, 0),), ((0, -1, 0), (0, -1, 1)), ((0, 0, 1), (0, 1, 0))),
                (((1, 0, 0),), ((0, -1, 1), (1, -1, 0)), ((0, 0, 1), (1, 1, 0))),
)

delta = (
    ((0, 1), (-1, 1), (1, 1)),
    ((0, -1), (-1, -1), (1, -1)),
    ((-1, 0), (-1, -1), (-1, 1)),
    ((1, 0), (1, -1), (1, 1)),
)

temp_dr = [0, 1]
temp_dc = [1, 0]

W = int(input())
walls = dict()

for _ in range(W):
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    if walls.get((x, y)):
        walls[(x, y)].append(t)
    else:
        walls[(x, y)] = [t]

def check_route(row, col, direction):
    next_pos = set()
    for i in range(3):
        check_walls = reachable[direction][i]
        blocked = 0
        for check_row, check_col, wall_type in check_walls:
            next_row, next_col = row + check_row, col + check_col
            if walls.get((next_row, next_col)):
                if wall_type in walls.get((next_row, next_col)):
                    blocked += 1
        if not blocked:
            new_row, new_col = row + delta[direction][i][0], col+ delta[direction][i][1]
            if 0 <= new_row < R and 0 <= new_col < C:
                next_pos.add((new_row, new_col))

    return next_pos


def blow_phase():
    for h_row, h_col, h_dir in heaters:
        row, col = h_row+dr[h_dir], h_col+dc[h_dir]
        room[row][col] += 5

        next_pos = check_route(row, col, h_dir)

        for step in range(4):
            new_next_pos = set()
            for next_row, next_col in next_pos:
                room[next_row][next_col] += 4 - step
                found_nexts = check_route(next_row, next_col, h_dir)
                for found in found_nexts:
                    new_next_pos.add(found)
            next_pos = new_next_pos


def mix_phase():
    differences = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            now_num = room[r][c]
            for d in range(2):
                next_row, next_col = r + temp_dr[d], c + temp_dc[d]
                if d == 0:
                    if walls.get((r, c)) and 1 in walls.get((r, c)):
                        continue
                if d == 1:
                    if walls.get((r+1, c)) and 0 in walls.get((r+1, c)):
                        continue
                if next_row < R and next_col < C:
                    next_num = room[next_row][next_col]
                    if now_num > next_num:
                        diff = (now_num - next_num) // 4
                        differences[r][c] -= diff
                        differences[next_row][next_col] += diff
                    else:
                        diff = (next_num - now_num) // 4
                        differences[r][c] += diff
                        differences[next_row][next_col] -= diff

    for row in range(R):
        for col in range(C):
            room[row][col] += differences[row][col]


def cool_phase():
    for r in range(R):
        if r == 0 or r == R-1:
            for c in range(C):
                if room[r][c]:
                    room[r][c] -= 1
        else:
            if room[r][0]:
                room[r][0] -= 1
            if room[r][C-1]:
                room[r][C-1] -= 1


def check():
    for row, col in watchlist:
        if room[row][col] < K:
            return False
    return True


while not watchlist_warmed:
    if chocolate > 100:
        chocolate = 101
        break
    blow_phase()
    mix_phase()
    cool_phase()
    chocolate += 1
    watchlist_warmed = check()

print(chocolate)

# import math
# from collections import deque
#
# facing = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]
#
# def wall_up(r, c):
#     return 0 in walls.get((r, c), [])
# def wall_down(r, c):
#     return 0 in walls.get((r+1, c), [])
# def wall_left(r, c):
#     return 1 in walls.get((r, c-1), [])
# def wall_right(r, c):
#     return 1 in walls.get((r, c), [])
#
#
# def spread(row, col, face):
#     temp_add = [[0] * C for _ in range(R)]
#     temp_add[row][col] = 5
#     q = deque()
#     q.append((row, col, 5))
#     while q:
#         r, c, h = q.popleft()
#         if face == 1:
#             # straight
#             if c + 1 < C and not wall_right(r, c) and temp_add[r][c + 1] == 0:
#                 temp_add[r][c + 1] = h - 1
#                 q.append((r, c + 1, h - 1))
#             if r - 1 >= 0 and not wall_up(r, c):
#                 if c + 1 < C and not wall_right(r - 1, c) and temp_add[r - 1][c + 1] == 0:
#                     temp_add[r - 1][c + 1] = h - 1
#                     q.append((r - 1, c + 1, h - 1))
#             if r + 1 < R and not wall_down(r, c):
#                 if c + 1 < C and not wall_right(r + 1, c) and temp_add[r + 1][c + 1] == 0:
#                     temp_add[r + 1][c + 1] = h - 1
#                     q.append((r + 1, c + 1, h - 1))
#         if face == 2:
#             if c - 1 >= 0 and not wall_left(r, c) and temp_add[r][c - 1] == 0:
#                 temp_add[r][c - 1] = h - 1
#                 q.append((r, c - 1, h - 1))
#             if r - 1 >= 0 and not wall_up(r, c):
#                 if c - 1 >= 0 and not wall_left(r - 1, c) and temp_add[r - 1][c - 1] == 0:
#                     temp_add[r - 1][c - 1] = h - 1
#                     q.append((r - 1, c - 1, h - 1))
#             if r + 1 < R and not wall_down(r, c):
#                 if c - 1 >= 0 and not wall_left(r + 1, c) and temp_add[r + 1][c - 1] == 0:
#                     temp_add[r + 1][c - 1] = h - 1
#                     q.append((r + 1, c - 1, h - 1))
#         if face == 3:
#             if r - 1 >= 0 and not wall_up(r, c) and temp_add[r - 1][c] == 0:
#                 temp_add[r - 1][c] = h - 1
#                 q.append((r - 1, c, h - 1))
#             if c - 1 >= 0 and not wall_left(r, c):
#                 if r - 1 >= 0 and not wall_up(r, c - 1) and temp_add[r - 1][c - 1] == 0:
#                     temp_add[r - 1][c - 1] = h - 1
#                     q.append((r - 1, c - 1, h - 1))
#             if c + 1 < C and not wall_right(r, c):
#                 if r - 1 >= 0 and not wall_up(r, c + 1) and temp_add[r - 1][c + 1] == 0:
#                     temp_add[r - 1][c + 1] = h - 1
#                     q.append((r - 1, c + 1, h - 1))
#         if face == 4:
#             if r + 1 < R and not wall_down(r, c) and temp_add[r + 1][c] == 0:
#                 temp_add[r + 1][c] = h - 1
#                 q.append((r + 1, c, h - 1))
#             if c - 1 >= 0 and not wall_left(r, c):
#                 if r + 1 < R and not wall_down(r, c - 1) and temp_add[r + 1][c - 1] == 0:
#                     temp_add[r + 1][c - 1] = h - 1
#                     q.append((r + 1, c - 1, h - 1))
#             if c + 1 < C and not wall_right(r, c):
#                 if r + 1 < R and not wall_down(r, c + 1) and temp_add[r + 1][c + 1] == 0:
#                     temp_add[r + 1][c + 1] = h - 1
#                     q.append((r + 1, c + 1, h - 1))
#     for ar in range(R):
#         for ac in range(C):
#             temperature[ar][ac] += temp_add[ar][ac]
#
#
# R, C, K = map(int, input().split())
# left = 0
# right = C-1
# top = 0
# bot = R-1
# room = [list(map(int, input().split())) for _ in range(R)]
# temperature = [[0] * C for _ in range(R)]
# heaters = []
# watchlist = []
# for r in range(R):
#     for c in range(C):
#         if 1 <= room[r][c] <= 4:
#             heaters.append((r, c, room[r][c]))
#         elif room[r][c] == 5:
#             watchlist.append((r, c))
# w = int(input())
# walls = {}
# for _ in range(w):
#     x, y, t = map(int, input().split())
#     if walls.get((x-1, y-1)):
#         walls[(x-1, y-1)].append(t)
#     else:
#         walls[(x-1, y-1)] = [t]
#
# chocolate = 0
# watchlist_warmed = False
# while not watchlist_warmed:
#     # blow phase
#     for heater in heaters:
#         r, c, f = heater
#         r += facing[f][0]
#         c += facing[f][1]
#         spread(r, c, f)
#     # mix phase
#     temp_change = [[0] * C for _ in range(R)]
#     for r in range(R):
#         for c in range(C):
#             # right
#             if c < C-1 and not wall_right(r, c):
#                 diff = abs(temperature[r][c] - temperature[r][c+1])
#                 change = math.floor(diff / 4)
#                 if temperature[r][c] > temperature[r][c+1]:
#                     temp_change[r][c] -= change
#                     temp_change[r][c+1] += change
#                 elif temperature[r][c] < temperature[r][c+1]:
#                     temp_change[r][c] += change
#                     temp_change[r][c+1] -= change
#             if r < R-1 and not wall_down(r, c):
#                 diff = abs(temperature[r][c] - temperature[r+1][c])
#                 change = math.floor(diff / 4)
#                 if temperature[r][c] > temperature[r+1][c]:
#                     temp_change[r][c] -= change
#                     temp_change[r+1][c] += change
#                 elif temperature[r][c] < temperature[r+1][c]:
#                     temp_change[r][c] += change
#                     temp_change[r+1][c] -= change
#     for r in range(R):
#         for c in range(C):
#             temperature[r][c] += temp_change[r][c]
#     # cool edge phase
#     # top and bottom
#     # top, bot, left, right = stretch()
#     for r in range(R):
#         if r == 0 or r == R - 1:
#             for c in range(C):
#                 if temperature[r][c]:
#                     temperature[r][c] -= 1
#         else:
#             if temperature[r][0]:
#                 temperature[r][0] -= 1
#             if temperature[r][C - 1]:
#                 temperature[r][C - 1] -= 1
#     # chocolate
#     chocolate += 1
#     if chocolate > 100:
#         break
#
#     # check watchlist
#     watchlist_warmed = True
#     for (wr, wc) in watchlist:
#         if temperature[wr][wc] < K:
#             watchlist_warmed = False
#             break
#
# print(chocolate)