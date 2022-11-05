'''

벽 부수고 이동하기 2


1번과의 차이?!

1번은 1개의 벽만 부술 수 있었지만!
2번은 k번 까지 부술 수 있다.



'''


# from collections import deque
# q = deque()
# from sys import stdin
# input = stdin.readline
#
# n,m,k = map(int, input().split())
# vis = [[[0]*(k+1) for _ in range(m)] for __ in range(n)]
# arr = [list(map(int,input().strip())) for _ in range(n)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# def bfs() :
#     q.append([0,0,k]) # k는 벽을 뚫을 수 있는 수
#     vis[0][0][k] = 1
#     while q :
#         x,y,z = q.popleft()
#         if x == n-1 and y == m-1 :
#             return vis[x][y][z]
#         for i in range(4) :
#             nx ,ny = dx[i] + x, dy[i]+y
#             if 0<=nx<n and 0<=ny<m :
#                 if arr[nx][ny]==1 and z>0 and vis[nx][ny][z-1]==0:
#                     vis[nx][ny][z-1] = vis[x][y][z]+1
#                     q.append([nx,ny,z-1])
#                 elif arr[nx][ny]==0 and vis[nx][ny][z]==0:
#                     vis[nx][ny][z] = vis[x][y][z]+1
#                     q.append([nx,ny,z])
#     return -1
#
# print(bfs())

#방1
from collections import deque
import sys


input = sys.stdin.readline


N, M, K = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

#초기 시작 문제에서 주어짐
visited[0][0][K] = 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():

    q = deque()
    q.append((0, 0, K))

    while q:
        row, col, power = q.popleft()

        if row == N-1 and col == M - 1 :
            return visited[row][col][power]

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if 0 <= next_row < N and 0 <= next_col < M :

                if MAP[next_row][next_col] == 0 and visited[next_row][next_col][power] == 0:

                    q.append((next_row, next_col, power))
                    visited[next_row][next_col][power] = visited[row][col][power] + 1
                #내가 벽을 뚫고 갈곳을 가봈었는지 체크
                elif MAP[next_row][next_col] == 1 and visited[next_row][next_col][power - 1] == 0 and power > 0:
                    q.append((row, col, power - 1))
                    visited[next_row][next_col][power] = visited[row][col][power] + 1

    return -1


print(bfs())


#빙2
from collections import deque
import sys
N, M, K = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a = []
for _ in range(N):
    a.append(list(map(int, list(sys.stdin.readline().rstrip()))))
q = deque()
q.append((0, 0, 0))
d = [[[0]*11 for _ in range(1000)] for _ in range(1000)]
d[0][0][0] = 1
while q:
    x, y, z = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if a[nx][ny]==0 and d[nx][ny][z]==0:
            d[nx][ny][z] = d[x][y][z] + 1
            q.append((nx, ny, z))
        elif z+1<=K and a[nx][ny]==1 and d[nx][ny][z+1]==0:
            d[nx][ny][z+1] = d[x][y][z] + 1
            q.append((nx, ny, z+1))
ans = -1
for i in range(K+1):
    if d[N-1][M-1][i]==0:
        continue
    if ans==-1 or ans>d[N-1][M-1][i]:
        ans = d[N-1][M-1][i]
print(ans)



# 방3
import sys
from collections import deque
input = sys.stdin.readline

dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # delta (dx, dy) order

def solve(g, N, M, K):
    visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append((0, 0, 0))         # (y, x, crushed count) order
    visited[0][0][0] = 1

    while q:
        y, x, crushed = q.popleft()

        if y == (N-1) and x == (M-1):
            return visited[y][x][crushed]

        for dx, dy in dt:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if g[ny][nx] == 0 and visited[ny][nx][crushed] == 0:
                    visited[ny][nx][crushed] = visited[y][x][crushed] + 1
                    q.append((ny, nx, crushed))
                elif g[ny][nx] == 1 and crushed < K and visited[ny][nx][crushed+1] == 0:
                    visited[ny][nx][crushed+1] = visited[y][x][crushed] + 1
                    q.append((ny, nx, crushed+1))

    return -1


# main logic
N, M, K = map(int, input().strip().split())

g = []
for _ in range(N):
    l = list(map(int, input().strip()))
    g.append(l)

ans = solve(g, N, M, K)
print(ans)





# 방 4
import sys
n, m, k  = tuple(map(int, input().split()))
a = [
  list(map(int, list(sys.stdin.readline().rstrip())))
  for _ in range(n)
]

visited = [
  [[0] * (k + 1)
  for _ in range(m)]
  for _ in range(n)
]
from collections import deque


def inRange(x, y):
  return 0 <= x < n and 0 <= y < m

def bfs():
  q = deque()
  q.append((0,0,0))
  visited[0][0][0] = 1

  dxs, dys = [1, -1, 0, 0, ], [0, 0, 1, -1]
  while q:
    x, y, crashCnt = q.popleft()

    if x == n-1 and y == m-1:
      print(visited[x][y][crashCnt])
      exit(0)


    for i in range(4):
      nx, ny = x+dxs[i], y + dys[i]

      if inRange(nx, ny) :

        if a[nx][ny] == 0 and visited[nx][ny][crashCnt] == 0: # 벽이 아닌 경우
          visited[nx][ny][crashCnt] = visited[x][y][crashCnt] + 1
          q.append((nx, ny, crashCnt))

        elif a[nx][ny] == 1 and crashCnt < k and visited[nx][ny][crashCnt+1] == 0:
            nextCrashCnt = crashCnt + 1
            visited[nx][ny][nextCrashCnt] = visited[x][y][crashCnt] + 1

            q.append((nx, ny, nextCrashCnt))


  print(-1)


bfs()


