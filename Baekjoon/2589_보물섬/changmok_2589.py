from collections import deque

def bfs(i, j):
    reach = [[-1] * c for _ in range(r)]
    furthest = 0
    q = deque([(i, j)])
    reach[i][j] = 0
    while q:
        nowr, nowc = q.popleft()
        for d in range(4):
            nexr = nowr + dr[d]
            nexc = nowc + dc[d]
            if not (0 <= nexr < r and 0 <= nexc < c) or area[nexr][nexc] != "L":
                continue
            if -1 < reach[nexr][nexc] <= reach[nowr][nowc] + 1:
                continue
            reach[nexr][nexc] = reach[nowr][nowc] + 1
            if reach[nexr][nexc] > furthest:
                furthest = reach[nexr][nexc]
            q.append((nexr, nexc))
    return furthest

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

r, c = map(int, input().split())
area = [input() for _ in range(r)]
land = []
for i in range(r):
    for j in range(c):
        if area[i][j] == "L":
            land.append((i, j))

answer = -1

for (i, j) in land:
    f = bfs(i, j)
    
    if f > answer:
        answer = f

print(answer)