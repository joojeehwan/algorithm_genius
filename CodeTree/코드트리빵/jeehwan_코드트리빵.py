
'''

예시)

for num in range(n ** 2):

    #각 학생번호와 그 학생의 선호도 학생들이 번호로
    student = students[num]
    temp = []

    #완탐
    for row in range(n):
        for col in range(n):
            #일단 가지 않았 던 곳으로 가야한다.
            if not visited[row][col]:
                #자리를 선택하는 기준이 되는 선호도와 빈공간 counting
                like = 0
                blank = 0
                for k in range(4):
                    next_row = row + dr[k]
                    next_col = col + dc[k]

                    if 0 <= next_row < n and 0 <= next_col < n:
                        # 주위에 선호하는 학생이 있다면! 다 카운팅하기
                        if visited[next_row][next_col] in student[:] :
                            like += 1

                        if visited[next_row][next_col] == 0:
                            blank += 1

                temp.append([like, blank, next_row, next_col])

    #람다 관련해서 더 공부
    temp.sort(key = lambda x : (-x[0], -x[1], x[3], x[2]))
    #이제 실제 MAP에다가 넣기! 가장 맨 앞이 학생 번호 인 것.
    visited[temp[num][2]][temp[num][3]] = student[0]
    
    
    
문제 정리 

- m명의 사람

- 1번 사람은 1분, 2번 사람은 2분에, ... , n번 사람은 정확히 n분에 편의점으로 이동

- 출발 시간이 되기 전까지 격자 밖으로, 사람들이 목표로 하는 편의점은 모두 다름

- N * N 크기의 격자에서 진행


1분 동안 진행되는 시물레이션 

1) 격자에 있는 사람들이 가고 싶어하는 편의점 방향으로 1칸 움직이기. 최단거리로 움직임. 최단거리의 방법이 여러가지인 경우 상 좌 우 하 의 순위로 움직임
 - 여기서 말하는 최단거리는 인접(4방향)으로 이동한 칸 으로 이동한 횟수가 가장 적은

2)  편의점에 도착하면, 해당 편의점에서 멈추고, 이때부터 다른 사람들은 해당 편의점에 방문하지 못함.

3) 현재 시간이 t분이고, t <= m 을 만족하다면, t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는(최단거리) 베이스 캠프에 들어감. 이때도 가장 가까운 베이스 캠프가 여러가지인 경우 
 행 , 열 이 작은 순서로 들어감. 
 베이스 캠프로 이동하는 데에는 시간이 소요되지 않음.
 사람이 들어간 베이스 캠프는 다른 사람이 지나가지 못함.  
 


입력

첫 번째 줄에는 격자의 크기 n과 사람의 수 m이 공백을 사이에 두고 주어집니다.

이후 n개의 줄에 걸쳐 격자의 정보가 주어집니다. 각 줄에 각각의 행에 해당하는 n개의 수가 공백을 사이에 두고 주어집니다.
0의 경우에는 빈 공간, 1의 경우에는 베이스캠프를 의미합니다.

이후 m개의 줄에 걸쳐 각 사람들이 가고자 하는 편의점 위치의 행 x, 열 y의 정보가 공백을 사이에 두고 주어집니다.

각 사람마다 가고 싶은 편의점의 위치는 겹치지 않으며, 편의점의 위치와 베이스캠프의 위치도 겹치지 않습니다.

2 ≤ n ≤ 15
1 ≤ m ≤ min(n**2 , 30)
m ≤ 베이스 캠프의 개수 ≤ n ** 2 −m

5 3
0 0 0 0 0
1 0 0 0 1
0 0 0 0 0
0 1 0 0 0
0 0 0 0 1
2 3
4 4
5 1


출력

모든 사람이 편의점에 도착하는 시간을 출력하세요.

문제 조건에 의해 어떠한 사람이 원하는 편의점에 도달하지 못하게 되는 경우는 절대 발생하지 않음을 가정해도 좋습니다.
또한, 이동하는 도중 동일한 칸에 둘 이상의 사람이 위치하게 되는 경우 역시 가능함에 유의합니다.

 
'''
# 편의점 리스트 관리 , 이런식으로 굳이 이차원 배열의 형태로 관리 하지 않아 why?!
# 리스트에서 뽑아서, 람다의 형태로 우선순위를 관리 할꺼니깐!

#초기 편의점 입력 받는다!
# cu_list = []
#
# for _ in range(m):
#     row, col = map(int, input().split())
#     cu_list.append((row - 1, col - 1))
#
# # bfs 함수 기록
# visited = [[False] * n for _ in range(n)]
#
# # 최단 거리 아아...!  아 이거 굳이 visited 배열로도 할 수 있다!
#
# # 이 문제에서 이것을 쓴 이유는,
# # 각 편의점별로(row, col)별로 가장 최단거리를 인덱스별로 기록하기 위힘
# shortest = [[0] * n for _ in range(n)]
#
# # 근데 원래 본디 나는 굳이 다른 메모리 써가면서 하지 않았음. 그냥 visted에다가 적으면서 했음.
# visited_2 = [[0] * n for _ in range(n)]
#
# # dx, dy값을
# # 문제에서의 우선순위인 상좌우하 순으로 적어줍니다.
# dr = [-1,  0, 0, 1]
# dc = [ 0, -1, 1, 0]

#bfs 함수, 최단
# def bfs(row, col):
#     #만약에 visited 배열이 밖에 있엇다면, 굳이 이렇게 초기화를 하지 않아도 되었을 것
#     for i in range(n):
#         for j in range(n):
#             visited[i][j] = False
#             #viisted_2[row][col] = 0
#             #shortest[row][col] = 0
#     q = deque()
#     q.append((row, col))
#     visited[row][col] = True
#     # visted_2[row][col] = 1
#     # 그리고 아래 shortest는 없고
#     #최단거리 갱신
#     shortest[row][col] = 0
#
#     while q :
#
#         now_row, now_col = q.popleft()
#
#         for i in range(4):
#             next_row = now_row + dr[i]
#             next_col = now_col + dc[i]
#
#             #범위 생각, 한번도 가보지 않은 곳.
#
#             if 0 <= next_row < n and 0 <= next_col < n :
#                 #visited_2 의 처음을 0으로 두면, 아예 안 간 곳만 체크를 하게 된다.
#                 if not visited[next_row][next_col] and MAP[next_row][next_col] != 2 :
#
#                     q.append((next_row, next_col))
#                     visited[next_row][next_col] = True
#                     #visited_2[next_row][next_col] = visted_2[now_row][now_col] + 1
#                     shortest[next_row][next_col] = shortest[now_row][now_col] + 1
#
# print(shortest)



#답안

from collections import deque
import sys
#상 좌 우 하 => 문제에 주어진 우선순위대로
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

INF = int(1e9)
#초기 입력
n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

#편의점 위치(인덱스 처리)
stores = []
for _ in range(m):
    row, col = map(int, input().split())
    stores.append([row -1, col - 1])

time = 0
# m번째 사람이 현재 어디 있는지 위치 기록  , idx가 m번째 사람을 뜻함. 
peoples = [[-1, -1] for _ in range(m)]

# bfs 함수 최단거리 (3. 베이스 캠프 찾기)
def bfs(idx, row, col) :
    #큐생성 = > 초기값 큐 삽입 = > visite배열 생성 => visted배열 초기값 체크 
    q = deque()
    q.append((0, row, col))
    visited = [[False] * (n) for _ in range(m)]
    visited[row][col] = True
    #최단거리이면서 베이스캠프가 될 수 있는 녀석들의 후보군 리스트 
    candidates = []

    #현재위치 기준으로 bfs를 돌면서, 최단거리로 갈 수 있는 베이스 캠프 조사
    while q :

        lev, row, col = q.popleft()

        #베이스캠프야?!  base 조건
        if MAP[row][col] == 1 :
            candidates.append((lev, row, col))
            # continue도 중요한 키워드, return이 아닌 건, 이 bfs함수를 통해 하나의 최단거리만 딱 보는 것이 아니라,
            # 같은 거리의 최단거리일 때, 행과 열의 위치를 통해 우선순위를 정하기 때문에, return 혹은 break를 통해 반복을 끝내는 것이 아니라
            # continue를 통해 다음 반복으로 넘어간다.
            continue

        # 4방향 탐색
        for i in range(4):
            
            #next_row /col 생성
            next_row = row + dr[i]
            next_col = col + dc[i]

            #이동후 항상 범위 체크
            if 0 <= next_row < n and 0 <= next_col < m :
                #g한번도 가지 않은 곳 이면서, 사람이 있지 않은 곳으로(임의로 내가 사람이 있는 곳은 2라 정의)
                if not visited[next_row][next_col] and MAP[next_row][next_col] != 2:
                    q.append((lev + 1, next_row, next_col))
                    visited[next_row][next_col] = True

    # 람다를 통해 정렬 -> 일단 거리가 짧을수록, 만약에 같은 거리라면 행, 그 다음에 열을 기준으로 정렬
    candidates.sort(key=lambda x : (x[0], x[1], x[2]))
    row, col = candidates[0][1], candidates[0][2] #조건에 맞는 가장 가까운 베이스 캠프 why?! 0번째(가장 맨앞)에 있는 값이 해당 조건을 가장 만족
    MAP[row][col] = 2 # 그곳은 현재 사람이 있다. why?! 문제에 이르길 베이스 캠프로는 바로 한번에 간다! 시간 소모 없이
    # 사람 위치 이동 - idx가 m번째 사람을 의미
    peoples[idx][0], peoples[idx][1] = row, col


# 시뮬레이션
while True :

    time += 1
    #1. 격자에 있는 모든 사람들이 편의점을 향해 1칸 움직이기(최단거리 이동)
    for i in range(m):
        #아예 밖에 있거나, 원하는 편의점에 도착했으면 편의점을 향해 1칸 움직일 필요가 없다.
        if peoples[i] == [-1, -1] or peoples[i] == stores[i]:
            continue

        # 해당 사람의 현재 위치
        row, col = peoples[i]
        minDist = INF
        min_row, min_col = row, col

        for j in range(4):

            #우선순위에 맞게 다음 row, col을 선택
            next_row = row + dr[j]
            next_col = col + dc[j]

            #선택된 next_row, next_col을 기준으로 다시 bfs를 돌려 편의점을 향해 가는 최단거리를 계산
            #이동 후 범위 체크
            if 0 <= next_row < n and 0 <= next_col < n:

                q = deque()
                q.append((0, next_row, next_col))
                visited_store = [[False] * n for _ in range(n)]
                visited_store[next_row][next_col] = True

                while q :
                    lev, cu_row, cu_col = q.popleft()
                    #편의점에 도착
                    if cu_row == stores[i][0] and cu_col == stores[i][1]:
                        # 이런식으로 lev를 만든 이유는 bfs로 최단거리를 구할 수 있지만, 하나의 점에서 점으로 이동하는 거리를 알기 위해서
                        # 변수를 하나 만들어 값을 누적시키면서, 그 값으로 전체적인 최단 거리 뿐만 아니라, bfs로도 특정 점과 점 사이의 거리를 구하기 위함.
                        if minDist > lev:
                            minDist = lev
                            min_row, min_col = next_row, next_col
                            break

                    for k in range(4):

                        next_cu_row = cu_row + dr[k]
                        next_cu_col = cu_col + dc[k]

                        #이동후 범위 설정

                        if 0 <= next_cu_row < n and 0 <= next_cu_col < n :
                            if not visited_store[next_cu_row][next_cu_col] and MAP[next_cu_row][next_cu_col] != 2 :
                                q.append((lev + 1, next_cu_row, next_cu_col))
                                visited_store[next_cu_row][next_cu_col] = True


            peoples[i] = [min_row, min_col]

    #2. 편의점 도착시 멈추고, 지나갈 수 없다.

    for i in range(m):
        if peoples[i] == stores[i]:
            row, col = peoples[i]
            MAP[row][col] = 2

    flag = True

    for i in range(m):
        #아직 편의점이 아냐
        if peoples[i] != stores[i] :
            flag = False
            break

    if flag :
        print(time)
        break

    if time > m:
        continue
    #편의점 위치 기준으로 베이스 캠프를 찾기
    bfs(time - 1, stores[time - 1][0], stores[time - 1][1])



