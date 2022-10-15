def move_tornado(s, now_r, now_c):
    if 0 <= now_r + direction[s][0] < size and 0 <= now_c + direction[s][1] < size:
        return now_r + direction[s][0], now_c + direction[s][1]
    else:
        return -1, -1


def move_sand(s, now_r, now_c, ans):
    # 현재 위치 모래 양 확인하기
    sand = field[now_r][now_c]
    if not sand:
        return ans

    for idx in range(9):
        # 모래 흩어지는 방향 확인하기
        if idx // 5:
            idx %= 5
            if s == 0:  # 서쪽
                now_sand_direction = (-sand_direction[idx][0], sand_direction[idx][1])
            elif s == 1:  # 남쪽
                now_sand_direction = (-sand_direction[idx][1], -sand_direction[idx][0])
            elif s == 2:  # 동쪽
                now_sand_direction = (-sand_direction[idx][0], -sand_direction[idx][1])
            else:  # 북쪽
                now_sand_direction = (sand_direction[idx][1], sand_direction[idx][0])
        else:
            if s == 0:  # 서쪽
                now_sand_direction = sand_direction[idx]
            elif s == 1:  # 남쪽
                now_sand_direction = (-sand_direction[idx][1], sand_direction[idx][0])
            elif s == 2:  # 동쪽
                now_sand_direction = (sand_direction[idx][0], -sand_direction[idx][1])
            else:  # 북쪽
                now_sand_direction = (sand_direction[idx][1], -sand_direction[idx][0])
        new_sand_row = now_row + now_sand_direction[0]
        new_sand_col = now_col + now_sand_direction[1]
        if idx == 4:  # 남은 모래 이동할 방향 저장
            moving_sand_direction = (now_sand_direction[0] // 2, now_sand_direction[1] // 2)
        # 흩어지는 모래 양 확인하기
        now_sand_weight = sand_weight[idx]
        # 모래 흩어지기
        if 0 <= new_sand_row < size and 0 <= new_sand_col < size:  # 맵 안
            field[new_sand_row][new_sand_col] += int(sand * now_sand_weight)
        else:  # 맵 밖
            ans += int(sand * now_sand_weight)
        field[now_row][now_col] -= int(sand * now_sand_weight)
    # 남은 모래 이동하기
    if 0 <= now_row + moving_sand_direction[0] < size and 0 <= now_col + moving_sand_direction[1] < size:
        field[now_row + moving_sand_direction[0]][now_col + moving_sand_direction[1]] += field[now_row][now_col]
    else:
        ans += field[now_row][now_col]
    field[now_row][now_col] = 0
    return ans


size = int(input())  # 격자 크기
field = [[] for _ in range(size)]  # 격자 상태
for r in range(size):
    field[r] = list(map(int, input().split()))
ans = 0

# 토네이도 상태
now_row, now_col = size // 2, size // 2  # 시작지점
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 이동 방향(서남동북)
weight = 1  # 이동 거리
seed = 0

# 모래 상태
sand_direction = [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2)]  # 모래가 이동하는 방향
sand_weight = [0.02, 0.1, 0.07, 0.01, 0.05]  # 모래가 이동하는 양


while now_row != 0 or now_col != 0:  # (1, 1)에 도착할 때까지
    # direction 방향으로 weight 만큼 이동
    for _ in range(weight):
        # 토네이도 이동
        result = move_tornado(seed % 4, now_row, now_col)
        if result == (-1, -1):
            break
        else:
            now_row, now_col = result
        # 모래 이동
        ans = move_sand(seed % 4, now_row, now_col, ans)
    # 방향 전환
    seed += 1
    if seed % 4 == 0 or seed % 4 == 2:
        weight += 1

print(ans)