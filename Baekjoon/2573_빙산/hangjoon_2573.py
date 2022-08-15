from collections import deque
import sys


# BFS
def bfs(r, c, row, col):
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        now_r, now_c = queue.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r, new_c = now_r + dr, now_c + dc
            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:  # 맵 밖임
                continue
            if visited[new_r][new_c]:  # 이미 방문함
                continue
            if not field[new_r][new_c]:  # 바다임
                cnt_lst[now_r][now_c] += 1
            else:  # 빙산임
                queue.append((new_r, new_c))
                visited[new_r][new_c] = 1
    # 이 빙산 덩어리 끝
    return 1


# 입력
row, col = map(int, sys.stdin.readline().split())  # 맵의 세로, 가로 크기
field = [[] for _ in range(row)]
for r in range(row):
    field[r] = list(map(int, sys.stdin.readline().split()))

ans = 0
while True:  # 빙산이 분리될 때까지
    visited = [[0] * col for _ in range(row)]  # 방문 목록
    ice = 0  # 빙산 수
    cnt_lst = [[0] * col for _ in range(row)]  # 바다와 닿은 수 카운트

    # 녹는 빙산 세기 (BFS)
    queue = deque()
    for r in range(1, row - 1):
        for c in range(1, col - 1):
            if field[r][c] and not visited[r][c]:  # 빙산이 있으면
                ice += bfs(r, c, row, col)

    # 빙산 녹이기
    for r in range(row):
        for c in range(col):
            field[r][c] = max(0, field[r][c] - cnt_lst[r][c])

    # 종료조건 확인하기
    if ice == 0:
        ans = 0
        break
    elif ice >= 2:
        break
    ans += 1  # 1년 추가

print(ans)