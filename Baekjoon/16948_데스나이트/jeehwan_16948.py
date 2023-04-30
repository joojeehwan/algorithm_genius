from collections import deque


dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

N = int(input())

MAP = [[-1] * N for _ in range(N)] # -1로 초기화 해, 0과 구분

r1, c1, r2, c2 = map(int, input().split())

def bfs(start_row, start_col) :

    q = deque()
    q.append((start_row, start_col))
    MAP[start_row][start_col] = 0

    while q :

        now_row, now_col = q.popleft()

        for k in range(6):

            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            if 0 <= next_row < N and 0 <= next_col < N:

                if MAP[next_row][next_col] == -1 :

                    q.append((next_row, next_col))
                    MAP[next_row][next_col]  = MAP[now_row][now_col] + 1 #최단거리 판단의 POINT



bfs(r1, c1)

print(MAP[r2][c2])