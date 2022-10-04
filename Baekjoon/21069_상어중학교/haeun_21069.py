from collections import deque

N, M = map(int, input().split())
blank = M+4  # 빈칸을 표현하기 위한 숫자
grid = list(list(map(int, input().split())) for _ in range(N))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
score = 0


def finding_block_groups():
    # 방문배열을 2개 사용. 일반 블록을 기준으로 빠르게 넘기기 위한 color_visited
    color_visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            color = grid[r][c]  # 블록 그룹의 색상
            # 검은색, 무지개 블록으로는 시작하지 않는다.
            if not (0 < color <= M) or color_visited[r][c]:
                continue
            color_visited[r][c] = 1
            queue = deque([(r, c)])  # 블록 그룹은 상하좌우로 이어져있어야한다.
            block_group = [(r, c)]  # 블록 그룹을 저장할 배열
            group_visited = [[0] * N for _ in range(N)]  # 그룹 내에서는 무지개도 방문 처리 해야해서
            group_visited[r][c] = 1
            group_rainbow = 0  # 무지개 개수

            # BFS
            while queue:
                now_r, now_c = queue.popleft()

                for d in range(4):
                    next_r, next_c = now_r + dr[d], now_c + dc[d]
                    # 범위를 넘으면 안된다.
                    if not (0 <= next_r < N and 0 <= next_c < N):
                        continue
                    # 이미 방문한데도 안된다.
                    if group_visited[next_r][next_c]:
                        continue
                    next_color = grid[next_r][next_c]
                    # 검은색, 다른색은 skip
                    if next_color == -1 or 0 < next_color != color:
                        continue
                    # 자연수. 방문했다고 표기
                    if 0 < next_color <= M:
                        color_visited[next_r][next_c] = 1
                    # 무지개 개수 세어야됨
                    if next_color == 0:
                        group_rainbow += 1
                    group_visited[next_r][next_c] = 1

                    block_group.append((next_r, next_c))
                    queue.append((next_r, next_c))

            block_len = len(block_group)
            if block_len >= 2:
                # 무지개 블록이 가장 위의 왼쪽에 있을 수도 업성!! 무지개 블록은 기준 블록이 안된다고!!
                block_groups.append([block_len, group_rainbow, r, c, block_group])

    # 블록 그룹들을 정렬한다.
    if block_groups:
        block_groups.sort(key=lambda x: (x[0], x[1], x[2], x[3]), reverse=True)
        return True
    else:
        return False


def remove_group(group):
    # print(group)
    blocks = group[4]
    for block_r, block_c in blocks:
        # 빈칸을 뭐로 만들지 몰라서 범위 밖의 수로 정함
        grid[block_r][block_c] = blank
    return (group[0]) ** 2


def gravity():
    for col in range(N):
        empty = 0
        for row in range(N-1, -1, -1):
            color = grid[row][col]
            if 0 <= color <= M:
                grid[row+empty][col] = color
            elif color == -1:
                # 검은 블록을 만난다면 지금까지 센 빈칸에 맞춰 내려준다.
                for empty_r in range(empty):
                    grid[empty_r+row+1][col] = blank
                empty = 0
            else:
                empty += 1

        for row in range(empty):
            grid[row][col] = blank


def rotate():
    rotate_grid = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            rotate_grid[N-col-1][row] = grid[row][col]
    return rotate_grid


while True:
    block_groups = list()  # 블록 그룹들을 저장하는 배열
    searching = finding_block_groups()
    if searching:
        score += remove_group(block_groups[0])
        gravity()
        grid = rotate()
        gravity()
    else:
        break

print(score)
