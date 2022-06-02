'''

트리 순회


특이한 입력 -> 이진 트리용으로 받아보자!

흠흠,, 딕셔너리 쓰면 훨씬 편하다! 부모와 자식을 연결하는 부분에서!



'''


#전위순회

def preorder(root): #root -> left -> right

    if root != ".":
        print(root, end="")
        preorder(tree)



N = int(input())

#딕셔너리
tree = {}

#입력받기!
for i in range(N):

    root, left, right = input().split()
    tree[root] = [left, right]