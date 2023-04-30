'''

이진트리

파이선 클래스

https://rebro.kr/133
https://wikidocs.net/28

'''
from collections import deque
import sys

#이진트리 순회 예시
class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def preorder(self):
        def _preorder(node):
            print(node.item, end=' ')
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)

        _preorder(self.root)

    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.item, end=' ')
            if node.right:
                _inorder(node.right)

        _inorder(self.root)

    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.item, end=' ')

        _postorder(self.root)

    def levelorder(self):
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.item, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


BT = BinaryTree()
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N7 = Node(7)
N8 = Node(8)

BT.root = N1
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7
N4.left = N8

print('preorder')
BT.preorder()

print('\ninorder')
BT.inorder()

print('\npostorder')
BT.postorder()

print('\nlevelorder')
BT.levelorder()

print('preorder')
BT.preorder()

print('\ninorder')
BT.inorder()

print('\npostorder')
BT.postorder()

print('\nlevelorder')
BT.levelorder()


#문제풀이1
import sys


class Node:
    def __init__(self, x, y, num):
        self.num = num
        self.x = x
        self.y = y
        self.left = None
        self.right = None


def pre(node, pre_lst):
    if node == None:
        return

    pre_lst.append(node.num)
    pre(node.left, pre_lst)
    pre(node.right, pre_lst)


def post(node, post_lst):
    if node == None:
        return

    post(node.left, post_lst)
    post(node.right, post_lst)
    post_lst.append(node.num)


def solution(nodeinfo):
    sys.setrecursionlimit(10 ** 6)

    for i, node in enumerate(nodeinfo):
        node.reverse()
        node.append(i + 1)

    nodeinfo.sort()
    nodeinfo.reverse()

    # 노드들관의 관계 설정 하는 부분 => 누가 왼쪽?! 오른쪽?!
    head = None
    for n_info in nodeinfo:
        node = Node(n_info[1], n_info[0], n_info[2])

        if head == None:
            head = node
            continue

        current = head

        while (True):

            # 지금보고 있는 노드보다 왼쪽에 있는 노드들
            if current.x > node.x:

                # 왼쪽에 있는 노드 기록
                if current.left == None:
                    current.left = node
                    break
                # 이미 기록이 되어 있으면, 그 기록 따라 할당(이동)
                else:
                    current = current.left
            # 지금 보고 있는 노드보다 오른쪽에 있는 노드들
            else:

                if current.right == None:
                    current.right = node
                    break
                else:
                    current = current.right
    pre_lst = []
    post_lst = []
    pre(head, pre_lst)
    post(head, post_lst)

    answer = [pre_lst, post_lst]
    return answer

#다른 풀이 2
import sys

sys.setrecursionlimit(10 ** 6)


# 전위 순회

def preorder(lstY, lstX, answer):
    # 맨위 노드 => 시작 노드
    node = lstY[0]
    # 시작 노드가, 왼쪽에서 몇번쨰 위치 하는가?
    idx = lstX.index(node)
    left = []
    right = []

    # 현재 보고 있는 노드 기준, 왼쪽 / 오른쪽 노드 정리
    for i in range(1, len(lstY)):
        # 현재 보고 있는 노드의 x좌표보다 i번쨰 노드의 x좌표보다 작으면(더 왼쪽에 있으면)
        if node[0] > lstY[i][0]:
            # left에 넣고,
            left.append(lstY[i])
            # 그게 아니면, right에 넣는다.
        else:
            right.append(lstY[i])

    # 노드번호 answer 배열에 넣기
    answer.append(node[2])

    # 재귀를 통한 전위순회 => 현재 보고 있는 노드 기준 왼쪽/오른쪽
    if len(left) > 0:
        preorder(left, lstX[:idx], answer)

    if len(right) > 0:
        preorder(right, lstX[idx + 1:], answer)

    return


# 후위 순회
def postorder(lstY, lstX, answer):
    # 맨위 노드 => 시작 노드
    node = lstY[0]
    # 시작 노드가, 왼쪽에서 몇번쨰 위치 하는가?
    idx = lstX.index(node)
    left = []
    right = []

    # 현재 보고 있는 노드 기준, 왼쪽 / 오른쪽 노드 정리
    for i in range(1, len(lstY)):
        # 현재 보고 있는 노드의 x좌표보다 i번쨰 노드의 x좌표보다 작으면(더 왼쪽에 있으면)
        if node[0] > lstY[i][0]:
            # left에 넣고,
            left.append(lstY[i])
            # 그게 아니면, right에 넣는다.
        else:
            right.append(lstY[i])

    # 재귀를 통한 전위순회 => 현재 보고 있는 노드 기준 왼쪽/오른쪽
    if len(left) > 0:
        postorder(left, lstX[:idx], answer)

    if len(right) > 0:
        postorder(right, lstX[idx + 1:], answer)

    answer.append(node[2])

    return


def solution(nodeinfo):
    preLst = []
    postLst = []

    # 문제의 제한사항에 적혀 있음.
    # "nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다."
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    # Y이 가장 클 수록, x값이 작을 수록 => 즉 맨위 / 왼쪽 노드 순으로 정렬
    arrY = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    # x값이 작을 수록 => 즉 맨왼쪽부터 오른쪽으로 정렬
    arrX = sorted(nodeinfo)
    # print(arrY)
    # print()
    # print(arrX)
    # print()
    preorder(arrY, arrX, preLst)
    postorder(arrY, arrX, postLst)
    # print(preLst)
    # print(postLst)
    answer = [preLst, postLst]
    return answer