import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# 방향 전환 2차원 배열
turns = [[0] * 4 for _ in range(5)]
turns[0][1], turns[2][3], turns[3][2] = -1, -1, -1
turns[0][2], turns[1][1], turns[2][0] = 1, 1, 1
turns[1][0], turns[3][3] = 3, -3


for tc in range(T):
    answer = 0
    N = int(input())
    MAP = list(list(map(int, input().split())) for _ in range(N))


    # 웜홀의 번호와 위치만 쌍으로 저장한다.
    wormholes = dict()
    # 시작 가능한 위치들을 저장한다.
    start_points = []
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > 5:
                worm_idx = MAP[r][c]
                if wormholes.get(worm_idx):
                    wormholes[worm_idx].append((r, c))
                else:
                    wormholes[worm_idx] = [(r, c)]
            elif MAP[r][c] == 0:
                start_points.append((r, c))

    # 갈 수 있는 위치들 * 4방향
    for start in start_points:
        start_row, start_col = start[0], start[1]
        for direct in range(4):
            # 디버깅용 표기
            visited = [[0] * N for _ in range(N)]
            visited[start_row][start_col] = 1
            # find_answer(start_row, start_col, direct, 0)
            direction = direct
            count = 0
            now_row, now_col = start_row, start_col

            while True:
                next_row, next_col = now_row + dr[direction], now_col + dc[direction]

                # 벽을 넘는 경우
                if not (0 <= next_row < N and 0 <= next_col < N):
                    # 뒤돌아가
                    direction = (direction + 2) % 4
                    count += 1
                    continue

                number = MAP[next_row][next_col]
                # 끝나는 경우
                if number == -1 or (next_row == start_row and next_col == start_col):
                    answer = max(answer, count)
                    visited[next_row][next_col] = 'F'
                    break

                if number == 0:
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    now_row, now_col = next_row, next_col
                elif 0 < number < 6:
                    count += 1
                    # 방향 바꾸기
                    if not turns[number-1][direction]:
                        # 뒤집기
                        direction = (direction + 2) % 4
                    else:
                        # 90도 회전
                        direction = direction + turns[number-1][direction]
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    now_row, now_col = next_row, next_col
                else:
                    # 웜홀인 경우
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    if wormholes[number][0] == (next_row, next_col):
                        now_row, now_col = wormholes[number][1]
                    else:
                        now_row, now_col = wormholes[number][0]
            print(f"출발지점 : {start} ||| 출발 방향 : {direct} ||| 현재위치 : {next_row, next_col} ||| 최종 점수 : {count}")

    print(f"#{tc+1} {answer}")

