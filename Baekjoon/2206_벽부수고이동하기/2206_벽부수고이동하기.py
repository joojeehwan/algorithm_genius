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


#벡터 배열 #상 하 좌 우

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col, wall = 0):
    q = deque()
    q.append((row, col, wall))
    visited[row][col] = 1


    while q:

        now_row, now_col, now_wall = q.popleft()

        # 원하는 도착 지점에 도착하면, bfs 종료
        if now_row == n-1 and now_col == m - 1 :
            return visited[row][col][wall]


        for dir in range(4):

            next_row = now_row + dr[dir]
            next_col = now_col + dc[dir]

            #범위 체크
            if 0 <= next_row < n and 0 <= next_col <m:

                #한번도 안 가본 곳 이면서, 벽이 없는 곳
                if not visited[next_row][next_col][wall] and MAP[next_row][next_col] == 0:
                    visited[next_row][next_col][wall] = visited[now_row][now_col] + 1
                    q.append((next_row, next_col, wall))

                # 한번도 안 가본 곳 이면서, 벽이 있는 곳
                if not visited[next_row][next_col][wall] and MAP[next_row][next_col] == 1:
                    visited[next_row][next_col][wall] = visited[now_row][now_col] + 1
                    q.append((next_row, next_col, 1))




#초기 입력받기
n, m = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(n)]

# 이 문제의 포인트..! 삼차원 배열로! 표시하기 // 배열의 값은 그떄까지의 최단 경로를 담기

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


