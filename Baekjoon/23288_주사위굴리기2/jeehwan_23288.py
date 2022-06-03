#재미 있는 구현

'''
1. 주사위 이동 => 주사위 맨 아래 vs (row, col)에 점수 비교

주사위 맨아래  > (row, col) 시계 방향 90도
주사위 맨아래  < (row, col) 반시계 방향 90도
주사위 맨아래 = (row, col) 방향 이동 없음

단, 그 다음 이동할 칸이 없으면(범위 밖) 그 반대 방향으로 이동
ex) 서쪽 -> 동쪽, 북쪽 -> 남쪽

2. 이동 후 (dfs / bfs)로 같은 숫자를 가지는 것들의 합


아 주사위 인덱스,,,
전개도 수정 ㅠㅠ 진짜 짜증ㅇ난다!!

주사위 남 / 북쪽으로 이동 => 가운데 줄이 컨테이너 같이 이동 
주사위 동 / 서쪽으로 이동 =>  십자가의 가로에서 이동이 일어나고, 
맨아래가 방향에 따라서 바뀌게 된다
'''
import sys
from collections import deque
input = sys.stdin.readline

#델타 배열 만들기
#이것도 중요! 그냥 무지성 상하좌우 하면 안돼! => 동남서북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(row, col, B):
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    cnt = 1
    while q:
        now_row, now_col = q.popleft()
        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]
            #범위 check
            if 0 <= next_row < N and 0<= next_col < M:
                if not visited[next_row][next_col] and MAP[next_row][next_col] == B:
                    cnt += 1
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))

    return cnt
N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
#아 주사위를 1차원 배열로 하면 되는디,, 이런 생각이 안난다 ㅠㅠㅠ
dice = [1,2,3,4,5,6]

row, col, dir, ans = 0, 0, 0, 0

#k번 주사위를 이동하면서! 점수를 check할꺼니깐!
for _ in range(K):

    #주사위가 맵 범위에 있는지 check! 범위 밖이면 반대 방향으로
    if not 0 <= row + dr[dir] < N or not 0 <= col + dc[dir] < M:
        dir = (dir + 2) % 4

    row = row + dr[dir]
    col = col + dc[dir]

    visited = [[False] * M for _ in range(N)]

    ans += (bfs(row, col, MAP[row][col])) * MAP[row][col]

    #주사위 방향 동쪽
    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 주사위 방향 남쪽
    elif dir == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    # 주사위 방향 서쪽
    elif dir == 2:  
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 주사위 방향 북쪽
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    if dice[5] > MAP[row][col]: #시계방향이동
        dir = (dir + 1) % 4
    elif dice[5] < MAP[row][col]: #반시계방향이동
        dir = (dir + 3) % 4

print(ans)


'''
#주사위를 2차원 배열로 보고! 이게 더 주사위 이해하기는 쉽다! 
from collections import deque
 
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
 
dy = (-1, 0, 1, 0)
dx = ( 0,-1, 0, 1)
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
dir = RIGHT
dice = [
    [ -1,  2, -1],
    [  4,  1,  3],
    [ -1,  5, -1],
    [ -1,  6, -1]
]
def move_dice(dir):
    global dice
 
    if dir == RIGHT:
        tmp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = tmp
    elif dir == LEFT:
        tmp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = tmp
    elif dir == UP:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    elif dir == DOWN:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
 
def get_score_by_bfs(sy, sx, B):
    used = [[False] * M for _ in range(N)]
    cnt = 0
    q = deque()
    q.append((sy, sx))
    used[sy][sx] = True
    while q:
        y, x = q.pop()
        cnt += 1 # count 추가
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
 
            if ny < 0 or nx < 0 or ny >= N or nx >= M or used[ny][nx]:
                continue
            if board[ny][nx] == B:
                used[ny][nx] = True
                q.append((ny, nx))
    return cnt * B # 점수 = B x B의 개수
 
loc = (0, 0)
result = 0
for i in range(K):
    ny = loc[0] + dy[dir]
    nx = loc[1] + dx[dir]
 
    if ny < 0 or nx < 0 or ny >= N or nx >= M: # 이동할 수 없는 경우
        dir = (dir + 2) % 4 # 방향을 180도 바꿔서 이동
        ny = loc[0] + dy[dir]
        nx = loc[1] + dx[dir]
 
    loc = (ny, nx)
    move_dice(dir) # 주사위 이동
    B = board[ny][nx] # 이동한 좌표의 숫자
    score = get_score_by_bfs(ny, nx, B) # BFS를 이용하여 점수 계산
    result += score
 
    #맨 아랫쪽 주사위 값(A)과 이동한 좌표의 숫자(B) 비교
    A = dice[3][1]
    if A > B: dir = (dir - 1) % 4
    elif A < B:dir = (dir + 1) % 4
 
print(result)
 



'''

