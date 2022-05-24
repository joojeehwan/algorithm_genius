"""
https://chelseashin.tistory.com/31

47개까지 틀리고 디버깅 해봐도 왜 틀렸는지 모르겠어서 답을 찾아봤는데
내가 생각하는 차이점은 방향 전환을 너무 헷갈리게 만들어서 잘 못 만든 것 같음
"""

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 방향 전환 2차원 배열
turns = (
    (1, 3, 0, 2),
    (3, 0, 1, 2),
    (2, 0, 3, 1),
    (1, 2, 3, 0),
    (1, 0, 3, 2),
         )


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
                # 있는 웜홀이면 추가
                if wormholes.get(worm_idx):
                    wormholes[worm_idx].append((r, c))
                # 처음이면 생성
                else:
                    wormholes[worm_idx] = [(r, c)]
            elif MAP[r][c] == 0:
                # 갈 수 있는 빈칸들만 따로 저장
                start_points.append((r, c))

    # 갈 수 있는 위치들 * 4방향
    for start in start_points:
        start_row, start_col = start[0], start[1]
        for start_direct in range(4):
            # 초기화
            direction = start_direct
            count = 0
            row, col = start_row, start_col

            while True:
                # next, now 나눴는데 그냥 합침
                row += dr[direction]
                col += dc[direction]

                # 벽을 넘는 경우
                if not (0 <= row < N and 0 <= col < N):
                    count += 1
                    # 반대로 튕겨나가게, 5번 블록이랑 부딪힌 셈
                    direction = turns[4][direction]
                else:
                    num = MAP[row][col]
                    # 끝나는 경우
                    if num == -1 or (row == start_row and col == start_col):
                        answer = max(answer, count)
                        break
                    # 블록인 경우
                    elif 1 <= num <= 5:
                        count += 1
                        direction = turns[num-1][direction]
                    # 웜홀인 경우
                    elif 6 <= num <= 10:
                        # 지금 번호와 같지만 위치가 다른 웜홀로 이동
                        if wormholes[num][0] == (row, col):
                            row, col = wormholes[num][1][0], wormholes[num][1][1]
                        else:
                            row, col = wormholes[num][0][0], wormholes[num][0][1]

    print(f"#{tc+1} {answer}")