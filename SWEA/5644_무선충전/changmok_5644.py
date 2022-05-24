# 콩시간 콩분

from collections import deque

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]


def put(row, col, i, p):
    if (row, col) in power_grid:
        power_grid[(row, col)].append((p, i))
    else:
        power_grid[(row, col)] = [(p, i)]


def add_power(ar, ac, br, bc):
    power_overlap = [[], []]
    a_power = b_power = False
    if (ar, ac) in power_grid:
        a_power = True
        for powers in power_grid[(ar, ac)]:
            power_overlap[0].append(powers)
    if (br, bc) in power_grid:
        b_power = True
        for powers in power_grid[(br, bc)]:
            power_overlap[1].append(powers)

    power_overlap = list(power_overlap)
    if a_power and b_power:
        if power_overlap[0][0] != power_overlap[1][0]:
            return power_overlap[0][0][0] + power_overlap[1][0][0]
        else:
            if len(power_overlap[0]) == 1 and len(power_overlap[1]) == 1:
                return power_overlap[0][0][0]
            elif len(power_overlap[0]) >= 2 and len(power_overlap[1]) == 1:
                return power_overlap[0][1][0] + power_overlap[1][0][0]
            elif len(power_overlap[0]) == 1 and len(power_overlap[1]) >= 2:
                return power_overlap[0][0][0] + power_overlap[1][1][0]
            else:
                return power_overlap[0][0][0] + max(power_overlap[1][1][0], power_overlap[0][1][0])
    elif a_power:
        return power_overlap[0][0][0]
    elif b_power:
        return power_overlap[1][0][0]
    else:
        return 0


for t in range(1, int(input())+1):
    m, a = map(int, input().split())
    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))

    answer = 0
    chargers = []
    for i in range(a):
        x, y, c, p = map(int, input().split())
        chargers.append((p, y-1, x-1, c, i))
    chargers.sort(reverse=True)

    power_grid = {}
    for i in range(a):
        p, row, col, c, index = chargers[i]
        put(row, col, i, p)
        q = deque([(row, col, 0)])
        v = [(row, col)]
        while q:
            cr, cc, cd = q.popleft()
            if cd >= c:
                continue
            for D in range(1, 5):
                nr = cr + dr[D]
                nc = cc + dc[D]
                if not (0 <= nr < 10 and 0 <= nc < 10):
                    continue
                if (p, i) in power_grid.get((nr, nc), []):
                    continue
                put(nr, nc, i, p)
                q.append((nr, nc, cd + 1))

    ar, ac = 0, 0
    br, bc = 9, 9

    answer += add_power(ar, ac, br, bc)

    for mi in range(m):
        ar += dr[a_move[mi]]
        ac += dc[a_move[mi]]
        br += dr[b_move[mi]]
        bc += dc[b_move[mi]]

        answer += add_power(ar, ac, br, bc)

    print(f'#{t} {answer}')