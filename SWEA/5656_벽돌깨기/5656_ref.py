"""
전건하, 실행시간 418ms / 메모리 65,896 kb

dfs안에서 너무 많은 일들을 하고 있다는게 단점이지만
백트랙킹 조건이 더 많고
중간에 비어있는 벽돌들을 아래로 내리는 과정이 더빠른 것 같다.
그리고 복사를 더 적은 횟수로 한 듯
어쩌면 나는 함수로 나눠서 parameter로 2차원 배열들을 더 빈번하게 넘겨서
더 오래걸린 것일 수도 있겠다.
"""
from collections import deque


def dfs(bricks, now_turn, all_brick_cnt):
    global lefts
    if not lefts:
        # 남은게 없다 -> 다 깨부쉈다.
        return
    if now_turn >= N:
        # 구슬을 N개 다 썼다.
        if lefts > cnt:
            lefts = cnt
        return
    if not all_brick_cnt:
        # 애초부터 벽돌이 없었다.
        lefts = 0
        return

    # 각 열을 보면서
    for col in range(W):
        # deepcopy를 쓰지 않고 배열을 직접 복사했다.
        copy_bricks = [line[:] for line in bricks]
        queue = deque()
        count = all_brick_cnt
        for row in range(H):
            # 값이 있다면
            if copy_bricks[row][col]:
                # (행, 열, value) 를 저장한다.
                queue.append((row, col, copy_bricks[row][col]))
                # 폭파 처리를 한다.
                copy_bricks[row][col] = 0
                # 남은 벽돌 개수를 1개 줄인다.
                count -= 1
                # 각 열당 값이 나오면 바로 터트린다...?
                break
        # queue가 빈 상태 = 하나의 column이 세로로 전부 0인 상황
        if not queue:
            # 다음 column으로 넘어감
            continue
        # 출발점을 찾았다면
        while queue:
            now_row, now_col, value = q.popleft()
            # 거리만큼 부숴줄 것이야
            for distance in range(1, value):
                for d in range(4):
                    next_row = now_row + distance * dx[d]
                    next_col = now_col + distance * dy[d]
                    # 범위 밖이라면 index에러 나니까 막고
                    if not (0 <= next_row < H and 0 <= next_col < W):
                        continue
                    # 0이라면 빈칸이니까 넘어가고
                    if not copy_bricks[next_row][next_col]:
                        continue
                    # 1보다 크면 다른 범위도 폭파할 수 있으니 덱에 넣어주고
                    if copy_bricks[next_row][next_col] > 1:
                        queue.append((next_row, next_col, copy_bricks[next_row][next_col]))
                    # 폭파처리 한 다음에
                    copy_bricks[next_row][next_col] = 0
                    # 남은 벽돌 수 하나 줄인다.
                    count -= 1
        # 다 터트렸으면 이제 아래로 내려주자.
        for col in range(W):
            # 우선 빈 공간이 높이값 그대로 라고 치고
            gap = H
            # 아래에서부터 위로 올라가면서 보는데
            for row in range(H - 1, -1, -1):
                # 해당 row, col에 값이 있다면
                if copy_bricks[row][col]:
                    # 만약 빈 공간에서 1개 뺀 값이 row와 같으면 벽돌끼리 공중에 빈 칸이 없는 상황인데, 다르다면 빈칸이 있는 상황임.
                    if gap - 1 != row:
                        # 비어있는 공간과 현재 row의 값을 교환한다.(자연스럽게 값을 아래로 내리고 0을 위로 올리는 행위)
                        copy_bricks[gap - 1][col], copy_bricks[row][col] = copy_bricks[row][col], copy_bricks[gap - 1][col]
                    # 격차를 줄인다.(빈칸이 없다면 row와 함께 위로 올라가야함.
                    gap -= 1
        dfs(copy_bricks, now_turn + 1, count)


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(T):
    N, W, H = map(int, input().split())
    bricks_map = [list(map(int, input().split())) for _ in range(H)]
    all_brick_cnt = 0
    for col in range(W):
        for row in range(H):
            if bricks_map[row][col]:
                all_brick_cnt += 1

    lefts = all_brick_cnt + 1
    dfs(bricks_map, 0, all_brick_cnt)
    print(f"#{tc + 1} {lefts}")