from collections import deque

#초기 입력 및 세팅

n,m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

#동 남 서 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dice = [1,2,3,4,5,6]

#bfs로 점수의 총합 구하기

row, col, dir, ans = 0, 0, 0, 0

def bfs(row, col, NUM) :

    #bfs 시작
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    cnt = 1
    while q:
        now_row, now_col = q.popleft()

        for k in range(4):

            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            if 0 <= next_row < n and 0 <= next_col < n:
                if not visited[next_row][next_col] and MAP[next_row][next_col] == NUM :
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))
                    cnt += 1

    return cnt


for _ in range(m):

    #만약에 주사위가 맵 밖에 있으면, 반대 방향으로 갈 수 있도록
    if not 0 <= row + dr[dir] < n or not 0 <= col + dc[dir] < n :
        dir = (dir + 2) % 4


    row = row + dr[dir]
    col = col + dc[dir]

    visited = [[False] * n for _ in range(n)]

    ans += (bfs(row, col, MAP[row][col])) * MAP[row][col]

    # 동쪽
    if dir == 0 :
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 남쪽
    elif dir == 1 :
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    # 서쪽
    elif dir == 2 :
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]

    # 북쪽
    else :
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    #주사위의 아랫면 check

    if dice[5] > MAP[row][col] : #시계 방향
        dir = (dir + 1) % 4

    elif dice[5] < MAP[row][col] : #반 시계 방향
        dir = (dir + 3) % 4

print(ans)