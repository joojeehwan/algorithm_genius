from collections import deque

n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
paper = list(list(map(int, input().split())) for _ in range(n))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

drawing_cnt, max_width = 0, 0

for r in range(n):
    for c in range(m):
        if paper[r][c] == 0:
            continue
        if not visited[r][c]:
            visited[r][c] = 1
            drawing_cnt += 1
            width = 1

            q = deque([(r, c)])

            while q:
                now_r, now_c = q.popleft()

                for d in range(4):
                    new_r, new_c = now_r + dr[d], now_c + dc[d]
                    if not (0 <= new_r < n and 0 <= new_c < m):
                        continue
                    if visited[new_r][new_c]:
                        continue
                    visited[new_r][new_c] = 1
                    if not paper[new_r][new_c]:
                        continue
                    q.append((new_r, new_c))
                    width += 1

            max_width = max(width, max_width)

print(drawing_cnt)
print(max_width)
