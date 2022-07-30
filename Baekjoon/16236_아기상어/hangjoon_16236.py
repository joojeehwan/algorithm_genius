from collections import deque
import sys


size = int(sys.stdin.readline())  # 공간의 크기
field = [[] for _ in range(size)]   # 공간 상태
shark = ()  # 상어 위치
weight = 2  # 상어 크기
fishes = 0  # 물고기 수
for i in range(size):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(size):
        if data[j]:  # 물고기 or 상어
            if data[j] == 9:  # 상어
                shark = (i, j, 0)
            else:  # 물고기
                fishes += 1
    field[i] = data

# BFS
queue = deque()
queue.append((shark))
cnt = 0  # 먹은 물고기 수
ans = 0  # 소요 시간
visited = [[0 for _ in range(size)] for _ in range(size)]  # 방문 정보
visited[shark[0]][shark[1]] = 1
dish = []  # 먹을 물고기
while queue:
    now_r, now_c, dis = queue.popleft()
    for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:  # 북서남동
        new_r, new_c = now_r + dr, now_c + dc
        if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:  # 맵 밖임
            continue
        if visited[new_r][new_c]:  # 이미 방문한 곳
            continue
        if 0 < field[new_r][new_c] < 9:  # 가장 먼저 찾은 물고기가 가장 가까운 물고기
            if field[new_r][new_c] < weight:  # 먹을 수 있는 물고기
                if not dish:  # 처음 찾은 물고기
                    dish = [new_r, new_c, dis + 1]
                else:  # 먹을 물고기가 여러개
                    if new_r < dish[0]:  # 지금 물고기가 더 위에
                        dish = [new_r, new_c, dis + 1]
                    elif new_r > dish[0]:  # 이전 물고기가 더 위에
                        continue
                    else:  # 같은 열에
                        if new_c < dish[1]:  # 지금 물고기가 더 왼쪽에
                            dish = [new_r, new_c, dis + 1]
                        else:  # 이전 물고기가 더 왼쪽에
                            continue
            elif field[new_r][new_c] == weight:  # 크기가 같은 물고기
                queue.append((new_r, new_c, dis + 1))
                visited[new_r][new_c] = 1
        else:  # 빈 공간
            queue.append((new_r, new_c, dis + 1))
            visited[new_r][new_c] = 1
    if dish and (not queue or queue[0][2] >= dish[2]):  # 먹을 물고기 있음 and 같은 거리의 물고기 다 계산함
        queue = deque()  # 초기화
        # 상어 이동
        ans += dish[2]
        field[shark[0]][shark[1]] = 0
        shark = (dish[0], dish[1], 0)
        queue.append(shark)
        # 물고기 먹기
        field[shark[0]][shark[1]] = 0
        fishes -= 1
        cnt += 1
        dish = []
        if cnt == weight:  # 자기 무게만큼 먹으면 진화
            weight += 1
            cnt = 0
        # 방문 정보 초기화
        visited = [[0 for _ in range(size)] for _ in range(size)]
        visited[shark[0]][shark[1]] = 1
    if not fishes:  # 남은 물고기 없음
        break

print(ans)