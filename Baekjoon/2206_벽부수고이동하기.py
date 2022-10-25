'''

bfs로 후다닥 풀어보자구!




1) 3차원 행렬로 풀 생각!

가장 기본적인 bfs 풀이지만, 단 한번 중간에 벽을 부술 수 있기에


벽 부수기 없이 visited[row][col]

벽 부수기가 있으면 visited[row][col][Boolean]

    => visited[row][col][True] 부순
    => visited[row][col][False] 안 부순


벽 파괴의 기회를 필사기 같이 갖고 있기!!


이거 내가 삼성 코테에서 실수 했었던...초기 입력 그거다...!





'''

from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))


from collections import deque

def bfs(i, j, wall):               # k는 벽 부수기 여부 (1:부숨)
    deq = deque()
    deq.append((i, j, wall))
    visited[i][j][wall] = 1        # 방문 체크

    while deq:
        i, j, wall = deq.popleft()

        if i == n-1 and j == m-1:
            return visited[i][j][wall]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][wall] == 0:      # 방문 안 했으면
                if mapp[ni][nj] == 0:                                           # 벽 없으면
                    visited[ni][nj][wall] = visited[i][j][wall] + 1             # 방문 체크
                    deq.append((ni, nj, wall))

                if mapp[ni][nj] == 1 and wall == 0:                          # 벽이 있고 안 부쉈으면
                    visited[ni][nj][1] = visited[i][j][wall] + 1             # 벽 부순 상태 방문 체크
                    deq.append((ni, nj, 1))

    return -1


n, m = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(n)]

di = [0, 1, 0, -1]  # 우하좌상 탐색
dj = [1, 0, -1, 0]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, 0))