# import sys
# sys.stdin = open("2382_input.txt", "r")

T = int(input())

# 상1, 하2, 좌3, 우4
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microbes = dict()

    # 미생물 해쉬 처리
    for _ in range(K):
        r, c, m, d = map(int, input().split())  # 행, 열, 미생물 수, 방향
        if microbes.get((r, c)):
            microbes[(r, c)].append([m, d])
        else:
            microbes[(r, c)] = [[m, d]]

    for _ in range(M):
        move_microbes = dict()
        for row, col in microbes.keys():

            now_microbes = microbes.get((row, col))
            for count, direction in now_microbes:
                new_row = row + dr[direction]
                new_col = col + dc[direction]

                if new_row == 0 or new_row == N-1 or new_col == 0 or new_col == N-1:
                    count //= 2
                    if direction % 2:
                        direction += 1
                    else:
                        direction -= 1

                if count > 0:
                    if move_microbes.get((new_row, new_col)):
                        move_microbes[(new_row, new_col)].append([count, direction])
                    else:
                        move_microbes[(new_row, new_col)] = [[count, direction]]

        for row, col in move_microbes.keys():
            if len(move_microbes.get((row, col))) > 1:
                move_microbes[(row, col)].sort(reverse=True)
                many_microbe = move_microbes[(row, col)][0]
                direction = many_microbe[1]
                sum_microbe = 0
                for m, d in move_microbes[(row, col)]:
                    sum_microbe += m
                move_microbes[(row, col)] = [(sum_microbe, direction)]

        microbes = move_microbes

    answer = 0
    for pos_microbes in microbes.values():
        for microbe in pos_microbes:
            answer += microbe[0]
    print(f"#{tc} {answer}")

