import sys

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 파편 던지는 방향 (↑, ↓, ←, →)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 소용돌이 순서 (아래 오른쪽 위 왼쪽)
mi = [1, 0, -1, 0]
mj = [0, 1, 0, -1]


# 소용돌이 순서를 먼저 인덱스로 만들어놓은 함수
def indexing():
    index_list = [(N // 2, N // 2 - 1)]
    beads_list = [MAP[N // 2][N // 2 - 1]]

    # 시작은 상어의 바로 왼쪽부터
    i = N // 2
    j = N // 2 - 1

    m = 0
    k = 1
    while i != -1 and j != -1:
        for _ in range(k):
            i += mi[m % 4]
            j += mj[m % 4]
            index_list.append((i, j))
            beads_list.append(MAP[i][j])
        m += 1
        if m % 2:
            k += 1

    index_list.pop(-1)
    beads_list.pop(-1)

    return index_list, beads_list


# 얼음파편을 던지는 함수
def throw(d, s):
    for k in range(1, s + 1):
        throw_i = N // 2 + di[d - 1] * k
        throw_j = N // 2 + dj[d - 1] * k
        if MAP[throw_i][throw_j]:
            MAP[throw_i][throw_j] = 0


# 구슬을 이동시키는 함수
def move():
    k = -1
    for i in range(len(indexing_list)):
        now_i, now_j = indexing_list[i]
        if not MAP[now_i][now_j]:  # MAP이 비어있다면 채워줘야함
            k += 1
            beads.pop(i - k)                    # beads 리스트에서 해당 구슬을 빼고 끝에 0을 넣어줌
            beads.append(0)


# 구슬이 폭발하는 단계
def bomb():
    flag = 1
    while flag:
        flag = 0
        for i in range(len(beads)):
            if not beads[i]:
                break
            num = beads[i]
            j = 1
            while i + j < len(beads) and beads[i + j] == num:
                j += 1
            if j >= 4:  # 연속으로 똑같은 게 4개 이상이면
                flag = 1
                bomb_beads[num] += j
                for k in range(j):
                    beads.pop(i)
                    beads.append(0)


# 구슬이 변화하는 단계
def change_beads():

    # 새로운 2차원 배열에 만들어줌
    new_MAP = [[0] * N for _ in range(N)]
    new_beads_list = []
    i = 0
    k = 0
    while i < len(beads):
        if not beads[i]:
            break
        if k >= len(indexing_list):
            break

        num = beads[i]
        j = 1

        while i + j < len(beads) and beads[i + j] == num:
            j += 1

        new_MAP[indexing_list[k][0]][indexing_list[k][1]] = j
        new_MAP[indexing_list[k + 1][0]][indexing_list[k + 1][1]] = num
        new_beads_list.append(j)
        new_beads_list.append(num)
        k += 2
        i += j

    new_beads_list += [0] * (N * N - 1 - len(new_beads_list))

    return new_MAP, new_beads_list


bomb_beads = [0, 0, 0, 0]
indexing_list, beads = indexing()
beads_cnt = []

for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())

    # 파편을 던지고 이동시키고
    throw(d, s)
    move()

    # 터트리고
    bomb()
    MAP, beads = change_beads()

print(bomb_beads[1] + 2 * bomb_beads[2] + 3 * bomb_beads[3])
