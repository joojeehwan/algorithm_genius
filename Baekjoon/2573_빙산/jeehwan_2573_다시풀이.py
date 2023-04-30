'''

문제 해결 전략

1. 격자에서 빙산이 위치하는 곳은 1차원 배열에 기록

2. bfs

    1. bfs시작하자마, 덩어리 갯수 체크

    2. 인접한 곳에 바다가 있는지 체크, 이를 관리할 변수(cnt)필요

    3. 인접한 곳에 방문한 이후에, 인접한 곳에 있는 같은 덩어리 소속 next_row, next_col q에 추가

    4. q가 다 돌아, 한 싸이클이 돈 이후에, 2번에서 체크한 cnt와 row, col을 기록배열에 추가

    5. 하나의 덩어리 사이클(q)가 돈 이후에, 이중 for문을 활용해 빙산의 높이 줄이기.

    6. ****이 문제의 포인트****

        주위의 바다로 인해, 0이 되어버린 빙산을 artic 배열에서 삭제 why?!

        artic배열을 이용해, q에 append하고 visted 배열을 관리.

        전체 사이클을 다 돌고도, 빙산이 존재하는 경우 그 다음 bfs에서 빠지면 안되고,

        전체 사이클을 다 돈 이후에, 빙산이 다 녹아 0이 되는 경우는 그 다음 bfs에서 제외 되어야 함.

        2개 이상의 덩어리가 생기는 것을 알기 위해서,

        만약에 1개의 덩이리의 경우, searh_iceburg의 값과 len(artic)의 값이 항상 같아 진다.

3. 전체 시물레이션

    - len(artic)과 bfs의 결과 비교

    > 덩어리가 1개인 경우는 artic의 전체 갯수와, bfs의 결과가 항상 같을 것,
    2개이상이 되는 경우부터 달라짐.


    - MAP에 빙하가 없는데에도 불구하고, (전체 다 같이 없어지는 경우) 덩어리가 2개 이상 되지 못한 경우 예외처리


입력
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

'''

from collections import deque

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

# 빙산의 위치를 기록
artic = []

# 정답
ans = 0

for row in range(N):

    for col in range(M):

        if MAP[row][col] != 0:
            artic.append((row, col))

# 델타배열 => 4방향 탐색, 상 하 좌 우

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque()
    # artic 배열의 값을 조절해, bfs가 적절하게 반복되어 질 수 있도록 함.
    q.append(artic[0][0], artic[0][1])
    visited = [[False] * m for _ in range(N)]
    visited[artic[0][0]][artic[0][1]] = True

    # 현재 덩어리에서 탐색한 빙산의 갯수
    cnt_iceberg = 0
    # 주위에 바다가 있어, 높이가 줄어들여할 빙산의 row, col 저장
    cut_iceberg = []

    while q:

        # 빙산 갯수 추가
        cnt_iceberg += 1
        now_row, now_col = q.popleft()
        cnt = 0

        # 4방향 탐색 주위 바다의 갯수 / 같은 덩어리의 빙산 check
        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            # 이동후 범위 체크

            if 0 <= next_row < N and 0 <= next_col < M:

                # 주위 바다 체크
                if MAP[next_row][next_col] == 0:
                    cnt += 1

                # 다음
                elif MAP[next_row][next_col] != 0 and not visited[next_row][next_col]:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True

        # 4방향을 다 돈 이후에, 해당 row, col 인접한 곳에 바다 있었다면?!
        # cut_iceberg에 기록하기
        if cnt != 0:
            cut_iceberg.append((row, col, cnt))

    # while문이 종료된 이후에, for문을 통해 빙산의 크기 줄이기
    # 0이하로는 가지 않아!
    for i, j, cnt in cut_iceberg:

        if MAP[i][j] - cnt <= 0:
            MAP[i][j] = 0

        else:
            MAP[i][j] -= cnt

        if MAP[i][j] == 0 and (i, j) in artic:
            artic.remove((i, j))

    return cnt_iceberg


while True:

    if len(artic) != bfs():
        break

    ans += 1

    # 빙하가 다 녹았는데도, 덩어리가 2개 이상이 안되는 경우

    temp = 0
    for row in range(N):
        temp += sum(MAP[row])

    if temp == 0:
        ans = 0
        break

print(ans)