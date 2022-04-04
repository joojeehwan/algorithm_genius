'''

보물섬 bfs => 각 좌표마다 bfs를 돌리면 된다.

'''

from collections import deque

#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col):
    # 2. 큐 생성
    q = deque()
    #초기값 생성 및 checked 배열 만들기
    q.append([row, col])
    visited = [[False] * M for _ in range(N)]
    visited[row][col] = True
    num = 0 #최장의 이동거리를 담는,,!

    while q:
        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #범위 체크
            if 0 <= next_row < N and 0 <= next_col < M:
                #그리고 육지이면서 한번도 안들린 곳
                if MAP[next_row][next_col] == "L" and visited[next_row][next_col] == False:
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    num = max(num, visited[next_row][next_col]) #최단 거리이면서 가장 멀리 이동할 수 있는 최단 거리
                    q.append([next_row, next_col])
    return num - 1
N, M = map(int, input().split())

#1. 맵 생성
MAP = [list(map(str, input())) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == "L":
            cnt = max(cnt, bfs(i,j))
print(cnt)



#서로 최단 거리로 이동하면서, 하지만 가장 긴 시간이 걸리는 곳으로,,
# 각 점마다 bfs를 돌려서 가장 값이 큰 두 점의 거리를 계산
# from collections import deque
#
# #델타 배열
#
# #상 하 좌 우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def bfs(row, col):
#
#     q = deque()
#     q.append([row, col])
#     visited[row][col] = True
#     #두 점사이의 최단거리를 기록
#     distance = 0
#
#     while q:
#         now_row, now_col = q.popleft()
#         #for문을 통해서 이동
#         for i in range(4):
#             next_row = now_row + dr[i]
#             next_col = now_col + dc[i]
#
#             #항상 이동후엔 범위 체크
#             #범위 안에 +  한번도 가보지 않은 곳 + 육지
#             if 0 <= next_row < N and 0 <= next_col < M:
#                 if not visited[next_row][next_col] and MAP[next_row][next_col] == "L":
#                     visited[next_row][next_col] = visited[now_row][now_col] + 1 # 이 부분이 포인트 -> 이를 통해서 한칸 이동할때마다 값이 1씩 증가
#                     distance = max(distance, visited[next_row][next_col]) #최단 거리 이면서 가장 멀리 이동을 체크
#                     q.append([next_row, next_col])
#     #return을 사용해서 while이 끝난다음에 함수를 종료
#     return distance - 1
# N, M = map(int, input().split())
#
# #그냥 하나씩 조꺠지 않고 전체 다 가져옴
# # MAP = [input() for _ in range(N)]
#
# # MAP = [list(input()) for _ in range(N)], 아래랑 위가 같은 식
# MAP = [list(map(str, input())) for _ in range(N)]
#
# #체크 배열 만들기
# visited = [[False] * M for _ in range(N)]
#
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if MAP[i][j] == "L":
#             #bfs의 인자로 row, col을 보낸다!
#             cnt = max(cnt, bfs(i, j))
#
# print(cnt)

