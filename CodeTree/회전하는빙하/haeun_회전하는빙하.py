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

# 필요 변수 (빙하 회전을 위해 우하좌상으로 만든다)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
length = 2 ** N
rotated = [[0] * length for _ in range(length)]    # 원래 격자 만큼의 임시 배열을 만든다. 회전하면서 여기다 옮겨줌


def print_ice(message):
    print(message)
    for line in ice:
        print(*line)
    print()


# 2^l 크기의 격자를 선택해서 들어왔다.
# 2^(l-1) 크기로 4등분된 빙하를 한 덩이씩 보면서 회전하는 함수
# d(방향) 에 맞춰 옮겨준다.
def rotating(sr, sc, half, d):
    for r in range(sr, sr+half):
        for c in range(sc, sc+half):
            nr = r + dr[d] * half
            nc = c + dc[d] * half
            rotated[nr][nc] = ice[r][c]


# 빙하를 선택하는 함수
# 2^N * 2^N의 빙하를 2^l * 2^l 만큼씩 선택한다.
# 그 안에서 2^(l-1) * 2^(l-1) 만큼씩 반시계 90'로 회전한다.
def iceberg_rotate(level):
    if level == 0:
        return
    l_len = 2 ** level
    h_len = l_len // 2

    # 4등분으로 반시계 방향으로 90' 회전하지만, 꼭 회전공식을 사용하지 않아도 된다.
    # 좌상, 우상, 우하, 좌하 격자 순대로 우 -> 하 -> 좌 -> 상의 방향으로 격자를 옮기는 것과 같은 행위다.
    # 이 생각을 떠올리긴 했지만, 4경우 모두 하나의 for 반복문 내에서 처리하려고 한 점이 더 돌아가게 만들었다.
    for start_r in range(0, length, l_len):
        for start_c in range(0, length, l_len):
            rotating(start_r, start_c, h_len, 0)
            rotating(start_r, start_c + h_len, h_len, 1)
            rotating(start_r+h_len, start_c+h_len, h_len, 2)
            rotating(start_r+h_len, start_c, h_len, 3)

    # 회전 사항 반영
    for r in range(length):
        ice[r] = rotated[r][:]
        rotated[r] = [0] * length


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