from itertools import combinations

n, m = map(int, input().split())
city = [list(input().split()) for _ in range(n)]

chicken = []
house = []

# 치킨집과 가정집을 구분해서 리스트에 좌표 저장
for r in range(n):
    for c in range(n):
        if city[r][c] == '1':
            house.append((r, c))
        if city[r][c] == '2':
            chicken.append((r, c))

# m개의 치킨집만 남기는 모든 조합
chickencomb = combinations(chicken, m)

mindistance = int(1e9)

# 매 치킨집 조합에 따라
for chickenleft in chickencomb:
    chickendistance = 0
    # 각 가정에서의 치킨 거리를 계산
    for (hr, hc) in house:
        dist = int(1e9)
        for (cr, cc) in chickenleft:
            dist = min(dist, abs(hr - cr) + abs(hc - cc))
        chickendistance += dist
        # 계산 도중 이미 구한 최소값보다 커지면 계산을 멈춤
        if chickendistance >= mindistance:
            chickendistance = int(1e9)
            break
    
    mindistance = min(mindistance, chickendistance)

print(mindistance)