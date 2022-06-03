'''

트리 순회


특이한 입력 -> 이진 트리용으로 받아보자!

흠흠,, 딕셔너리 쓰면 훨씬 편하다! 부모와 자식을 연결하는 부분에서!



'''


#전위순회

def preorder(root): #root -> left -> right

    if root != ".":
        print(root, end="") #루트
        preorder(tree[root][0]) #왼쪽
        preorder(tree[root][1]) #오른쪾

#중위 순회
def inorder(root): #left -> root -> right

    if root != ".":

        inorder(tree[root][0]) #왼
        print(root, end="") #루트
        inorder(tree[root][1]) #오

#후위 순회

def postorder(root): #reft -> right -> root

    if root != ".":

        postorder(tree[root][0]) #왼
        postorder(tree[root][1]) #오
        print(root, end="")



N = int(input())

#딕셔너리
tree = {}

#입력받기!
for i in range(N):

    root, left, right = input().split()
    tree[root] = [left, right]

# print(tree)

#"A에서 시작
preorder('A')
print()
inorder('A')
print()
postorder('A')