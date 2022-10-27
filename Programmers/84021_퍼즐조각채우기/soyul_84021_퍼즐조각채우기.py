def solution(game_board, table):
    n = len(game_board)

    # 게임 보드를 반시계방향으로 회전시키는 함수
    def rotate():
        rotate_table = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotate_table[i][j] = table[j][n - i - 1]

        return rotate_table

    # 게임 보드 빈 곳과 블럭의 인덱스를 뽑는 함수
    # flag가 1면 게임보드 검사, flag가 0이면 블럭 검사
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    def dfs(now_i, now_j, i, j, flag):

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            if flag == 1:
                if game_board[next_i][next_j]:
                    continue

                game_board[next_i][next_j] = 1
                emp.append([next_i - i, next_j - j])
                dfs(next_i, next_j, i, j, flag)
            else:
                if not table[next_i][next_j]:
                    continue

                table[next_i][next_j] = 0
                blc.append([next_i - i, next_j - j])
                dfs(next_i, next_j, i, j, flag)

        return

    # 비어있는 블럭들을 dfs로 검사해서 index저장 (0, 0을 기준으로 넣어줌)
    empty = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:  # 비어있는 곳이라면 검사
                game_board[i][j] = 1  # 방문 표시
                emp = []
                dfs(i, j, i, j, 1)
                empty.append(emp)

    answer = 0
    # 테이블을 회전시키면서 검사
    for _ in range(4):

        for i in range(n):
            for j in range(n):
                # 블럭이 있으면 검사해서 블럭 index 추출
                if table[i][j] == 1:
                    table[i][j] = 0
                    blc = []
                    dfs(i, j, i, j, 0)

                    # 그 블럭이 맞는 빈곳이 있다면
                    if blc in empty:
                        answer += (len(blc) + 1)
                        empty.remove(blc)
                    # 블럭이 맞는 곳이 없다면 아까 방문표시 했던 것들 다 풀어줌
                    else:
                        for x, y in blc:
                            table[x + i][y + j] = 1
                        table[i][j] = 1
        # 회전
        table = rotate()

    return answer