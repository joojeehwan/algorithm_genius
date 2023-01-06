'''

트리의 지름이란,

트리에서 임의의 두 점 사이의 거리 중 가장 긴 것


=> 임의의 한 점에서 dfs / bfs 알고리즘을 사용하여 각 노드까지의 거리를 구하고,

이 중 최대 거리를 갖는 노드에서 시작하여, 다시 한번 각 노드까지의 최대 거리를 구한다면?!

그 최대 거리가 바로 트리의 지름이 된다.




입력


5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1

'''

# 초기 입력 값 정리

n = int(input())

MAP = [[] for _ in range(n + 1)]

visited = [-1] * (n + 1)  # 탐색 여부와, 간선의 거리 저장

visited[1] = 0
for _ in range(n):

    temp = list(map(int, input().split()))

    for i in range(1, len(temp) - 1, 2):
        MAP[temp[0]].append([temp[i], temp[i + 1]])

    # i = 1
    # while i != len(temp) - 1:
    #     MAP[temp[0]].append([temp[i], temp[i+1]])
    #     i += 2


# print(MAP)


# 1. dfs 풀이

def dfs(start_node, distance):
    for node, value in MAP[start_node]:

        if visited[node] == -1:
            visited[node] = value + distance
            dfs(node, value + distance)


dfs(1, 0)

start = visited.index(max(visited))  # 1번 노드에서 가장 먼 노드를 찾는다.

# print(start)

visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))

# 2. bfs 풀이