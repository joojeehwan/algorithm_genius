from collections import deque

R, C = map(int, input().split())
grid = list(list(input()) for _ in range(R))
plan = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]
north, west, east, south = (-1, 0), (0, -1), (0, 1), (1, 0)
# 북, 서, 남, 동 순으로 +2로 반대되게끔
delta = [north, west, south, east]
block = {".": 0, "|": 1, "-": 2, "+": 3, "1": 4, "2": 5, "3": 6, "4": 7, "M": 0, "Z": 0}
reverse_block = {1: "|", 2: "-", 3: "+", 4: "1", 5: "2", 6: "3", 7: "4"}
# .(빈칸) | - + 1 2 3 4 순으로 파이프가 갈 수 있는 곳 방향 정함
pipe = [[], [north, south], [west, east], [north, west, east, south], [east, south], [north, east], [north, west],
        [west, south]]


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def bfs(r, c):
    queue = deque([(r, c)])

    while queue:
        row, col = queue.popleft()
        p_type = plan[row][col]
        visited[row][col] = 1

        for dr, dc in pipe[p_type]:
            n_row, n_col = row + dr, col + dc
            if in_range(n_row, n_col) and not visited[n_row][n_col]:
                if plan[n_row][n_col]:
                    queue.append((n_row, n_col))
                    visited[n_row][n_col] = 1
                else:
                    return n_row, n_col, (-dr, -dc)


def is_connected(br, bc, nr, nc):
    for dr, dc in pipe[plan[nr][nc]]:
        if br == nr+dr and bc == nc+dc:
            return True
    return False


def simulation():
    # 초기화
    for i in range(R):
        for j in range(C):
            plan[i][j] = block.get(grid[i][j])
            if grid[i][j] == "M":
                moscow = (i, j)
                visited[i][j] = 1

    # 모스크바와 이어진 블록을 찾는다.
    for dr, dc in delta:
        nr, nc = moscow[0] + dr, moscow[1] + dc
        if in_range(nr, nc) and plan[nr][nc]:
            # 빈칸을 찾아와라!
            b_row, b_col, b_dir = bfs(nr, nc)
            break
    blank_pipe = [b_dir]

    # 빈 칸과 연결된 파이프를 찾는다. 그래서 빈 칸에 들어가야할 파이프의 종류를 알아낸다.
    for dr, dc in delta:
        nr, nc = b_row + dr, b_col + dc
        if in_range(nr, nc) and not visited[nr][nc] and plan[nr][nc]:
            # 해당 파이프에서 내 쪽으로 올 수 있는가? (이미 지나온 곳은 제외)
            if is_connected(b_row, b_col, nr, nc):
                blank_pipe.append((dr, dc))

    for idx in range(8):
        if pipe[idx] == sorted(blank_pipe):
            print(b_row + 1, b_col + 1, reverse_block.get(idx))


simulation()
