'''

마법사 상어 시리즈

아니 문제가 이해가 안되는데!?

=> na982 문제 이해 강의 참고.



1. 최대 N이 6인 2^N * 2^N의 이차원 배열의 각 칸안에 얼음의 양이 입력된다.

2. 최대 Q가 1000인 파이어 스톰을 시전하면서 변경되는 얼음을 시뮬레이션

    => 내가 이상하게 이해하고 있던 부분.

    - 2^L *  2*L 의 크기 안에서! 로테이션이 일어나느 것! 그 크기만큼 전환이 되는 것이 아니라!

    - 실제로 로테이션이 일어나는 크기는 2^(L - 1)의 크기 만큼 돌아간다.

    - 근데 얼음이 3칸 이상 인접하지 않는다(0, 1, 2 인접하면 얼음이 준다))

        * 근데 이것이 가능해,,?! 다 얼음이 있는데..! 아예 처음부터 0이 있는 경우가 아니라면?!
        * 아 그러네. 예제 6번의 경우가 64가 아니라, 다른 값이 나온다.

        * 각 모서리에 있는 경우가 줄어들 수 있겠구나

3. 시뮬레이션 이후에 남아 있는 얼음의 총량과 얼음 덩어리 중 가장 큰 덩어리가 차지 하는 칸의 개수를 구하라.


구현해야 하는 것

- 1) 2^L *  2*L의 격자 크기로 나누고, 그 안에서 시계방향으로 90도 회전

>  격자 크기 나누는 것?! 반복문으로

> 90도 회전 : row = col / col = N - 1 - row


- 2)  얼음이 3칸 이상 인접하지 않으면, 얼음의 양을 줄인다.

 > 단순히 이차 포문을 돌면서, 이웃 데이터 체크하자.

- 3)  DFS, BFS를 사용해서(완탐) 가장 큰 얼음덩어리의 크기(칸의 개수를)를 구한다.

> dfs로 하자! bfs로도 해보고!

'''

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

#하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


#데이터 입력받기

n, q = map(int, input().split())
n = 2 ** n
MAP = [list(map(int, input().split())) for _ in range(n)]
l = list(map(int, input().split()))

# print(l)
# visited = [[False] * n for _ in range(n)] 이거 만들어서 하면 매모리 초과난다..! 그냥 MAP를 이용
ans = 0
cnt = 0

def dfs(row, col):
    global ans
    ret = 1 #개수 counting
    # visited[row][col] = True
    MAP[row][col] = 0
    for dir in range(4) :
        next_row = row + dr[dir]
        next_col = col + dc[dir]

        #범위 체크, 한번도 가지 않은 곳 + 얼음 없는 곳은 가지 않아.
        if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] :
            ret += dfs(next_row, next_col)
    #가장 큰 덩어리가 차지하는 칸의 개수이니..!
    ans = max(ans, ret)
    return ret

for L in l:

    k = 2 ** L
    # l의 단계에 맞게, 격자 나누기 => 이게 제일 어렵다.
    for row in range(0, n, k):
        for col in range(0, n, k):
            temp = []
            for i in range(row, row + k):
                temp.append(MAP[i][col:col + k])
            # print(temp)

            #회전
            for i in range(k):
                for j in range(k):
                    MAP[row + j][col + k - 1 - i] = temp[i][j]

    # print(MAP)

    #근처 얼음 counting 그 이후에 제거 (세는 것과 녹이는 것을 동시에 할 수 없다.)
    iceCnt = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            for dir in range(4):
                next_row = row + dr[dir]
                next_col = col + dc[dir]

                #범위 체크 & 얼음이 있으면
                if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] > 0:
                    iceCnt[row][col] += 1

    for row in range(n):
        for col in range(n):
            if MAP[row][col] > 0 and iceCnt[row][col] < 3:
                iceCnt[row][col] -= 1

for row in range(n):
    for col in range(n):
        cnt += MAP[row][col]
        if MAP[row][col] > 0 :
            dfs(row, col)
print(cnt)
print(ans)


'''
bfs 풀이


'''

import sys
from copy import deepcopy
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(2 ** N)]
L = list(map(int, sys.stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for rotate in L:
    # 회전
    rotate_A = [[0] * (2 ** N) for _ in range(2 ** N)]
    # 부분 격자
    for i in range(0, 2 ** N, 2 ** rotate):
        for j in range(0, 2 ** N, 2 ** rotate):
            # 부분 격자 내 회전(오른쪽 열부터 채워 나가기 위해 i2 j2를 뒤집음)
            for i2 in range(2 ** rotate):
                for j2 in range(2 ** rotate):
                    rotate_A[i + j2][j + 2 ** rotate - 1 - i2] = A[i + i2][j + j2]
    A = deepcopy(rotate_A)

    # 얼음이 3칸 미만으로 인접한 부분 줄이기
    for i in range(2 ** N):
        for j in range(2 ** N):
            count = 0
            for k in range(4):
                mx = i + dx[k]
                my = j + dy[k]
                if mx < 0 or mx >= 2 ** N or my < 0 or my >= 2 ** N:
                    continue
                if A[mx][my] > 0:
                    count += 1
            if count < 3 and rotate_A[i][j] > 0:
                # 만약 이전 칸에 얼음이 녹아서 0이 되면 영향을 끼칠 수 있으므로
                # A를 기준으로 검토하여 rotate_A에서 녹이는 작업 후 deepcopy를 실행
                rotate_A[i][j] -= 1
    A = deepcopy(rotate_A)

# 얼음의 합 계산
sum_result = 0
for i in range(2 ** N):
    sum_result += sum(A[i])


# 가장 큰 덩어리가 차지하는 칸의 개수 계산
def bfs(x, y):
    q = deque()
    q.append((x, y))
    A[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= 2 ** N or ny < 0 or ny >= 2 ** N:
                continue
            if A[nx][ny] > 0:
                cnt += 1
                q.append((nx, ny))
                A[nx][ny] = 0
    return cnt


block_result = 0
for i in range(2 ** N):
    for j in range(2 ** N):
        if A[i][j] > 0:
            block_result = max(block_result, bfs(i, j))

print(sum_result)
print(block_result)