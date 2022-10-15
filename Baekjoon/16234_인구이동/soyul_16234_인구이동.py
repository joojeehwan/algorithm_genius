import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 연합할 국가를 구하는 함수(bfs로 구해줌)
def union(now_i, now_j, day):

    uni = []
    uni_sum = 0

    q = deque()
    q.append((now_i, now_j))
    visited[now_i][now_j] = day

    while q:
        now_i, now_j = q.popleft()
        uni.append((now_i, now_j))
        uni_sum += MAP[now_i][now_j]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N:
                continue
            if visited[next_i][next_j] == day:
                continue
            diff = abs(MAP[next_i][next_j] - MAP[now_i][now_j])
            if diff < L or diff > R:
                continue

            visited[next_i][next_j] = day
            q.append((next_i, next_j))

    return uni, uni_sum

# 인구를 이동시키는 함수
def move(uni, uni_sum):

    for i, j in uni:
        MAP[i][j] = uni_sum // len(uni)

day = 1
while 1:
    flag = 0                        # 인구이동할 게 남았는지 확인할 변수

    union_list = []                 # 연합을 저장하는 리스트
    visited = [[0] * N for _ in range(N)]                   # 방문 기록 저장(day변수 이용)
    # 다 돌아보면서 연합한 국가 구하기
    for i in range(N):
        for j in range(N):

            if visited[i][j] != day:
                uni, uni_sum = union(i, j, day)
                if len(uni) == 1:                                   # 연합할 국가가 하나밖에 없으면 pass
                    continue
                move(uni, uni_sum)
                flag = 1
    if not flag:
        break
    day += 1

print(day-1)