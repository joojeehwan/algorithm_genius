def pre_order(x):
    if x == '.':
        return

    print(x, end='')
    pre_order(tree[x][0])
    pre_order(tree[x][1])

def in_order(x):
    if x == '.':
        return

    in_order(tree[x][0])
    print(x, end='')
    in_order(tree[x][1])

def post_order(x):
    if x == '.':
        return

    post_order(tree[x][0])
    post_order(tree[x][1])
    print(x, end='')

n = int(input())
tree = {}
for _ in range(n):
    a, b, c = input().split()

    tree[a] = [b, c]

pre_order('A')
print()
in_order('A')
print()
post_order('A')