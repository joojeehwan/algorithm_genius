'''

스타트 택시

bfs 졸업식


- 각 칸은 비어있거나, 벽

- 택시 이동은 상하좌우로 인접한 칸 1칸(최단경로) / 연료 1칸 소진

- M명의 승객, 여러 승객을 한번에 같이 탑승하는 경우 X(M번 반복)

- 각 승객은 출발지에서만 탑승, 도착지에서만 하차

- 손님 탑승 기준

1) 택시 현재 위치 기준 가장 최단거리 

2) 행 번호가 가장 작은 승객

3) 열 번호가 가장 작은 승객

- 택시와 승객이 같이 서있다면, 거리 0 

- 승객을 태워 도착지 까지 이동 성공 => 그 승객을 태워 이동하면서, 소모한 연료의 양의 2배의 연료 충전

- 이동 중에 도중에 연료가 바닥 나면, 업무 종료
BUT, 도착과 동시에 연료가 바닥 나는 것은 실패로 간주 X


2개의 bfs를 만들자

1. 택시 기준 최단거리에 있는 승객을 찾기 (택시 to 승객)

2. 승객 태운 장소부터, 도착지까지 최단거리로 가는 (택시with승객 to 도착지)


첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N**2, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.

다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.

다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.

그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.

입력
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5


'''

from collections import deque

#벡터 배열 상 하 좌 우


# 와 이렇게 사용이 가능하네?!
# def test() :
#
#     for i in range(3):
#         temp = i
#
#     return temp
# print(test())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, fuel = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

taxi_start_row, taxi_start_col = map(int, input().split())

taxi = [taxi_start_row - 1, taxi_start_col - 1]

#손님들의 시작 좌표
person_departures = []

#손님들의 도착 좌표
person_destinateions = []

# 택시 기준 최단거리에 있는 승객을 찾기 (택시 to 승객)
def bfs_find_person(taxi_row, taxi_col):

    q = deque()
    q.append((taxi_row, taxi_col))
    # visited 배열 안에다가 "최단거리"를 기록해야하기 때문에, False가 아닌 0값을 넣어, Integer로 관리
    # 또한 , True/False로 관리하는 것과 달리 , 초기값을 visited[row][col] = True의 작업을 하지 않아도 된다.
    visited = [[0] * N for _ in range(N)]
    min_distance = 1e9
    #최단 경로가 될 수 있는 승객의 row, col을 담을 리스트
    candidate = []

    while q:
        now_row, now_col = q.popleft()

        # 가지치기 1
        # visted 배열 안에다가, 최단거리를 기록
        # 현재 있는 최단 거리보다 더 길어?! 그럼 굳이 갈 필요가 없지..!
        if visited[now_row][now_col] > min_distance :
            break

        # 현재 좌표가, 손님이 출발지라면?! => 즉 택시가 손님이 있는 곳에 도착했다면, 
        # base 조건
        if (now_row, now_col) in person_departures :
            min_distance = visited[now_row][now_col]
            candidate.append((now_row, now_col))

        # else 존재 이유
        # => 아래에 있는 for문에서, 인접한(4개의 방향)으로 now_row/now_col에서 이동을 하는데, else가 없다면 이미 도착한 곳에서 또 이동을 하는건데
        # 이건 이상하자나
        else:
            for k in range(4):
                next_row = now_row + dr[k]
                next_col = now_col + dc[k]

                #이동 후 범위 체크,
                if 0 <= next_row < N and 0 <= next_col < N:
                    # 한번도 가보지 않은 곳 이면서, 벽이 아닌 곳
                    if not visited[next_row][next_col] and MAP[next_row][next_col] != 1 :
                        # 최단거리 => visited배열을 활용한
                        visited[next_row][next_col] = visited[now_row][now_col] + 1
                        q.append((next_row, next_col))


    if candidate:
        # candidate에 값이 들어오는 순간 이미 그 값은 최단거리를 보장, 행, 열, 기준으로 오름차순 정렬 => 이미 행 / 열 순으로 값을 넣었음
        candidate.sort()
        # 최단거리, row, col 반환
        return visited[candidate[0][0]][candidate[0][1]], candidate[0][0], candidate[0][1]
    else:
        return -1, -1, -1



# 승객 태운 장소부터, 도착지까지 최단거리로 가는 (택시with승객 to 도착지)
def bfs_destination(person_start_row, person_start_col, person_end_row, person_end_col) :
    q = deque()
    q.append((person_start_row, person_start_col))
    visited = [[0] * N for _ in range(N)]

    while q:
        now_row, now_col = q.popleft()

        #지금 온 곳이, 바로 도착지라면 ?!
        if (now_row, now_col) == (person_end_row, person_end_col) :
            break

        for k in range(4):
            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            # 범위 안에 있고
            if 0 <= next_row < N and 0 <= next_col < N :
                # 한 번도 가지 않은 곳 이면서, 벽이 아닌 곳
                if not visited[next_row][next_col] and MAP[next_row][next_col] != 1 :
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    q.append((next_row, next_col))

    #while문이 끝났을 때의 now_row, now_col을 이런식으로 return이 가능
    return visited[now_row][now_col], now_row, now_col


for _ in range(M):
    start_row, start_col, end_row, end_col = map(int, input().split())
    person_departures.append((start_row - 1, start_col - 1))
    person_destinateions.append((end_row - 1, end_col - 1))



for _ in range(M):

    debug = 1

    distance, p_row, p_col = bfs_find_person(taxi[0], taxi[1])

    if distance == -1 or fuel - distance < 0 :
        fuel = -1
        break

    debug = 1

    fuel -= distance
    index = person_departures.index((p_row, p_col))
    person_departures[index] = (-1, -1)
    distance2, p_row2, p_col2 = bfs_destination(p_row, p_col, person_destinateions[index][0], person_destinateions[index][1])
    if (p_row2, p_col2) != person_destinateions[index] or fuel - distance2 < 0:
        fuel = -1
        break

    debug = 1

    fuel += distance2
    taxi = [p_row2, p_col2]

print(fuel)








