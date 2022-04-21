dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def count(bricks, w, h):
    cnt = 0
    for r in range(h):
        for c in range(w):
            if bricks[r][c]:
                cnt += 1
    return cnt


def gravity(marked_bricks):
    for c in range(w):
        stack = []
        for r in range(h):
            if marked_bricks[r][c]:
                stack.append(marked_bricks[r][c])
                marked_bricks[r][c] = 0
        rr = h
        while stack:
            rr -= 1
            marked_bricks[rr][c] = stack.pop()
    return marked_bricks


def mark(copied_bricks, r, c, w, h):
    chain = copied_bricks[r][c]
    copied_bricks[r][c] = 0
    for d in range(4):
        for i in range(1, chain):
            nr = r + dr[d] * i
            nc = c + dc[d] * i
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if not copied_bricks[nr][nc]:
                continue
            if copied_bricks[nr][nc] > 1:
                mark(copied_bricks, nr, nc, w, h)
                continue
            copied_bricks[nr][nc] = 0
    return copied_bricks


def initialise(og_bricks, dropped, n, w, h):
    if dropped == n:
        global record
        record = min(record, count(og_bricks, w, h))
        return
    for c in range(w):
        for r in range(h):
            if og_bricks[r][c]:
                copied_bricks = [row[:] for row in og_bricks]
                marked_bricks = mark(copied_bricks, r, c, w, h)
                dropped_bricks = gravity(marked_bricks)
                initialise(dropped_bricks, dropped+1, n, w, h)
                break


for t in range(1, int(input())+1):
    n, w, h = map(int, input().split())

    bricks = [list(map(int, input().split())) for _ in range(h)]
    record = 13 * 16 + 1

    initialise(bricks, 0, n, w, h)

    if record == 13 * 16 + 1:
        record = 0

    print(f'#{t} {record}')