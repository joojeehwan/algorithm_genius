"""
뭐야 엄청 간단하게 풀었잖아...
https://developer-ellen.tistory.com/68
"""

import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    line = []
    for j in range(4):
        # 물고기 번호, 방향
        line.append([data[2*j], data[2*j+1]-1])
    board[i] = line


max_score = 0


def dfs(shark_row, shark_col, score, board):
    global max_score
    score += board[shark_row][shark_col][0]
    max_score = max(max_score, score)
    # 이미 먹어버렸어
    board[shark_row][shark_col][0] = 0

    # 물고기 움직임
    for f_idx in range(1, 17):
        fish_row, fish_col = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f_idx:
                    # 물고기 위치 찾음
                    fish_row, fish_col = x, y
                    break
        if fish_row == -1 and fish_col == -1:
            continue
        fish_direction = board[fish_row][fish_col][1]

        for i in range(8):
            next_direction = (fish_direction+i) % 8
            next_row = fish_row + dx[next_direction]
            next_col = fish_col + dy[next_direction]
            # 범위 밖이거나, 상어의 위치이거나(상어의 위치가 shark_row, shark_col)
            if not (0 <= next_row < 4 and 0 <= next_col < 4) or (next_row == shark_row and next_col == shark_col):
                continue
            # 새로운 방향을 저장해주고
            board[fish_row][fish_col][1] = next_direction
            # 기존의 값과 새로운 값을 바꿈
            board[fish_row][fish_col], board[next_row][next_col] = board[next_row][next_col], board[fish_row][fish_col]
            break

    # 상어가 물고기 먹으러감
    shark_dir = board[shark_row][shark_col][1]
    for i in range(1, 5):
        next_row = shark_row + dx[shark_dir]*i
        next_col = shark_col + dy[shark_dir]*i
        if (0 <= next_row < 4 and 0 <= next_col < 4) and board[next_row][next_col][0] > 0:
            dfs(next_row, next_col, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)