from collections import deque


def bfs():
    #큐 생성
    q = deque()
    #초깃값
    q.append((0, 0))
    #비짓 배열은 여기 있어야 한다.
    #bfs를 돌떄마다 초기화 하고 가야대
    visited = [[False] * M for _ in range(N)]

    cnt = 0

    while q:
        now_row, now_col = q.popleft()
        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #범위 생각
            if 0 <= next_row < N and 0 <= next_col < M:
                #가보지 않은 곳, 치즈가 없는 칸
                if MAP[next_row][next_col] == 0 and visited[next_row][next_col] == False:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col))

                elif MAP[next_row][next_col] == 1:
                    MAP[next_row][next_col] = 0
                    cnt += 1
                    visited[next_row][next_col] = True
    return cnt



N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


result = []
time = 0

while True:
    count = bfs()
    result.append(count)
    if count == 0:
        break
    time += 1

print(time)
print(result[-2])
