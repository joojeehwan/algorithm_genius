"""
- 어려운 점 : 빙하를 레벨에 따라 다르게 회전시켜야한다.
- 해결 방법 : 시작점과 길이를 계속 반영
- 풀이 시간 : 1시간 51분... ㅠㅠㅠㅠ
"""
from collections import deque

# 입력 처리
N, Q = map(int, input().split())
ice = list(list(map(int, input().split())) for _ in range(2**N))
levels = list(map(int, input().split()))  # python이라 딱히 Q 필요 없음

# 필요 변수
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
length = 2 ** N
rotated = [[0] * length for _ in range(length)]


def print_ice(message):
    print(message)
    for line in ice:
        print(*line)
    print()


# 4등분된 빙하를 한 덩이씩 보면서 회전하는 함수
def rotating(sr, sc, l):

    l_len = 2 ** l  # level의 길이
    s_len = 2 ** (l-1)  # level-1의 길이
    temp = [[0] * l_len for _ in range(l_len)]

    for r in range(0, l_len, s_len):
        for c in range(0, l_len, s_len):
            for _r in range(s_len):
                for _c in range(s_len):
                    temp[c+_r][s_len-r+_c] = ice[sr+r+_r][sc+c+_c]

    for r in range(l_len):
        for c in range(l_len):
            rotated[sr+r][sc+c] = temp[r][c]


# 빙하를 선택하는 함수
# 2^N * 2^N의 빙하를 2^l * 2^l 만큼씩 선택한다.
# 그 안에서 2^(l-1) * 2^(l-1) 만큼씩 반시계 90'로 회전한다.
def iceberg_rotate(level):
    if level == 0:
        return
    global rotated
    # 원래 격자 만큼의 임시 배열을 만든다. 회전하면서 여기다 옮겨줌
    rotated = [[0] * length for _ in range(length)]

    for start_r in range(0, length, 2 ** level):
        for start_c in range(0, length, 2 ** level):
            rotating(start_r, start_c, level)

    # 회전 사항 반영
    for r in range(length):
        ice[r] = rotated[r][:]


# 빙하가 녹는 함수
def iceberg_melt():
    melted = [[0] * length for _ in range(length)]
    for r in range(length):
        for c in range(length):
            if ice[r][c] == 0:
                continue
            cnt = 0
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < length and 0 <= nc < length and ice[nr][nc]:
                    cnt += 1

            if cnt < 3:
                melted[r][c] = -1

    for r in range(length):
        for c in range(length):
            ice[r][c] += melted[r][c]


def calculate():
    total = 0
    max_cnt = 0
    visited = [[0] * length for _ in range(length)]

    for r in range(length):
        for c in range(length):
            if ice[r][c] and not visited[r][c]:
                cnt = 1
                visited[r][c] = 1
                q = deque([(r, c)])

                while q:
                    now_r, now_c = q.popleft()
                    total += ice[now_r][now_c]

                    for d in range(4):
                        next_r, next_c = now_r + dr[d], now_c + dc[d]
                        if 0 <= next_r < length and 0 <= next_c < length and not visited[next_r][next_c] and ice[next_r][next_c]:
                            visited[next_r][next_c] = 1
                            cnt += 1
                            q.append((next_r, next_c))

                max_cnt = max(max_cnt, cnt)

    return total, max_cnt


def solution():
    # 꼭 빙하 순서대로
    for level in levels:
        # level에 맞춰 빙하 회전
        iceberg_rotate(level)
        # print_ice("!!!!!!!!!! 회전했다아아아아")
        iceberg_melt()
        # print_ice("~~~~~~~~~~~ 녹였다아아아아아")
    # 다 돌았으면 정답 찾기
    total, max_cnt = calculate()
    print(total)
    print(max_cnt)


solution()