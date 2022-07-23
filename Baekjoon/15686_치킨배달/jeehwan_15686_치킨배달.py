
#문제에선 내가 생각하는 row, col을 바꾸어서 말한다.
# 그치만 문제되지 않는다. 내가 정한 좌표로 생각하고 문제를 이해하고 풀자.



# 가장 최소가 되는 치킨 거리를 구한다.
def calc_distance(dist):
    #가장 가까운 치킨집의 거리를 더하는거라서!
    for i in range(len(houses)):
        row1, col1 = houses[i]
        for j in range(len(visited)):
            if  visited[j]:
                row2, col2 = chickens[j]
                distnce = abs(row1-row2) + abs(col1-col2)
                dist[i] = min(distnce,  dist[i])
    return sum(dist)

def dfs(start,lev, max_len):

    global ans
    #전체 치킨의 조합 중에서 m개에 해당하는 중복 x 뽑기

    if lev == max_len:
        dist = [987654321 for _ in range(len(houses))]
        ans = min(calc_distance(dist), ans)
        return
                #집과 거리 계산

    #중복이 되지 않게! => start 출발! 1부터 출발하지 않음
    for i in range(start, len(chickens)):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, lev + 1, max_len)
            visited[i] = False

N, M = map(int, input().split())
MAP = []
chickens = []
houses = []
for i in range(N):
    row = list(map(int, input().split()))
    MAP.append(row)
    for j in range(N):
        if MAP[i][j] == 1:
            houses.append([i,j])
        if MAP[i][j] == 2:
            chickens.append([i,j])

visited = [False for _ in range(len(chickens))]
ans = 987654321
for r in range(M):
    dfs(0, 0, r+1)
print(ans)


# from sys import stdin
# from math import inf
#
#
# def manhattan_dist(h, c):
#     return abs(h[X] - c[X]) + abs(h[Y] - c[Y])
#
#
# def dfs(idx, selected):
#     global answer
#
#     if idx > len(chicken):
#         return
#
#     if selected == m:
#         sum_distance = 0
#         for house in houses:
#             min_distance = inf
#             for c_idx, value in enumerate(chicken):
#                 if not check[c_idx]:
#                     continue
#                 min_distance = min(min_distance, manhattan_dist(house, value))
#             sum_distance += min_distance
#         answer = min(answer, sum_distance)
#         return
#
#     check[idx] = True
#     dfs(idx + 1, selected + 1)
#     check[idx] = False
#     dfs(idx + 1, selected)
#
#
# if __name__ == '__main__':
#     X, Y = 0, 1
#     n, m = map(int, stdin.readline().split())
#     graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
#     houses, chicken = [], []
#     answer = inf
#
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 1:
#                 houses.append([i + 1, j + 1])
#             elif graph[i][j] == 2:
#                 chicken.append([i + 1, j + 1])
#
#     check = [False] * (len(chicken) + 1)
#     dfs(0, 0)
#     print(answer)
#
#  이 풀이와 차이가 뭐지,,?!!?
#
# '''
