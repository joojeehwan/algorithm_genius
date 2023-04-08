'''
아 이거 언제 풀었따 햇더니 이코테에서 풀엇구나,,!

초기 상어의 크기 2
1초에 상하좌우로 인접한 한 칸씩 이동
자신보다 크다? 지나갈 수 없다.
자신보다 작다? 먹는다.
자신과 같다? 먹지 x 지나갈 수 만 있음.

물고기를 다 먹는 데 몇초가 걸리는지 구하라! 

<이동 조건>

* 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
* 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
* 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

'''

from collections import deque



#초기 입력 받기
n = int(input())

MAP = [list(map(int, input().split())) for _ in range(n)]


#델타 배열 for bfs
#상 하 좌 우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


#초기값 변수 설정
now_row = 0
now_col = 0

#아기 상어 어디 있니?!

for row in range(n):
    for col in range(n):
        if MAP[row][col] == 9:
            #상어가 원래 있던 곳으로 다시 상어가 갈 수 있으니! 기록하고, 빈칸으로 만들어 준다.
            MAP[row][col]  = 0
            now_row = row
            now_col = col
            break

#초기 상어 사이즈
size = 2
#상어가 먹은 먹이의 갯수
cnt = 0
#상어의 총 이동 칸 갯수(최소값이 되어야 함)
moveCnt = 0


#먹을 먹이가 없을때를 조건으로 주고! 먹이가 없을 떄 까지 계속 반복문 반복! so While True
#bfs를 한번 돌리고 끝나는게 아님!
while True:

    #큐 생성 및 초기값 세팅
    q = deque()
    #큐에다가 이동시간까지 같이 넣어서! 비교!
    q.append((now_row, now_col, 0))
    #비짓배열 생성
    visited = [[False] * n for _ in range(n)]

    flag = 1e9
    fish = []
    # bfs 시작
    while q :

        start_row, start_col, count = q.popleft()

        #만약! 지금까지의 최소 이동 시간보다 더 시간이 오래 걸린다?! 탐색x
        if count > flag:
            break

        #이동 시작! 델타 배열 활용

        for i in range(4):
            next_row = start_row + dr[i]
            next_col = start_col + dc[i]

            # #이동의 조건 판단
            # if 0 <= next_row < n and 0 <= next_col < n:
            #     #한번도 가지 않은 곳 + 아기 상어보다 같거나 작은곳!
            #     if not visited[next_row][next_col] and MAP[next_row][next_col] < size:
            #         fish.append((next_row, next_col, count + 1))
            #         #flag를 둠으로써 굳이 최단거리가 아닌 물고기들을 탐색 x
            #         flag = count
            
            #장외 판단
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                continue

            #아기상어보다 값이 큰 곳 X, 한번 가본곳 X
            if MAP[next_row][next_col] > size or visited[next_row][next_col] :
                continue

            #여기 if문까지 통과하면 아기상어가 이동은 가능! 

            #먹을 수 있는 물고기들
            #빈칸이 아니어야 하고! 아기상어보다 같아도 안되고! 작아야 한다!
            if MAP[next_row][next_col] != 0 and MAP[next_row][next_col] < size:
                fish.append((next_row, next_col, count + 1))
                flag = count
                
            #일단 이동했으니! 아래와 같이 적는 것
            visited[next_row][next_col] = True
            q.append((next_row, next_col, count + 1))


    #bfs를 통해서 먹을 수 있는 물고기들 다 담고! 이제는 식사(조건에 맞게! 위에서 왼쪽)

    if len(fish) > 0 :
        fish.sort() # 이것만 하면 조건이 되는구나,,!
        #fish라는 이차원형태에서! 가장 맨앞에 있는 것! 정렬을 통해서 조건을 맞춰줫음
        row, col, move = fish[0][0], fish[0][1], fish[0][2]

        #먹은 물고기까지의 이동거리는 위에서 구했으니 거기까지의 이동거리를 총 이동거리에 계속해서 더해간다.
        moveCnt += move
        cnt += 1

        #식사 했으니 물고기 없다!
        MAP[row][col] = 0

        #만약에 내 몸의 사이즈 만큼 먹었다면! 상어의 크기가 증가해야한다.
        if cnt == size:
            size += 1
            cnt = 0
        # now_row, now_col을 기준으로 가까운 거리의 물고기 경우를 전부다 넣고,
        # 다시 bfs를 돌린다.
        now_row = row
        now_col = col
    else:
        #While True문 종료시킨다.
        #위에 if절에서 더이상 먹을 물고기를 bfs를 통해서 담지 못했으니!
        break
print(moveCnt)


#다른 풀이

from collections import deque

INF = 1e9 #최단거리 계산할때 사용

n = int(input())

array = []

for i in range(n):
    array.append(list(map(int,input().split())))

now_size = 2
now_x,now_y = 0,0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x,now_y = i,j
            array[now_x][now_y] = 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]

#모든 위치까지의 최단거리만 계산

def bfs():
    dist = [[-1]*n for _ in range(n)]
    queue = deque([(now_x,now_y)])
    dist[now_x][now_y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if array[nx][ny]<=now_size and dist[nx][ny] == -1:
                    queue.append((nx,ny))
                    dist[nx][ny] = dist[x][y]+1
    return dist

def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j]!=-1 and 1<=array[i][j]<now_size:
                if dist[i][j]<min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    if min_dist == INF: #먹을 물고기가 없는 경우
        return None
    else:
        return x,y,min_dist
result  = 0
ate = 0
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x,now_y = value[0],value[1]
        result+=value[2]
        array[now_x][now_y] = 0
        ate+=1
    if ate>=now_size:
        now_size+=1
        ate = 0






