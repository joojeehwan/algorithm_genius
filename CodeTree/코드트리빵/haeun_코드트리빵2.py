"""
정답 : 총 몇 분 후에 모두 편의점에 도달하는 가?
"""
from collections import deque


class Person:
    def __init__(self, r, c, store_r, store_c, finish):
        self.r = r
        self.c = c
        self.sr = store_r
        self.sc = store_c
        self.finish = finish

    def __repr__(self):
        return f"위치 {self.r, self.c} || 편의점 : {self.sr, self.sc} || 도달여부 : {self.finish} "


# 입력
N, M = map(int, input().split())

camp = [list(map(int, input().split())) for _ in range(N)]  # 1이면 베이스캠프
block = [[False] * N for _ in range(N)]  # 베이스 캠프, 편의점 도달로 인해 지나갈 수 없는 곳
arrived = 0  # 도착한 사람의 수. M이 되면 반복문은 끝난다.
minute = 0  # 모두 편의점에 도달한 순간

dr = [-1, 0, 0, 1]  # 상 좌 우 하
dc = [0, -1, 1, 0]

people = []  # 사람 저장
for _ in range(M):
    x, y = map(int, input().split())
    # 사람은 처음에 격자 밖에 있어서 (-1, -1)로 처리
    # 왜 자꾸 좌표 1부터 시작하는거로 주는데 ㅡㅡ
    people.append(Person(-1, -1, x - 1, y - 1, False))


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def start(minute):
    # minute에 해당하는 사람이 베이스캠프로 간다.
    person = people[minute]
    sr, sc = person.sr, person.sc  # 원하는 편의점의 위치

    # 원하는 편의점에서 가장 가까운 베이스캠프를 찾는다. (여러개일 수 있다.)
    bc = []
    distance = N ** 2 + 1

    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    q = deque([(sr, sc)])

    # O(N^2)
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if in_range(nr, nc) and not block[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1  # 거리를 재기 위해 visited에 +1을 한다.
                if visited[nr][nc] > distance:  # 이미 찾은 곳 보다 먼 곳은 볼 필요가 없다.
                    continue
                q.append((nr, nc))
                # 이 캠프가 갈만한지 검사해본다.
                if camp[nr][nc]:
                    if visited[nr][nc] < distance:
                        # 최단거리 갱신이면 비우고 넣는다.
                        bc.clear()
                        bc.append((nr, nc))
                        distance = visited[nr][nc]
                    elif visited[nr][nc] == distance:
                        bc.append((nr, nc))

    bc.sort(key=lambda x: (x[0], x[1]))
    person.r, person.c = bc[0]  # 가장 적은 행, 열에 위치한 베이스 캠프로 할당한다.
    block[person.r][person.c] = True  # 이제 이 베이스캠프는 지나갈 수 없다.


def move():
    global arrived

    # O(30) *
    for person in people:
        # 이미 도달한 사람은 넘어간다.
        if person.finish:
            continue
        # 아직 출발하지 않은 사람도 넘어간다.
        if person.r == -1 and person.c == -1:
            continue
        # 편의점에서 BFS를 한다.
        pr, pc = person.r, person.c
        sr, sc = person.sr, person.sc

        visited = [[0] * N for _ in range(N)]
        visited[sr][sc] = 1
        q = deque([(sr, sc)])
        found = N ** 2 + 1  # 사람에게 최초로 닿은 거리. 이보다 큰 visited위치는 안본다.(백트래킹)
        # O(N^2)
        while q:
            r, c = q.popleft()

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                if in_range(nr, nc) and not visited[nr][nc] and not block[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    if visited[nr][nc] > found:  # 이미 찾은 곳 보다 먼 곳은 보지 않는다.
                        continue
                    if nr == pr and nc == pc and visited[nr][nc] < found:
                        found = visited[nr][nc]
                    q.append((nr, nc))

        # 현재 사람 위치에서 상 좌 하 우 로 보면서 가장 적은 visited값을 가진 위치를 고른다.
        distance = N ** 2 + 1  # 가장 가까운 곳 비교
        mr, mc = -1, -1   # move_row, move_col  => 이동할 위치

        # O(4)
        for d in range(4):
            cr, cc = pr + dr[d], pc + dc[d]   # check_row, check_col
            # @@@@@@@@ [디버깅] visited값이 0 이면 아예 막혀서 못 가는 곳인데,
            # 0 < visited를 안 했다가 못 가는 곳을 가도록 만들어버렸다.
            if in_range(cr, cc) and 0 < visited[cr][cc] < distance and not block[cr][cc]:
                distance = visited[cr][cc]
                mr, mc = cr, cc

        # @@@@@@@@ [디버깅] person.r이 아니라 pr에다 할당하면서 왜 안움직이지 이러고 있었다.
        person.r, person.c = mr, mc
        # 움직인 결과, 편의점에 도달한 경우
        if mr == sr and mc == sc:
            block[sr][sc] = True
            person.finish = True
            arrived += 1


while arrived != M:
    if minute > 0:
        move()  # 1, 2는 합쳐야 됨
    if minute < M:
        start(minute)
    minute += 1

print(minute)