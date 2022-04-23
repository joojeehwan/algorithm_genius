import sys

dr = [0, 1, 1, 1, 0]
dc = [-1, -1, 0, 1, 1]

def kill(r, c):
    for d in range(5):
        nr, nc = r + dr[d], c + dc[d]
        while nr < n and 0 <= nc < n:
            board[nr][nc] += 1
            nr += dr[d]
            nc += dc[d]

def revive(r, c):
    for d in range(5):
        nr, nc = r + dr[d], c + dc[d]
        while nr < n and 0 <= nc < n:
            board[nr][nc] -= 1
            nr += dr[d]
            nc += dc[d]

def dfs(k):
    global cnt
    if k == n:
        cnt += 1
        return
    for i in range(n):
        if board[k][i] == 0:
            kill(k, i)
            dfs(k + 1)
            revive(k, i)


n = int(sys.stdin.readline())

board = [[0] * n for _ in range(n)]

cnt = 0

dfs(0)

print(cnt)