'''
빙산
지구 온난화로 인하여 북극의 빙산이 녹고 있다. 빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자.
빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당되는 칸에는 0이 저장된다.
그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.


 	2	4	5	3
 	3	 	2	5	2
 	7	6	2	4

그림 1. 행의 개수가 5이고 열의 개수가 7인 2차원 배열에 저장된 빙산의 높이 정보

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 따라서 그림 1의 빙산은 일년후에 그림 2와 같이 변형된다.

그림 3은 그림 1의 빙산이 2년 후에 변한 모습을 보여준다. 2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다. 따라서 그림 2의 빙산은 한 덩어리이지만, 그림 3의 빙산은 세 덩어리로 분리되어 있다.


 	 	2	4	1
 	1	 	1	5
 	5	4	1	2

그림 2


 	 	 	3
 	 	 	 	4
 	3	2

그림 3

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

예제 입력1

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0


2

'''


#bfs 풀이
import sys
from collections import deque
input = sys.stdin.readline


#델타 배열 만들기

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


n, m  = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

year = 0
artic = [] #빙산이 담길 list



#빙산 찾기
for i in range(n):
    for j in range(m):
        if MAP[i][j] != 0:
            artic.append((i, j))

def bfs():

    q = deque()
    q.append(artic[0])
    visited = [[False] * m for _ in range(n)]
    visited[artic[0][0]][artic[0][1]] = True

    #탐색한 빙산의 갯수
    search_iceberg = 0
    debug = 1
    cut_iceberg = []
    while q:

        now_row, now_col = q.popleft()
        search_iceberg += 1 # bfs 단위로 덩어리 파악
        cnt = 0 #인접 바다의 갯수 => 0의 갯수

        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]
            #항상 범위
            if 0 <= next_row < n and 0 <= next_col < m:
                #주위에 바다
                if MAP[next_row][next_col] == 0:
                    cnt += 1
                #빙산인데, 한번도 안 가본 곳
                elif MAP[next_row][next_col] > 0 and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))

        #주위에 바다가 있었네?!
        if cnt != 0:
            cut_iceberg.append((now_row, now_col, cnt))

    for row, col, height in cut_iceberg:

        #0 이하로는 가지 않는다.
        if MAP[row][col] - height > 0:
            MAP[row][col] = MAP[row][col] - height
        else:
            MAP[row][col] = 0

        #0이 되어버린 빙산은 뺴서, 갯수를 세야 해서, 이 if문이 들어간다.
        #artic의 갯수를 없애야. searh_iceberg 와 갯수 비교가 가능해짐
        if MAP[row][col] == 0 and (row, col) in artic:

            artic.remove((row, col))

    return search_iceberg

while True:

    # 덩어리가 2개 이상인 경우
    # 한 덩어리의 경우 len(artic)과 bfs의 반환값이 언제나 같음.
    # search_iceberg가 곧 len(artic)의 갯수 만큼 있을테니
    if len(artic) != bfs():
        break

    year += 1

    if sum(map(sum, MAP)) == 0: #빙하가 다 녹았는데도! 덩어리가 2개 이상이 안된 경우
        year = 0
        break

print(year)

'''
# print(artic)

print(len(artic), artic)
print(sum(map(sum, MAP)))

test = 0
for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        test += MAP[i][j]

print(test)

'''



#dfs 풀이

import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

def melt(x, y):
    cnt = 0  # 인접한 바다 개수

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                cnt += 1

    if cnt != 0:
        return x, y, cnt
    else:
        return None

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and arr[nx][ny] != 0:
                dfs(nx, ny)

# 입력
N, M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(N)]

# 풀이
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

while True:
    answer += 1

    # 1. 빙하 녹이기
    reduce = []  # x, y, 녹는 높이
    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0:
                h = melt(x, y)

                if h is not None:
                    reduce.append(h)

    for x, y, h in reduce:
        arr[x][y] = arr[x][y] - h if arr[x][y] - h > 0 else 0

    # 2. 빙하 개수 구하기
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for x in range(1, N):
        for y in range(1, M):
            if arr[x][y] != 0 and not visited[x][y]:
                cnt += 1

                if cnt == 2:
                    break

                dfs(x, y)

    if cnt > 1:  # 종료 조건
        break

    if sum(map(sum, arr[1:-1])) == 0:  # 빙하가 다 녹을때까지 덩어리가 1개?
        answer = 0
        break

# 출력
print(answer)

'''

문제 해결 전략

1. 격자에서 빙산이 위치하는 곳은 1차원 배열에 기록

2. bfs

    1. bfs시작하자마, 덩어리 갯수 체크  

    2. 인접한 곳에 바다가 있는지 체크, 이를 관리할 변수(cnt)필요 

    3. 인접한 곳에 방문한 이후에, 인접한 곳에 있는 같은 덩어리 소속 next_row, next_col q에 추가 

    4. q가 다 돌아, 한 싸이클이 돈 이후에, 2번에서 체크한 cnt와 row, col을 기록배열에 추가 

    5. 하나의 덩어리 사이클(q)가 돈 이후에, 이중 for문을 활용해 빙산의 높이 줄이기.

    6. ****이 문제의 포인트****

        주위의 바다로 인해, 0이 되어버린 빙산을 artic 배열에서 삭제 why?!

        artic배열을 이용해, q에 append하고 visted 배열을 관리.

        전체 사이클을 다 돌고도, 빙산이 존재하는 경우 그 다음 bfs에서 빠지면 안되고, 

        전체 사이클을 다 돈 이후에, 빙산이 다 녹아 0이 되는 경우는 그 다음 bfs에서 제외 되어야 함. 

        2개 이상의 덩어리가 생기는 것을 알기 위해서, 

        만약에 1개의 덩이리의 경우, searh_iceburg의 값과 len(artic)의 값이 항상 같아 진다. 

3. 전체 시물레이션

    - len(artic)과 bfs의 결과 비교

    > 덩어리가 1개인 경우는 artic의 전체 갯수와, bfs의 결과가 항상 같을 것, 
    2개이상이 되는 경우부터 달라짐. 


    - MAP에 빙하가 없는데에도 불구하고, (전체 다 같이 없어지는 경우) 덩어리가 2개 이상 되지 못한 경우 예외처리 


입력
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0 
0 7 6 2 4 0 0
0 0 0 0 0 0 0

'''

from collections import deque

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

# 빙산의 위치를 기록
artic = []

# 정답
ans = 0

for row in range(N):

    for col in range(M):

        if MAP[row][col] != 0:
            artic.append((row, col))

# 델타배열 => 4방향 탐색, 상 하 좌 우

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque()
    # artic 배열의 값을 조절해, bfs가 적절하게 반복되어 질 수 있도록 함.
    q.append(artic[0][0], artic[0][1])
    visited = [[False] * m for _ in range(N)]
    visited[artic[0][0]][artic[0][1]] = True

    # 현재 덩어리에서 탐색한 빙산의 갯수
    cnt_iceberg = 0
    # 주위에 바다가 있어, 높이가 줄어들여할 빙산의 row, col 저장
    cut_iceberg = []

    while q:

        # 빙산 갯수 추가
        cnt_iceberg += 1
        now_row, now_col = q.popleft()
        cnt = 0

        # 4방향 탐색 주위 바다의 갯수 / 같은 덩어리의 빙산 check
        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            # 이동후 범위 체크

            if 0 <= next_row < N and 0 <= next_col < M:

                # 주위 바다 체크
                if MAP[next_row][next_col] == 0:
                    cnt += 1

                # 다음
                elif MAP[next_row][next_col] != 0 and not visited[next_row][next_col]:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True

        # 4방향을 다 돈 이후에, 해당 row, col 인접한 곳에 바다 있었다면?!
        # cut_iceberg에 기록하기
        if cnt != 0:
            cut_iceberg.append((row, col, cnt))

    # while문이 종료된 이후에, for문을 통해 빙산의 크기 줄이기
    # 0이하로는 가지 않아!
    for i, j, cnt in cut_iceberg:

        if MAP[i][j] - cnt <= 0:
            MAP[i][j] = 0

        else:
            MAP[i][j] -= cnt

        if MAP[i][j] == 0 and (i, j) in artic:
            artic.remove((i, j))

    return cnt_iceberg


while True:

    if len(artic) != bfs():
        break

    ans += 1

    # 빙하가 다 녹았는데도, 덩어리가 2개 이상이 안되는 경우

    temp = 0
    for row in range(N):
        temp += sum(MAP[row])

    if temp == 0:
        ans = 0
        break

print(ans)





