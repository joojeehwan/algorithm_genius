"""
76ms 나오길래 나도 68ms로 낮추고싶어서 찾아보던 도중 나랑 거의 유사한데 한 군데만 다른 코드를 찾음
https://www.acmicpc.net/source/43492120
내 코드의 문제점은 더 이상 방문할 건물이 없을 때 return을 하도록 해서
현재의 코드는 1군데만 있으면 바로 추가하고 돌아가는 것과 다르게 2번 더 들어가야 했다.
그래서 그걸 줄여주니까 68ms로 바뀌었다.
"""


K = int(input())
visited = list(map(int, input().split()))

tree = [[] for _ in range(K)]


def inorder(depth, buildings):
    if len(buildings) == 1:
        tree[depth].append(buildings.pop())
        return
    root_idx = len(buildings)//2
    tree[depth].append(buildings[root_idx])
    inorder(depth+1, buildings[:root_idx])
    inorder(depth+1, buildings[root_idx+1:])


inorder(0, visited)

for line in tree:
    print(*line)