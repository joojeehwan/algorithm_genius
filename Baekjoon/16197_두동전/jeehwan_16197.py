'''

완전탐색

- N x M 크기의 MAP

- MAP위의 3가지 종류의 경우의 수  :

    1. 동전(2개) : o

    2. 빈 칸 : .

    3. 벽 : #

- 버튼(왼, 오, 위, 아래)을 사용해, MAP위의 동전(2개)이 동시에 움직임.

- 동전 이동 규칙

    1. 이동하려는 칸이 벽이면 동전은 이동X

    2. 이동하려는 방향에 칸이 없으면, 동전은 보드 바깥으로 떨어짐(MAP을 벗어남)

    3. 그 외의 경우에는 이동하려는 방향으로 한 칸 이동.

        => 동전이 있는 곳이라도 갈 수 있음. 동전이 이동하고 나면, 그 곳은 빈 칸 '.'이 될테니깐

- 두 동전 중에서, 하나만 보드(MAP)에서 떨어뜨리기 위해 버튼을 최소 몇번을 눌러야하는지 구해라.



'''
# DFS 풀이1 (visited 배열 사용)


import sys, math
sys.setrecursionlimit(10**6)


N, M  = map(int, input().split())

MAP = [list(input().split()) for _ in range(N)]
visited = []
coins_position = []


# 이동의 방향을 위한 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, -1,0, 1]

ans = math.inf

print(ans)


# coin1 : (row, col) // coin2 : (row, col) // cnt : 버튼을 누르는 횟수
def dfs(coin1, coin2, cnt):
    global ans

    row1, col1 = coin1
    row2, col2 = coin2

    # 가지치기 1 : 10번 보다 더 많이 눌러야 한다면 종료
    if cnt >= 10 :
        return

    # 가지치기 2 : cnt가 res보다 커지는 경우
    # why?! 우리는 최소의 cnt를 찾기 위해 ans를 갱신하고 있는 중
    if cnt >= ans:
        return 

    #가지치기 3: 두 동전 모두 MAP 밖으로 나가게 되는 경우
    if (0 > row1 or N <= row1 or 0 > col1 or M <= col1) and (0 > row2 or N <= row2 or 0 > col2 or M <= col2) :
        return
    
    
    # base 조건 : 두 동전 중에 하나만 MAP에서 떨어지게 되는 경우

    if (0 > row1 or N <= row1 or 0 > col1 or M <= col1) or (0 > row2 or N <= row2 or 0 > col2 or M <= col2) :
        ans = (cnt, ans)
        return
    
    # 재귀 연산 부분
    for i in range(4):
        next_row1 = row1 + dr[i]
        next_col1 = col1 + dc[i]
        next_row2 = row2 + dr[i]
        next_col2 = col2 + dc[i]

        # 이동 후 범위체크

        #두 동전의 이동이 모두 MAP 안에서 이루어질 때
        if 0 <= next_row1 < N and 0 <= next_col1 < M and 0 <= next_row2 < N and 0 <= next_col2 < M:
            # 두 동전 다음이 벽이 아닌 곳으로 이동
            if MAP[next_row1][next_col1] != "#" and MAP[next_row2][next_col2] != "#" and (next_row1, next_col1, next_row2, next_col2) not in visited :
                visited.append((next_row1, next_col1, next_row2, next_col2))
                dfs((next_row1, next_col1), (next_row2, next_col2), cnt + 1)
                visited.pop()
            # 1번 동전은 벽이 있는 곳으로, 2번 동전은 정상적으로 이동
            elif MAP[next_row1][next_col1] == "#" and MAP[next_row2][next_col2] != "#" and (row1, row2, next_row2 , next_col2) not in visited :
                visited.append((next_row1, next_col1, next_row2, next_col2))
                dfs((next_row1, next_col1), (next_row2, next_col2), cnt + 1)
                visited.pop()
            # 2번 동전은 벽이 있는 곳으로, 1번 동전은 정상적으로 이동
            elif MAP[next_row1][next_col1] != "#" and MAP[next_row2][next_col2] == "#" and (next_row1, next_col1, row2, col2) not in visited :
                visited.append((next_row1, next_col1, next_row2, next_col2))
                dfs((next_row1, next_col1), (next_row2, next_col2), cnt + 1)
                visited.pop()


        # 하나 이상의 동전이 이동후 MAP 밖으로
        else:
            visited.append((next_row1, next_col1, next_row2, next_col2))
            dfs((next_row1, next_col1), (next_row2, next_col2), cnt + 1)
            visited.pop()


for row in range(N):
    for col in range(M):
        if MAP[row][col] == "0" :
            coins_position.append((row, col))


dfs(coins_position[0], coins_position[1], 0)
print(ans if ans <= 10 else print(-1))



#dfs 풀이 2

import sys

def solve(r1, c1, r2, c2, depth):
    global answer
    if depth >= 10:
        return

    for i in range(4):
        nr1, nc1 = r1+dr[i], c1+dc[i]
        nr2, nc2 = r2+dr[i], c2+dc[i]
        move = [1, 1]
        # 둘 다 나갔다 continue, 이 밑으로는 적어도 하나는 안에 있다
        if not verify(nr1, nc1) and not verify(nr2, nc2):
            continue

        # nr1, nc1이 안에 있으면서 다음께 # 이면 이동 안함
        if verify(nr1, nc1) and adj[nr1][nc1] == '#':
            nr1, nc1 = r1, c1
            move[0] = 0
        if verify(nr2, nc2) and adj[nr2][nc2] == '#':
            nr2, nc2 = r2, c2
            move[1] = 0

        # 둘 다 이동 안한 경우도 지나쳐주자
        if move[0] or move[1]:
            continue

        # 둘 다 안 나간 경우, 이동하자
        if verify(nr1, nc1) and verify(nr2, nc2):
            solve(nr1, nc1, nr2, nc2, depth+1)
            continue

        answer = min(depth+1, answer)


# x1, y1, x2, y2 가 따로움직여야함.
def verify(r, c):
    if r < 0 or r >= N or c < 0 or c >= M:
        return False
    return True


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, M = map(int, sys.stdin.readline().rstrip().split())
adj = []
coins = []
answer = 0xFF
for r in range(N):
    road = list(sys.stdin.readline().rstrip())
    adj.append(road)
    for i, c in enumerate(road):
        if c == 'o':
            coins.append([r, i])

solve(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)
if answer == 0xFF:
    print(-1)
else:
    print(answer)


#bfs풀이 ( 이 풀이가 제일 깔끔)

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 벽이라면
                if board[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1
            else:  # 둘 다 빠진 경우 무시
                continue

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())

    coin = deque()
    board = []
    temp = []
    for i in range(n):
        board.append(list(input().strip()))
        for j in range(m):
            if board[i][j] == "o":
                temp.append((i, j))

    coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

    print(bfs())

#bfs풀이2

from collections import deque
import sys

def solve():
    queue = deque([(coin[0], coin[1], coin[2], coin[3], 0)])
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    while queue:
        r1, c1, r2, c2, cnt = queue.popleft()
        if cnt >= 10:
            break

        for i in range(4):
            nr1, nc1 = r1+dr[i], c1+dc[i]
            nr2, nc2 = r2+dr[i], c2+dc[i]
            move = [1, 1]
            # 둘 다 나간 경우
            if not (0 <= nr1 < N and 0 <= nc1 < M) or not (0 <= nr2 < N and 0 <= nc2 < M):
            # if not verify(nr1, nc1) and not verify(nr2, nc2):
                continue

            # 하나만 나간 경우
            if not (0 <= nr1 < N and 0 <= nc1 < M) or not (0 <= nr2 < N and 0 <= nc2 < M):
            # if not verify(nr1, nc1) or not verify(nr2, nc2):
                return cnt + 1

            # 둘 다 안나간 경우
            if adj[nr1][nc1] == '#':
                nr1, nc1 = r1, c1
                move[0] = 0
            if adj[nr2][nc2] == '#':
                nr2, nc2 = r2, c2
                move[1] = 0
            if move[0] or move[1]:
                queue.append((nr1, nc1, nr2, nc2, cnt+1))
    return -1


def verify(r, c):
    if 0 <= r < N and 0 <= c < M:
        return True
    return False

N, M = map(int, sys.stdin.readline().rstrip().split())
adj = []
coin = []

for r in range(N):
    road = list(sys.stdin.readline().rstrip())
    adj.append(road)
    for c in range(M):
        if road[c] == 'o':
            coin.extend([r, c])

answer = solve()
print(answer)

