"""
풀이시간 : 2시간 이상
"""

answer = 0
N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))

# 델타
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

HALF = N // 2


def print_grid(turn):
    print(f" >>>>>>>>>> {turn} <<<<<<<<<< ")
    for line in grid:
        print(*line)
    print()

# 입력받은 1차원 배열을 그리드에 채운다.
# 4개 이상의 몬스터가 연속으로 있는지도 확인한다.
def fill_grid(monsters):
    new_grid = [[0] * N for _ in range(N)]
    row, col = HALF, HALF
    dct = 2
    m_idx = 0
    m_cnt = len(monsters)
    more_than_four = False

    if m_cnt > 0:
        prv_num, prv_cnt = monsters[0], 1
        for i in range(1, m_cnt):
            if monsters[i] == prv_num:
                prv_cnt += 1
                if prv_cnt > 3:
                    more_than_four = True
                    break
            else:
                prv_cnt = 1
                prv_num = monsters[i]

        for limit in range(1, N):
            for _ in range(2):
                for _ in range(limit):
                    if m_idx == m_cnt:
                        break
                    row += dr[dct]
                    col += dc[dct]
                    new_grid[row][col] = monsters[m_idx]
                    m_idx += 1
                dct = (dct - 1) % 4

        for _ in range(N - 1):
            if m_idx == m_cnt:
                break
            row += dr[dct]
            col += dc[dct]
            new_grid[row][col] = monsters[m_idx]
            m_idx += 1

    for r in range(N):
        grid[r] = new_grid[r][:]

    return more_than_four


# 플레이어 공격
def attack(dct, power):
    global answer
    row, col = HALF, HALF

    for _ in range(power):
        row += dr[dct]
        col += dc[dct]
        answer += grid[row][col]
        grid[row][col] = 0


# 한칸씩 돌면서 몬스터 리스트에 담아 빈칸 없애기
def line_monster():
    monsters = []
    row, col = HALF, HALF
    dct = 2

    for limit in range(1, N):
        for _ in range(2):
            for _ in range(limit):
                row += dr[dct]
                col += dc[dct]
                if grid[row][col]:
                    monsters.append(grid[row][col])
            dct = (dct - 1) % 4

    # 마지막 맨 윗 줄
    for _ in range(N-1):
        row += dr[dct]
        col += dc[dct]
        if grid[row][col]:
            monsters.append(grid[row][col])

    return monsters


# 달팽이 + 몬스터 수 세면서 삭제
def kill_more_than_four():
    global answer
    monsters = []
    row, col = HALF, HALF
    dct = 2

    prv_num, prv_cnt = grid[row][col-1], 0

    # 플레이어 왼쪽에 숫자가 있는 경우
    if prv_num:
        # 달팽이로 돌면서
        for limit in range(1, N):
            for _ in range(2):
                for _ in range(limit):
                    row += dr[dct]
                    col += dc[dct]

                    if prv_num == 0 and grid[row][col] == 0:
                        return monsters

                    # 이전 숫자와 같으면 개수 추가
                    if grid[row][col] == prv_num:
                        prv_cnt += 1
                    else:
                        # 4개 이상이면 삭제라 점수 추가
                        if prv_cnt > 3:
                            answer += (prv_num * prv_cnt)
                        # 3개 이하면 monsters에 추가
                        else:
                            monsters += [prv_num] * prv_cnt
                        # 바뀐 숫자므로 어쨌든 1로 초기화
                        prv_cnt = 1
                        prv_num = grid[row][col]
                dct = (dct - 1) % 4

        for limit in range(N-1):
            row += dr[dct]
            col += dc[dct]

            if prv_num == 0 and grid[row][col] == 0:
                return monsters

            # 이전 숫자와 같으면 개수 추가
            if grid[row][col] == prv_num:
                prv_cnt += 1
            else:
                # 4개 이상이면 삭제라 점수 추가
                if prv_cnt > 3:
                    answer += (prv_num * prv_cnt)
                # 3개 이하면 monsters에 추가
                else:
                    monsters += [prv_num] * prv_cnt
                # 바뀐 숫자므로 어쨌든 1로 초기화
                prv_cnt = 1
                prv_num = grid[row][col]

    return monsters


def pair_monster():
    result = []

    row, col = HALF, HALF
    dct = 2

    prv_num, prv_cnt = grid[row][col - 1], 0

    # 플레이어 왼쪽에 숫자가 있는 경우
    if prv_num:
        # 달팽이로 돌면서
        for limit in range(1, N):
            for _ in range(2):
                for _ in range(limit):
                    row += dr[dct]
                    col += dc[dct]

                    # 이전 숫자와 같으면 개수 추가
                    if prv_num == 0 and grid[row][col] == 0:
                        return result
                    if grid[row][col] == prv_num:
                        prv_cnt += 1
                    else:
                        result += [prv_cnt, prv_num]
                        prv_cnt = 1
                        prv_num = grid[row][col]
                dct = (dct - 1) % 4

    return result


def solution():
    for _ in range(M):
        d, p = map(int, input().split())
        # 플레이어는 상하좌우 방향 중 주어진 공격 칸 수만큼 몬스터를 공격하여 없앨 수 있습니다.
        attack(d, p)
        print_grid("공격")

        # 비어있는 공간만큼 몬스터는 앞으로 이동하여 빈 공간을 채웁니다.
        monsters = line_monster()

        # 이때 몬스터의 종류가 4번 이상 반복하여 나오면
        while fill_grid(monsters):
            print_grid("앞으로 땡김")
            # 해당 몬스터 또한 삭제됩니다. 해당 몬스터들은 동시에 사라집니다.
            monsters = kill_more_than_four()
            # 삭제된 이후에는 몬스터들을 앞으로 당겨주고, 4번 이상 나오는 몬스터가 있을 경우 또 삭제를 해줍니다.
        # 4번 이상 나오는 몬스터가 없을 때까지 반복해줍니다.
        print_grid("삭제가 끝남")
        # 삭제가 끝난 다음에는 몬스터를 차례대로 나열했을 때 같은 숫자끼리 짝을 지어줍니다.
        # 이후 각각의 짝을 (총 개수, 숫자의 크기)로 바꾸어서 다시 미로 속에 집어넣습니다.
        monsters = pair_monster()
        fill_grid(monsters)
        print_grid("짝지음")

    print(answer)

solution()