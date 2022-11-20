'''


이진 트리의 순회 먼저 다시 리마인드


그림에 주어진 행과 열이

행 : 그 노드의 깊이

열 : 중위순회의 순서를 나타냄

ex) 5번 노드는 그림에서 3행 8열에 존재하는데,  => 노드 깊이가 3, 8번째 순서

8 - 4 - 2 - 14 - 9 - 18 - 15 - 5 - 10 - 1 - 16 - 11 - 6 - 12 - 3 - 19 - 17 - 13 - 7



'''

'''

입력력


7 
A B C
B D .
C E F
E . .
F . G
D . . 
G . .

'''

import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

#전위 순회 //루트-왼-오
def pre_order(node):
    print(node.data, end='')
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

#중위 순회 // 왼-루트-오
def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != None:
        in_order(tree[node.right])

#후위 순회 // 왼-오-루트
def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end='')

N = int(sys.stdin.readline().rstrip())
tree = {}

for i in range(N):
    data, left, right = sys.stdin.readline().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

#풀이 1

N = int(input())
graph = [[] for _ in range(N + 1)] # 그래프를 이차원배열
isRoot = [0] * (N + 1)
distance = [[] for _ in range(N + 1)] #거리 값을 저장
root = 0

for _ in range(N):
    parent, left, right = map(int, input().split())
    graph[parent].append(left)
    graph[parent].append(right)
    isRoot[parent] += 1
    if left != -1:
        isRoot[left] += 1

    if right != -1:
        isRoot[right] += 1

for i in range(1, N + 1): # 제일 꼭대기 루트는 1의 값만 갖는다.
    if isRoot[i] == 1:
        root = i

num = 1

#중위 순회 구현
def inOrder(start, lev):

    global num
    #왼쪽이 있어?!
    if graph[start][0] != -1:
        inOrder(graph[start][0], lev + 1)
    #현재 레벨에 이 위치에 노드가 있음을 표시
    distance[lev].append(num)
    num += 1
    #오른쪽이 있어?!
    if graph[start][1] != -1:
        inOrder(graph[start][1], lev + 1)



inOrder(root, 1)
level = 1
#첫번 째 레벨을 값으로
ans = 1
for i in range(1, N + 1):
    if distance[i]:
        small = min(distance[i])
        big = max(distance[i])
        if ans < big - small + 1:
            ans = big - small + 1
            level = i

print(level)
print(ans)
#다른 풀이 이렇게도 푸는 군


# import sys
#
# sys.setrecursionlimit(1000000)
#
#
# class node:
#     def __init__(self):
#         self.left = -1
#         self.right = -1
#         self.depth = 0
#         self.order = 0
#
#
# def inorder(node, depth):
#     global order
#     if node == -1:
#         return
#     inorder(a[node].left, depth + 1)
#     a[node].depth = depth
#     order += 1
#     a[node].order = order
#     inorder(a[node].right, depth + 1)
#
#
# n = int(sys.stdin.readline())
# a = [node() for _ in range(10001)]
# left = [0] * 10001
# right = [0] * 10001
# parent = [0] * 10001
# order = 0
#
# for i in range(n):
#     x, b, c = map(int, sys.stdin.readline().split())
#     a[x].left = b
#     a[x].right = c
#     if b != -1:
#         parent[b] += 1
#     if c != -1:
#         parent[c] += 1
#
# root = 0
# for i in range(1, n + 1):
#     if parent[i] == 0:
#         root = i
#
# inorder(root, 1)
# maxdepth = 0
# for i in range(1, n + 1):
#     depth = a[i].depth
#     order = a[i].order
#     if left[depth] == 0:
#         left[depth] = order
#     else:
#         left[depth] = min(left[depth], order)
#     right[depth] = max(right[depth], order)
#     maxdepth = max(maxdepth, depth)
#
# maxwidth = 0
# anslevel = 0
#
# for i in range(1, maxdepth + 1):
#     if maxwidth < right[i] - left[i] + 1:
#         maxwidth = right[i] - left[i] + 1
#         anslevel = i
#
# sys.stdout.write("{} {}".format(anslevel, maxwidth))