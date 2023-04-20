'''


["X591X","X1X5X","X231X", "1XXX1"]   res : [1, 1, 27]

["XXX","XXX","XXX"]                  res : [-1]

'''



from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs(row, col, visited, maps, N, M) :

    cnt = int(maps[row][col])
    q = deque()
    q.append((row, col))
    visited[row][col] = True

    while q:

        now_row, now_col = q.popleft()

        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if 0 <= next_row < M and 0 <= next_col < N :

                if maps[next_row][next_col] != 'X' and not visited[next_row][next_col]:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    cnt += int(maps[next_row][next_col])

    return cnt

def solution(maps):

    answer = []
    N = len(maps[0])
    M = len(maps)
    visited = [[False] * N for _ in range(M)]

    for row in range(M) :
        for col in range(N) :
            if maps[row][col] != 'X' and not visited[row][col]:
                temp = bfs(row, col, visited, maps, N, M)
                answer.append(temp)

    answer.sort()

    if answer == []:
        return [-1]
    return answer



print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))


# dfs 풀이


7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
def solution(maps):
    import sys
    sys.setrecursionlimit(int(1e9))

    graph = [list(row) for row in maps]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    ans = []

    def dfs(x, y):
        cnt = 0
        if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
            return cnt
        if not graph[x][y].isdigit():
            return cnt
        cnt = int(graph[x][y])
        graph[x][y] = 'X'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt += dfs(nx, ny)
        return cnt

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j].isdigit():
                ans.append(dfs(i,j))

    return sorted(ans) if len(ans) != 0 else [-1]
