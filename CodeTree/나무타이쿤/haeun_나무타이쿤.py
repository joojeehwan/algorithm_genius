"""
43분
typing 쓰느라 나대고
영양제로 1 성장시키고 나서 대각선 탐지 멋대로 합쳐서 틀림
바보
"""
from typing import List

N, M = map(int, input().split())

# → ↗ ↑ ↖ ← ↙ ↓ ↘
dr: List[int] = [0, -1, -1, -1, 0, 1, 1, 1]
dc: List[int] = [1, 1, 0, -1, -1, -1, 0, 1]

tree: List[List[int]] = list(list(map(int, input().split())) for _ in range(N))
# 영양제를 [(x,y)] 로 관리하냐, [[true, true, false..]] 로 관리하냐?
nutri: List[List[int]] = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]


def in_range(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < N


def move(d: int, p: int) -> None:
    cnt = len(nutri)
    for i in range(cnt):
        new_row = (nutri[i][0] + dr[d] * p) % N
        new_col = (nutri[i][1] + dc[d] * p) % N
        nutri[i] = [new_row, new_col]


def grow() -> None:
    for r, c in nutri:
        tree[r][c] += 1

    for r, c in nutri:
        dia_tree = 0
        for d in range(1, 8, 2):
            n_row, n_col = r + dr[d], c + dc[d]
            if not in_range(n_row, n_col):
                continue
            if tree[n_row][n_col] > 0:
                dia_tree += 1

        tree[r][c] += dia_tree


def buy() -> List[List[int]]:
    bought: List[List[int]] = []
    old_nutri: List[List[bool]] = [[False] * N for _ in range(N)]

    # 영양제를 사용한 곳을 사용하지 않게 하고싶은데,
    # r, c in [nutri] 하면 시간 복잡도가 아까워서
    for r, c in nutri:
        old_nutri[r][c] = True

    for r in range(N):
        for c in range(N):
            if not old_nutri[r][c] and tree[r][c] >= 2:
                tree[r][c] -= 2
                bought.append([r, c])

    return bought


def count_tree() -> None:
    answer = 0

    for r in range(N):
        answer += sum(tree[r])

    print(answer)


def solution() -> None:
    global nutri

    for _ in range(M):
        d, p = map(int, input().split())
        # 특수 영양제를 이동 규칙에 따라 이동시킵니다.
        move(d-1, p)

        # 특수 영양제를 이동 시킨 후 해당 땅에 특수 영양제를 투입합니다.
        # 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장합니다.
        # 대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않습니다.
        grow()

        # 특수 영양제를 투입한 리브로수를 제외하고
        # 높이가 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고,
        # 해당 위치에 특수 영양제를 올려둡니다.
        nutri = buy()

    count_tree()


solution()