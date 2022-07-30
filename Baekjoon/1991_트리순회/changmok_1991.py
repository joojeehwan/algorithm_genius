from sys import stdin

def dfs(node):
    global pre, mid, post
    pre += node
    if tree[node][0] != '.':
        dfs(tree[node][0])
    mid += node
    if tree[node][1] != '.':
        dfs(tree[node][1])
    post += node

n = int(stdin.readline())

tree = dict()

for _ in range(n):
    p, c1, c2 = stdin.readline().split()
    tree[p] = [c1, c2]

pre = ''
mid = ''
post = ''

dfs('A')

print(pre)
print(mid)
print(post)