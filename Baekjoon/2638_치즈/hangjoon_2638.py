from collections import deque
import sys


def bfs(lst, rowNum, colNum):
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * colNum for _ in range(rowNum)]  # 빈 영역 방문 정보
    visited[0][0] = 1
    while queue:
        now_r, now_c = queue.popleft()
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:  # 북서남동
            new_r = now_r + dr
            new_c = now_c + dc
            if new_r < 0 or new_r >= rowNum or new_c < 0 or new_c >= colNum:
                continue  # 맵 바깥
            if visited[new_r][new_c]:
                continue  # 이미 탐색함
            if field[new_r][new_c] >= 1:  # 치즈가 얼마나 공기와 닿았는지
                lst[new_r][new_c] += 1
            else:  # 빈 영역
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c))
    return


row, col = map(int, sys.stdin.readline().split())  # 모눈 종이의 세로, 가로 크기
field = [[] for _ in range(row)]  # 모눈 종이 정보
for i in range(row):
    field[i] = list(map(int, sys.stdin.readline().split()))
ans = 0

"""
[New]
1. (0, 0)부터 시작하면 내부에 격리된 공기와 만나기 전에 치즈와 먼저 만나게 됨
2. 따라서, (0, 0) 부터 방문 정보를 기록하면서 방문한 공기(두 영역 이상)와 치즈가 만날 때 녹는다고 판별
3. 공기를 만나면 방문을 기록, 치즈를 만나면 공기와 만난 횟수를 기록(카운트)
4. 치즈와 만났을 때 queue에 넣지 않으면 그 안쪽의 공기를 기록할 일은 없음
"""

flag = 1
while flag:
    flag = 0
    bfs(field, row, col)
    for r in range(1, row - 1):
        for c in range(1, col - 1):
            if field[r][c] >= 3:  # 두 영역 이상 공기와 닿은 치즈
                field[r][c] = 0  # 녹음
                flag = 1
            elif field[r][c] == 2:  # 한 영역과만 닿은 치즈
                field[r][c] = 1  # 녹지 않음
    if flag:
        ans += 1

print(ans)