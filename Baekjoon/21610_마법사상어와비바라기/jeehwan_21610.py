'''



게임 규칙에 따라, 구름이 생성, 이동, 소멸

물 복사 버그 마법을 시전하면, 규칙에 따라 물이 증가.

M 번의 이동이 완료된 후에 남아 있는 물의 총 량을 리턴




구현 해야 하는 것 => 이를 시뮬레이션 M번 반복

1) 구름을 이동

=>
구름의 위치 좌표를 저장하고, 이동하는 크기만큼 증가
그후에, 모듈러 연산을 통해서, 위치좌표를 계산


2)구름이 있는 칸에 물을 증가

=>
구름의 위치를 반복문으로 순회 하면서, 물을 증가 시키는 로직

3) 구름을 소멸
=>

추후에 물 복사 버그와 구름 생성시 활용을 위해, 소멸 되는 구름의 위치를 기억해야 한다.

백업이 되는 2차원 공간에, 사라지는 구름의 위치를 기록하자.

4) 물 복사 버그

=>
대각선에(4방향), 0이 아닌 숫자를 카운트하고, 그 숫자들 만큼 버그를 시작하는 좌표에 물을 증가(복사)

≈
5) 구름 생성

=>

물이 2이상 있는 칸에 구름을 생성 x => 구름이 생기는 곳은 물의 양이 줄어든다.

단, 구름이 소멸된 칸에서는 구름이 생성되지 않습니다.

'''

import sys
input = sys.stdin.readline


#초기 입력

#n : 격자 크기, m : 시물레이션 횟수
n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

#구름 이동 방향
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
#초기 구름 세팅
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

# 물복사 버그 마법 시작 좌상 대각 / 우상 대각 / 좌하 대각 / 우하 대각
magic_dr = [-1, -1, 1, 1]
magic_dc = [-1, 1, -1, 1]

# distance_dir = [list(map(int, input().split())) for _ in range(m)]
#
# for i in range(m):
#     distance_dir[i][0] = distance_dir[i][0] - 1
#바로 배열을 받는게 아니라, 그 배열안의 값을 조정해야 한다면, for문 풀이로 받는 것이 편리히다.
#문제와 실제 배열의 인덱스간의 차이를 없애기 위해서

distance_dir = []
for i in range(m) :
    temp = list(map(int, input().split()))
    distance_dir.append([temp[0] - 1, temp[1]])

#m회 시뮬레이션 시작
for i in range(m):

    # 1) 구름을 이동시킨다. 모듈려 연산
    moving_d, moving_s = distance_dir[i]
    next_cloud = []
    for clo_row, clo_col in cloud:
        row = clo_row
        col = clo_col
        d, s = moving_d, moving_s
        next_row = (n + row + dr[d] * s) % n
        next_col = (n + col + dc[d] * s) % n
        next_cloud.append([next_row, next_col])

    # 2) 구름이 있는 칸에 물 증가

    visited = [[False] * n for _ in range(n)]

    for mkit_rain in next_cloud:
        row = mkit_rain[0]
        col = mkit_rain[1]
        MAP[row][col] += 1
        visited[row][col] = True

    # 3) 구름을 모두 삭제 => 구름이 있는 칸을 위에서 기록 했음.  visited[row][col] = True, (row, col) : 비가 와서 삭제 된 곳

    cloud = []

    # 4) 물 복사 버그 시작
    for magic_row, magic_col in next_cloud:

        row, col = magic_row, magic_col
        count = 0
        for k in range(4):
            next_row = row + magic_dr[k]
            next_col = col + magic_dc[k]

            #범위 체크 , 비바라기를 사용하는 좌표의 대각선중에서, 해당 좌표에 물이 있다면 => 그 수 만큼 비바라기를 사용하는 곳의 물의 양을 중가
            if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] >= 1 :
                count += 1

        MAP[row][col] += count

    # 5) 구름 생성

    for row in range(n):
        for col in range(n):
            if MAP[row][col] >= 2 and not visited[row][col]:
                MAP[row][col] -= 2
                cloud.append([row, col])


answer = 0
for i in range(n):
    for j in range(n):
        answer += MAP[i][j]

print(answer)




#현우 풀이

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dir_move = [list(map(int, input().split())) for _ in range(m)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
cloud = deque(cloud)

def move_rain(dir, dist):
    global n
    size = len(cloud)
    for _ in range(size):
        x, y = cloud.popleft()
        nx = (x + dx[dir] * dist) % n
        ny = (y + dy[dir] * dist) % n
        if 0 > nx:
            nx += n
        if 0 > ny:
            ny += n
        cloud.append((nx, ny))
        # 구름이 사라진 자리를 표시
        visited[nx][ny] = True
        graph[nx][ny] += 1


def dup():
    while cloud:
        # 대각선 검사
        x, y = cloud.popleft()
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                graph[x][y] += 1


for dir, dist in dir_move:
    visited = [[False] * n for _ in range(n)]
    # 1. 구름 이동 후 비 내리기
    move_rain(dir - 1, dist)
    # 2. 물 복사
    dup()
    # 3. 구름 생성
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and not visited[i][j]:
                cloud.append((i, j))
                graph[i][j] -= 2
answer = 0
for i in range(n):
    for j in range(n):
        answer += graph[i][j]
print(answer)
