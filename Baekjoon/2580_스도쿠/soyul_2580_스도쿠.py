import sys

MAP = [list(map(int, input().split())) for _ in range(9)]

# 스도쿠의 모든 조건을 만족하는지 확인
def possible(now_i, now_j):

    # 가로 확인
    # MAP안의 숫자를 인덱스로 검사
    check = [0] * 9
    for k in range(9):
        if MAP[now_i][k] == 0:
            continue
        if check[MAP[now_i][k] - 1]:
            return 0
        check[MAP[now_i][k] - 1] = 1

    # 세로 확인
    check = [0] * 9
    for k in range(9):
        if MAP[k][now_j] == 0:
            continue
        if check[MAP[k][now_j]-1]:
            return 0
        check[MAP[k][now_j]-1] = 1

    # 칸 확인
    check = [0] * 9

    p = now_i // 3
    q = now_j // 3
    for i in range(3 * p, 3 * (p + 1)):
        for j in range(3 * q, 3 * (q + 1)):
            if MAP[i][j] == 0:
                continue
            if check[MAP[i][j]-1]:
                return 0
            check[MAP[i][j]-1] = 1

    return 1


def dfs(now):
    global result

    if result:
        return

    if now >= len(lst):
        result = 1
        for i in range(9):
            print(" ".join(map(str, MAP[i])))
        return

    for i in range(now, len(lst)):
        next_i, next_j = lst[i]

        if MAP[next_i][next_j]:                 # 채워져 있으면
            continue

        flag = 0                                # flag
        for k in range(1, 10):
            MAP[next_i][next_j] = k
            if possible(next_i, next_j):
                flag = 1
                dfs(now + 1)
                flag = 0
        if not flag:
            MAP[next_i][next_j] = 0
            return


lst = []
result = 0
# 채워야 하는 빈칸이 생기면
for i in range(9):
    for j in range(9):
        if MAP[i][j] == 0:
            lst.append((i, j))

dfs(0)
