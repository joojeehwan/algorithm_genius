# import sys
# sys.stdin = open('input.txt', 'r')
"""
메모리 77056 실행시간 483
"""
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(T):
    N, M, K = map(int, input().split())
    half_K = K // 2
    # 시간이 19면 왼쪽에 9, 오른쪽에 10 이렇게 grid를 늘릴 수 없으므로 올림하고 2배해서 쓴다.
    # 그럼 2차원 배열이 들쑥날쑥 해지지 않는다.
    if K % 2:
        half_K += 1
    max_len = half_K * 2 + 2
    grid = [[0]*(M+max_len) for _ in range(N+max_len)]
    for row in range(half_K+1, half_K+N+1):
        grid[row] = [0]*(half_K+1) + list(map(int, input().split())) + [0]*(half_K+1)
    born_time = list([0]*(M+max_len) for _ in range(N+max_len))

    # 세포의 위치. 매번 완탐하기 싫어서
    pos = dict()
    for row in range(half_K+1, half_K+N+1):
        for col in range(half_K+1, half_K+M+1):
            if grid[row][col]:
                # 1차원 배열이면 갖게될 index를 key값으로 한다.
                pos[row*(M+max_len)+col] = (row, col)

    for now in range(1, K+1):
        remove_pos = list()
        add_pos = list()
        for key in pos.keys():
            cell_row, cell_col = pos[key][0], pos[key][1]
            cell_power = grid[cell_row][cell_col]
            cell_time = born_time[cell_row][cell_col]
            time_gap = now - cell_time

            # 괜히 여기서 if elif 쓰느라고 시간 다 날려먹었다......
            # 시간 계산하기가 은근 헷갈리고 어렵더라... 젠장...
            if time_gap == cell_power * 2:
                # 죽은 상태
                remove_pos.append(cell_row*(M+max_len)+cell_col)
            if now == cell_time + cell_power + 1:
                # 번식
                for d in range(4):
                    new_row = cell_row + dr[d]
                    new_col = cell_col + dc[d]

                    if not grid[new_row][new_col]:
                        grid[new_row][new_col] = cell_power
                    else:
                        # 누가 번식 해놨는데 같은 시간인데 내가 생명력이 더 크다 -> 동시에 왔으니 더 큰애가 먹는다.
                        if born_time[new_row][new_col] == now and cell_power > grid[new_row][new_col]:
                            grid[new_row][new_col] = cell_power
                        else:
                            # 누가 번식해놨는데 이전에 배양되었거나, 진행 안했는데 내가 더 작으면 추가할 이유 X
                            continue
                    # 출생 신고
                    born_time[new_row][new_col] = now
                    # 살아있는 세포 추가요~
                    add_pos.append((new_row, new_col))

        for remove_key in remove_pos:
            pos.pop(remove_key)
        for (add_row, add_col) in add_pos:
            pos[add_row*(M+max_len)+add_col] = (add_row, add_col)

    print(f"#{tc+1} {len(pos)}")