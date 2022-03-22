import sys

def dfs(now, run):
    global ans

    if len(run) >= m:       # 치킨집 조합을 다 만들면 계산
        sum_dis = 0
        for i in range(len(house)):
            min_dis = []
            for j in range(m):
                min_dis.append(abs(run[j][0] - house[i][0]) + abs(run[j][1] - house[i][1]))
            sum_dis += min(min_dis)

        ans.append(sum_dis)
        return

    # 치킨집의 조합을 만들어줌
    for i in range(now, len(chicken)):
        dfs(i + 1, run + [chicken[i]])

n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 치킨집과 집의 좌표들을 모두 저장
house = []
chicken =[]
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1:
            house.append((i, j))
        elif MAP[i][j] == 2:
            chicken.append((i, j))

ans = []
dfs(0, [])

print(min(ans))