from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
grid = list(list(map(int, input().split())) for _ in range(N))
answer = 0

# 상어의 초기값
shark_row, shark_col, shark_size = 0, 0, 2

# 물고기 크기별로 마리수를 저장한다.
fish_cnt = [0] * 7

for r in range(N):
    for c in range(N):
        value = grid[r][c]
        if value == 9:
            shark_row, shark_col = r, c
            grid[r][c] = 0
        elif 1 <= value <= 6:
            fish_cnt[value] += 1

# 상어의 기본 크기는 2이기 때문에,가장 처음엔 1 크기의 물고기만 먹을 수 있다.
edible_fish_cnt = fish_cnt[1]
eaten_fish_cnt = 0

while edible_fish_cnt:
    # 먹을 수 있는데 가장 가까운 물고기가 여러마리 있을 수 있다.
    near_fish = []
    # 가장 가까운 거리를 찾기 위해 일단 큰 값으로 설정
    near_dist = 987654321
    visited = [[0] * N for _ in range(N)]
    visited[shark_row][shark_col] = 1
    queue = deque([(shark_row, shark_col)])

    while queue:
        now_r, now_c = queue.popleft()

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            # 다음 위치까지의 거리
            dist = visited[now_r][now_c] + 1

            if 0 <= next_r < N and 0 <= next_c < N:
                # 최소거리를 구했는데 더 멀다면 필요 없다.
                if near_dist != 987654321 and near_dist < dist:
                    continue
                if visited[next_r][next_c]:
                    continue
                # 상어보다 같거나 크면 일단 지나갈 수 있다.
                if grid[next_r][next_c] <= shark_size:
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = dist
                    # 조건에 near_dist <= dist 에 등호가 있는 이유는, 최단 거리에 있는 물고기가 여러마리일 수 있으니까
                    if 0 < grid[next_r][next_c] < shark_size and dist <= near_dist:
                        near_dist = dist
                        near_fish.append((next_r, next_c))

    # 먹을 수 있는 물고기가 있다면
    if near_fish:
        near_fish.sort(key=lambda x: (x[0], x[1]))

        # 물고기 먹음
        shark_row, shark_col = near_fish[0]  # 상어 위치 옮기고
        grid[shark_row][shark_col] = 0  # 해당 위치에 아무것도 없고
        eaten_fish_cnt += 1  # 먹은 개수 추가하고
        answer += visited[shark_row][shark_col] - 1  # 걸린 시간 더하고
        fish_cnt[grid[shark_row][shark_col]] -= 1  # 해당 크기의 물고기 수 줄이고
        edible_fish_cnt -= 1  # 먹을 수 있는 물고기의 수 줄이고

        if shark_size == eaten_fish_cnt:
            eaten_fish_cnt = 0
            shark_size += 1
            fish_max_size = shark_size
            if shark_size < 7:
                fish_max_size = 6
            edible_fish_cnt = sum(fish_cnt[:fish_max_size])
    else:
        break



print(answer)