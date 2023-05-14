'''

1 - 6 이하의 임의의 숫자가 그려진 n * n의 격자판

주사위(정육면체)를 굴린다. 해당 주사위는 1 - 6까지의 숫자가 적혀있고,  m번에 걸쳐 주사위를 계속 1칸씩 굴리게 된다. 이떄 마주보는 주사위의 합은 정확히 7


- 주사위 진행방향 및 점수 획득 방법

*) 주사위는 항상 초기에 격자판의 1행 1열에 놓여져 있고, 처음에는 항상 오른쪽으로 이동한다.

*) 주사위를 움직일 때마다, 격자판위에 주사위가 놓여있는 칸에 적혀있는 숫자와 상하좌우로 인접하며 같은 숫자가 적혀있는 모든 칸의 합만큼 점수를 획득 (bfs)

*) 초기 1행 1열에서의 오른쪽으로 한 칸 이동후에는 주사위의 아랫면(격자와 맞닿는 부분)과 격자의 숫자를 비교해 방향을 설정

    1) 주사위의 아랫면의 숫자가 맞닿고 있는 격자의 숫자 보다 더 크다면, 진행방향의 90도 반시계 방향

    2) 주사위의 아랫면의 숫자가 맞닿고 있는 격자의 숫자 보다 더 작다면, 진행방향의 90도 시계 방향

    3) 진행 도중 격자판을 벗어나게 되는 경우엔 => 방향이 반대로 (모듈려 연산)


'''

from collections import deque

#초기 입력 및 세팅

n,m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

#동 남 서 북 => 맨 처음 이동은 동쪽으로 이동, 이에 반대방향과 초기이동을 고려해 "동남서북"으로 델타 배열을 결정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

#주사위 격자
dice = [1,2,3,4,5,6]

#bfs로 점수의 총합 구하기

row, col, dir, ans = 0, 0, 0, 0

def bfs(row, col, NUM) :

    #bfs 시작
    '''
    NUM가 같은 숫자들의 인접하게 몇개나 있는지 확인해 갯수를 return
    '''
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    #일단 처음에 있는 값은 무조건 세야 하니 1
    cnt = 1
    while q:
        now_row, now_col = q.popleft()

        for k in range(4):

            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            if 0 <= next_row < n and 0 <= next_col < n:
                #방문하지 않았으면서, 인자로 주어진 NUM가 같은 숫자들만 cnt에 추가
                if not visited[next_row][next_col] and MAP[next_row][next_col] == NUM :
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))
                    cnt += 1
    return cnt

#시물레이션 m번 진행

for _ in range(m):

    #만약에 주사위가 맵 밖에 있으면, 반대 방향으로 갈 수 있도록
    if not 0 <= row + dr[dir] < n or not 0 <= col + dc[dir] < n :
        dir = (dir + 2) % 4

    #주사위 이동
    row = row + dr[dir]
    col = col + dc[dir]

    #방문 기록 배열, bfs함수 밖에 만들어, bfs함수와 별개로 전역적으로 관리
    visited = [[False] * n for _ in range(n)]

    #점수 획득 로직 실행 =>  횟수 * 실제 격자의 값
    ans += (bfs(row, col, MAP[row][col])) * MAP[row][col]


    # 초기 : 동쪽
    # 초기 이후 : 격자와, 격자와 맞닿는 주사위의 아랫면과의 비교를 통해, 주사위를 이동시킴.

    # 동쪽으로 이동 할떄의 주사위 변화
    if dir == 0 :
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 남쪽으로 이동 할떄의 주사위 변화
    elif dir == 1 :
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    # 서쪽으로 이동 할떄의 주사위 변화
    elif dir == 2 :
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 북쪽으로 이동 할떄의 주사위 변화
    else :
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    #주사위의 아랫면 check를 통해 다음 반복을 위한 주사위 이동방향을 결정

    if dice[5] > MAP[row][col] : #시계 방향  dr, dr에서 +1을 더하면(index 이동) 시계방향 이동
        dir = (dir + 1) % 4

    elif dice[5] < MAP[row][col] : #반 시계 방향  dr, dr에서 +3을 더하면(index 이동) 반시계방향 이동
        dir = (dir + 3) % 4  #^2

print(ans)