import sys

# 기본적인 입력값 처리
N, M = map(int, sys.stdin.readline().split())
MAP = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))


# 도시의 치킨 거리 구하기
def city_chicken_distance(chicken_stores): # chicken_stores = [0, 1] 과 같이 가능한 치킨집의 index 배열
    # 이번 조합의 도시 치킨 거리
    sum_chicken_distance = 0
    # 사용할수 없는 컬럼을 제외한 거리를 담을 새로운 2차원 배열 생성
    available_distance = [[0] * M for _ in range(cnt_houses)]

    # 집 = row, 가능한 치킨집 = col
    for idx_house in range(cnt_houses):
        for idx_chicken in range(M):
            # 압축한 2차원 배열에 맞는 값을 넣는 과정
            available_distance[idx_house][idx_chicken] = distance[idx_house][chicken_stores[idx_chicken]]

    # 집을 기준으로 최소 거리만 구해서 더함
    for idx_house in range(cnt_houses):
        sum_chicken_distance += min(available_distance[idx_house])

    return sum_chicken_distance


# 살릴 치킨집 고르기. permutations 없이 풀어보고 싶었다. now는 조합 시작의 치킨집 index
def pick_chickens(now):
    # 최대 개수를 채웠다면, 조합에 현재 고른 가게들을 추가한다.(= 종료조건)
    if sum(visited) == M:
        picked = []
        for i in range(cnt_chickens):
            # 1개인데 끝까지 도는 꼴이 보기 싫어서
            if len(picked) == M:
                break
            if visited[i]:
                picked.append(i)
        # 고른 가게들을 조합에 추가한다.
        picked_store.append(picked)
        return

    # [0,1] 이 조합에 있다면 [1,0] 은 중복이므로 필요없다.
    # 고로 지금의 치킨집보다 뒤에 있는 치킨집이랑만 조합을 짜도 된다.
    for i in range(now+1, cnt_chickens):
        if visited[i]:
            pick_chickens(i)
        else:
            visited[i] = 1
            pick_chickens(i)
            # dfs 국룰
            visited[i] = 0

# 집과 치킨집의 위치를 배열로 저장한다. 둘 다 2차원 배열
houses = []
chickens = []

# 맵을 다 돌면서 1이면 집, 2면 치킨집
for row in range(N):
    for col in range(N):
        if MAP[row][col] == 1:
            houses.append([row, col])
        elif MAP[row][col] == 2:
            chickens.append([row, col])

# 집과 치킨집의 개수
cnt_houses, cnt_chickens = len(houses), len(chickens)

# 치킨집 * 집 개수 만큼 거리를 계산해서 넣을 2차원 배열
distance = [[0] * cnt_chickens for _ in range(cnt_houses)]

# 각 집과 치킨집의 거리를 계산한다.
for row in range(cnt_houses):
    for col in range(cnt_chickens):
        row_diff = abs(houses[row][0] - chickens[col][0])
        col_diff = abs(houses[row][1] - chickens[col][1])
        distance[row][col] = row_diff + col_diff

# 최소값을 찾을거고 N=50이고 집이 100채여도 987654321 까진 못 온다.
answer = 987654321

# 현재 있는 치킨 집의 개수와 M의 개수가 같다면 폐업시키지 않는다.
if cnt_chickens == M:
    # 모든 치킨집을 사용할 수 있으므로 치킨집 개수만큼의 index를 담은 배열 전달
    answer = city_chicken_distance([_ for _ in range(cnt_chickens)])
else:
    # 아니라면 살릴 치킨집 조합을 계산한다.
    # ex) picked_store = [[0,1], [0,2], [0,3] ... ]
    picked_store = []

    # 조합을 만들 때 사용하기 위한 방문 배열
    visited = [0] * cnt_chickens

    # 모든 치킨집을 한 곳 씩 돌면서 조합을 구한다.
    for idx_chicken in range(cnt_chickens):
        visited[idx_chicken] = 1
        pick_chickens(idx_chicken)
        # dfs 국룰
        visited[idx_chicken] = 0

    # 조합들을 담은 배열에서 하나의 조합씩 보면서 도시의 치킨 거리를 구한다.
    for store_set in picked_store:
        store_set_distance = city_chicken_distance(store_set)
        # 만약 지금까지 구한 것보다 짧은 거리라면 정답
        if store_set_distance < answer:
            answer = store_set_distance


print(answer)