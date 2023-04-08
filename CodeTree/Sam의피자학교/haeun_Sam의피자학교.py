"""
이 문제의 까다로운 점은 2차원 배열이 행마다 열의 수가 다르다는 점이다.
- 시간 : 1시간 58분 (한번에 맞췄어.. 대박)
"""
# import sys
# sys.stdin = open('input.txt', "r")


N, K = map(int, input().split())
dough = [list(map(int, input().split()))]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def print_dough():
    for line in dough:
        print(*line)


# 1. 밀가루 양이 가장 적은 곳에 1 추가
# - 가장 적은 곳이 여러군데면 다 추가한다.
def fill_flour():
    minimum = min(dough[0])
    for i in range(N):
        if dough[0][i] == minimum:
            dough[0][i] += 1


# +) 시계 90도 회전하기.
# - 회전한 배열을 반환한다.
# - (r, c) -> (c, R-r)
def rotate_clock(dou):
    R = len(dou)
    C = len(dou[0])

    rotated = [[0] * R for _ in range(C)]

    for r in range(R):
        for c in range(C):
            rotated[c][R-r-1] = dou[r][c]

    return rotated


# 2. 도우를 말아준다 (극혐파트)
def roll_dough():
    global dough
    # - 맨 밑바닥이 그 위보다 짧기 전에 중단한다.
    # - 우선 한개 뜯어낸다.
    one = [dough[0].pop(0)]
    dough.append(one)

    # 루프를 돈다. 밑이 짧아지고나서 종료하면 안된다. 짧아지기 직전에 종료해야한다.
    while True:
        # - 최상단 행의 열의 길이만큼 밑에서부터(0->top) 뜯어낸다.
        piece = []  # 회전할 덩어리
        top_row = len(dough)  # 최상단 행
        top_len = len(dough[top_row-1])  # 최상단 행의 열의 길이

        for r in range(top_row-1, -1, -1):
            line = []
            for _ in range(top_len):
                line.append(dough[r].pop(0))
            if len(dough[r]) == 0:  # 비어버린 배열은 빼줘야한다...
                dough.pop(r)
            piece.append(line)

        # - 시계 90도 회전한다.
        piece = rotate_clock(piece)
        # - 회전한걸 거꾸로 한줄씩 붙인다.
        for r in range(len(piece)-1, -1, -1):
            dough.append(piece[r])

        # 다음 연산에 밑에 줄이 짧아질 것 같으면 멈춰야한다.
        top_row = len(dough)  # 최상단 행
        top_len = len(dough[top_row - 1])  # 최상단 행의 열의 길이
        if len(dough) > len(dough[0])-top_len:
            break


# 3. 도우를 누른다.
def flatten():
    global dough
    dough_rows = len(dough)  # 도우의 행 개수
    visited = []  # 방문 확인용 2차원 배열(같은 크기) 필요
    diff = []  # 차이를 저장(동시진행)할 2차원 배열(같은 크기) 필요
    for r in range(dough_rows):
        visited.append([0] * len(dough[r]))
        diff.append([0] * len(dough[r]))


    # r -> c로 보면서 (c의 길이가 r마다 다르다는걸 잊지말자)
    for r in range(dough_rows):
        col = len(dough[r])
        for c in range(col):
            now = dough[r][c]

            for d in range(4):
                n_r, n_c = r + dr[d], c + dc[d]
                if 0 <= n_r < dough_rows and 0 <= n_c < col:
                    if n_r == r+1 and n_c >= len(dough[r+1]):  # 아래인데 밑에 행의 열의 길이보다 길다면 ㅂㅂ
                        continue
                    if visited[n_r][n_c]:
                        continue
                    nxt = dough[n_r][n_c]

                    # 인접한 곳과 abs(a-b)/5 = d이고, 큰 쪽에는 -d, 작은 쪽에는 +d를 차이 배열에 저장한다.
                    difference = abs(now - nxt) // 5
                    if nxt > now:
                        diff[n_r][n_c] -= difference
                        diff[r][c] += difference
                    elif nxt < now:
                        diff[n_r][n_c] += difference
                        diff[r][c] -= difference
            # 4방향 다 본 애는 체크해서 그만본다.
            visited[r][c] = 1


    # 다 돌았으면 차이를 반영한다.
    # r -> c로 보면서 (c의 길이가 r마다 다르다는걸 잊지말자)
    for r in range(dough_rows):
        col = len(dough[r])
        for c in range(col):
            dough[r][c] += diff[r][c]

    # 0번째 행의 열의 길이만큼을 길이로 하는 2차원 배열을 만든다.
    flat = [[] for _ in range(len(dough[0]))]
    # 행을 돌면서 각 열의 idx에 맞춰 추가한다.
    for r in range(dough_rows):
        for c in range(len(dough[r])):
            flat[c].append(dough[r][c])

    # 이제 0부터 돌면서 일차원 배열에 추가한다.
    flatted = []
    for line in flat:
        flatted += line

    # 그게 도우가 된다.
    dough = [flatted[:]]


# 4. 도우를 2번 반 접는다.
def double_fold():
    global dough
    # 2번 반복한다.
    for _ in range(2):
        bottom = []  # - 자른걸 저장할 새 배열이 필요하다.
        top = []  # - 회전할걸 저장할 새 배열이 필요하다.

        # - 1. 행을 돌며, 앞의 반은 회전용, 뒤의 반은 temp 추가한다.
        half = len(dough[0]) // 2
        dough_rows = len(dough)
        for r in range(dough_rows):
            top.append(dough[r][:half])
            bottom.append(dough[r][half:])

        # - 2. 다 돌았으면, rotated를 90도 함수에 2번 돌린다.
        for _ in range(2):
            top = rotate_clock(top)

        dough = []
        # bottom 먼저
        for line in bottom:
            dough.append(line)

        for line in top:
            dough.append(line)


def solution():
    answer = 0
    while max(dough[0])-min(dough[0]) > K:
        # print(" >> 1 << 밀가루 채우기!")
        fill_flour()
        # print(" >> 2 << 도우 말아주기!")
        roll_dough()
        # print(" >> 3 << 도우 눌러주기!")
        flatten()
        # print(" >> 4 << 도우 2번 접기!")
        double_fold()
        # print(" >> 5(3) << 도우 눌러주기!")
        flatten()
        answer += 1
    print(answer)

solution()