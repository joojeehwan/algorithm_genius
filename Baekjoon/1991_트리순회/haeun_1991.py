"""
문자열을 숫자로 바꿔서 list로 하나
딕셔너리로 하나 시간 차이는 없다.
그냥 코드 가독성이 더 좋은 것 같아서 바꿨다.

쉬운건데.. 오히려 쉬워서 못 풀었다.
막 find_left 함수 만들고 난리 피우고 있었다ㅎㅎ;;
쉬운 문제를 빨리 풀어야 한다고 하는데 난 한참 멀었나보다.
"""


N = int(input())

tree = {}


def preorder(now):
    if now != '.':
        print(now, end="")
        preorder(tree[now][0]) # 왼쪽
        preorder(tree[now][1]) # 오른쪽


def inorder(now):
    if now != '.':
        inorder(tree[now][0])
        print(now, end="")
        inorder(tree[now][1])


def postorder(now):
    if now != '.':
        postorder(tree[now][0])
        postorder(tree[now][1])
        print(now, end="")


for _ in range(N):
    parent_node, left_node, right_node = input().split()
    tree[parent_node] = [left_node, right_node]


preorder('A')
print()
inorder('A')
print()
postorder('A')
