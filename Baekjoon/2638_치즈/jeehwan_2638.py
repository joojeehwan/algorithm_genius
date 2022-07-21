'''

2636 치즈를 풀었엇구나,,


bfs가 떠오른다,,


그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서
적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다.

이걸 어떻게 확인하지!?

놓치지 말아야 하는 것
치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다.
그러므로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다

아 어렵네,, 이거 참내,,

좀만 더 생각하고 다시 풀어보자,,!!
답을 보더라도 내 풀이로 만들어야 해
'''

from collections import deque
import sys
input = sys.stdin.readline


#델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


#초기 입력
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def bfs():
    q = deque()
    q.append([0,0])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while q:
        row, col = q.popleft()

        for i in range(4):

            next_row = row + dr[i]
            next_col = col + dc[i]

            #범위체크
            if 0 <= next_row < N and 0<= next_col < M:
                #그러면서 한번도 안간 곳

                if visited[next_row][next_col] == False:

                    # 여기는 치즈 => 사라질 가능성이 잇는 곳
                    if MAP[next_row][next_col] >= 1:
                        MAP[next_row][next_col] += 1

                    # 여기는 0인곳! 치즈가 없는곳! 다음번에 가지 않기 위해서
                    # visied 배열에만 표시를 하고 그 다음 bfs를 위해서 q에 넣는다.
                    else:
                        visited[next_row][next_col] = True
                        q.append([next_row, next_col])

while True :
    bfs()
    flag = 0

    for i in range(N):
        for j in range(M):
            if MAP[i][j] >= 3:
                MAP[i][j] = 0
                flag = 1
            #인접한 칸에 공기가 1개인것 -> 그대로 치즈로 유지
            elif MAP[i][j] == 2 :
                MAP[i][j] = 1

    if flag == 1:
        ans += 1
    else:
        break

print(ans)

# import sys
# from collections import deque
# input = sys.stdin.readline

# def visual (List):
#     for i in range(n):
#         print(List[i])

# n,m = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
#
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
#
# def bfs():
#     q = deque()
#     q.append([0,0])
#     visited[0][0] = 1
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
#                 if graph[nx][ny] >= 1:
#                     graph[nx][ny] += 1
#                 else:
#                     visited[nx][ny] = 1
#                     q.append([nx,ny])
# time = 0
# while 1:
#     visited = [[0]*m for _ in range(n)]
#     bfs()
#     flag = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] >= 3:
#                 graph[i][j] = 0
#                 flag = 1
#             elif graph[i][j] == 2:
#                 graph[i][j] = 1
#     if flag == 1:
#         time += 1
#     else:
#         break
#
# print(time)



