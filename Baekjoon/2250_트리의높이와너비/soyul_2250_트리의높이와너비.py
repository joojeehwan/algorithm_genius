import sys

n = int(sys.stdin.readline())
parent = [-1] * (n+1)
tree = {}
for _ in range(n):
    z, x, y = map(int, sys.stdin.readline().split())
    tree[z] = [x, y]
    if x != -1:
        parent[x] = z
    if y != -1:
        parent[y] = z

"""
중위순회를 돌면서 각 층과, 인덱스를 기록해줌
"""
# 중위순회
def in_order(x, floor):
    global cnt

    if x == -1:
        return

    in_order(tree[x][0], floor + 1)
    index[floor].append(cnt)
    cnt += 1
    in_order(tree[x][1], floor + 1)

# 루트 노드 찾기
root = 0
for i in range(n+1):
    if parent[i] == -1:
        root = i

index = [[] for _ in range(n+1)]
cnt = 0

in_order(root, 0)

ans_idx = 0
ans_width = 0
for i in range(1, n):
    if len(index[i]) <= 1:
        continue

    if index[i][-1] - index[i][0] + 1 > ans_width:
        ans_width = index[i][-1] - index[i][0] + 1
        ans_idx = i


print(ans_idx + 1, ans_width)