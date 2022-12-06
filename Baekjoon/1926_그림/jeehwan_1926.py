


from collections import deque

n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

maxValue = 0
def bfs(row, col):

    global maxValue
    q = deque()
    q.append((row, col))
    visited[row][col] = 1
    temp = 1

    while q :

        now_row, now_col = q.popleft()

        for k in range(4):
            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            if 0 <= next_row < n and 0 <= next_col < m:
                if MAP[next_row][next_col] == 1 and visited[next_row][next_col] == 0:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    temp += 1

    if temp > maxValue :
        maxValue = temp




cnt = 0
for row in range(n):
    for col in range(m):
        if MAP[row][col] == 1 and visited[row][col] == 0 :
            bfs(row, col)
            cnt += 1

print(cnt)
print(maxValue)



