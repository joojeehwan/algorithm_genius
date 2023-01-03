import sys

# 1.  dfs 풀이
print(ord("A"))
input = sys.stdin.readline

r, c = map(int, input().split())

MAP = [input().rstrip() for _ in range(r)]

check = [False] * 256

ans = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col, cnt):
    global ans

    ans = max(ans, cnt)

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]

        # 이동 후 범위체크 국룰
        if 0 <= next_row < r and 0 <= next_col < c and not check[next_row][next_col]:

            asc = ord(MAP[next_row][next_col])

            # 이전에 없던 알파벳
            if check[asc]:
                continue

            check[asc] = True
            dfs(next_row, next_col, cnt + 1)
            check[asc] = False


# 초기 세팅
check[ord(MAP[0][0])] = True
dfs(0, 0, 1)
print(ans)

# 2. SET을 활용한 풀이


# 2 - 1 dfs 다른 풀이
# 전체 4방향 돌기전애, visited 배열 건드릴 수 있음.

r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]
visited = set()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0


def dfs(row, col, cnt):
    global ans
    ans = max(ans, cnt)
    visited.add(MAP[row][col])

    for i in range(4):

        next_row = row + dr[i]
        next_col = col + dc[i]

        if 0 <= next_row < r and 0 <= next_col < c :
            if MAP[next_row][next_col] not in visited:
                dfs(next_row, next_col, cnt + 1)

    visited.remove(MAP[row][col])


dfs(0, 0, 1)

print(ans)

# 2 - 2 bfs 풀이

r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]
visited = set()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 1


def bfs(row, col):
    global answer
    q = set([(row, col, MAP[row][col])])

    while q:

        next_row, next_col, ans = q.pop()

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if 0 <= next_row < r and 0 <= next_col < c and MAP[next_row][next_col] not in ans:
                q.add((next_row, next_col, ans + MAP[next_row][next_col]))
                answer = max(answer, len(ans) + 1)


bfs(0, 0)
print(answer)