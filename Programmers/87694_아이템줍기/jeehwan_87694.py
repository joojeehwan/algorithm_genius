from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    MAXNUM = 101
    MAP = [[0 for _ in range(MAXNUM)] for _ in range(MAXNUM)]

    # print(MAP)

    # 1
    # 사각형 1로 채우기 (테두리 + 내부)
    # 곱하기 2배를 해야 테스트 케이스 오류가 안난다.

    # 렉탱글에서 값 하나씩 뽑고 for, 그 뽑은 값에 대해서 사각형 채우기! 이중포문
    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1, 2 * r2 + 1):  # 요.i의 길이 만큼
            for j in range(2 * c1, 2 * c2 + 1):  # 요 j의 길이 만큼
                MAP[i][j] = 1

    # 2
    # 사각형 안에를 0으로 채우기! 바깥에는 이제 1로 채워진다!
    # 시작에 +1을 하고 마지막에서 -1을 해서! 그렇게 만든다!
    # *2를 하는것은 반례 테스트케이스를 없앨려고!

    for c1, r1, c2, r2 in rectangle:
        for i in range(2 * r1 + 1, 2 * r2):
            for j in range(2 * c1 + 1, 2 * c2):
                MAP[i][j] = 0

    # 3
    visited = [[0] * 101 for i in range(101)]
    chrr, chc, itr, itc = 2 * characterY, 2 * characterX, 2 * itemY, 2 * itemX

    q = deque()
    q.append([chrr, chc])
    cnt = 0
    while q:

        chrr, chc = q.popleft()
        if (chrr, chc) == (itr, itc):
            cnt = (MAP[chrr][chc] - 1) // 2
            break

        for i in range(4):
            next_chrr = chrr + dr[i]
            next_chc = chc + dc[i]

            if 0 <= next_chrr < 101 and 0 <= next_chc < 101 and MAP[next_chrr][next_chc] != 0 and visited[next_chrr][
                next_chc] == 0:
                MAP[next_chrr][next_chc] = MAP[chrr][chc] + 1
                visited[next_chrr][next_chc] = 1
                q.append((next_chrr, next_chc))

    return cnt