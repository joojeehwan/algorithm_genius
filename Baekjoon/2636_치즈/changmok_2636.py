import sys
from collections import deque

# 네 귀퉁이에서부터 bfs로 갉아먹어 들어오는 방식
# 이 문제만의 특징
# 치즈가 갉아먹히는 다음 스텝은 nq에 저장해두고 q가 비어서 nq로 갈아끼우는 횟수를 센다는 것

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
seen = [[0] * m for _ in range(n)]
seen[0][0] = 1
seen[0][m-1] = 1
seen[n-1][0] = 1
seen[n-1][m-1] = 1

# while 문의 특성상 nq에 첫 네 귀퉁이 저장
nq = deque([(0, 0, 0), (0, m-1, 0), (n-1, 0, 0), (n-1, m-1, 0)])

# 이제 bfs는 이 q로 봄
q = deque()
phase = 0

while nq:
    lastql = len(nq)
    q, nq = nq, q
    phase += 1
    while q:
        r, c, p = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not seen[nr][nc]:
                if board[nr][nc] == 0:
                    q.append((nr, nc, p))
                    seen[nr][nc] = 1
                else:
                    nq.append((nr, nc, p + 1))
                    seen[nr][nc] = 1

print(phase - 1)
print(lastql)