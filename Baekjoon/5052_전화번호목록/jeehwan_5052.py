'''

트라이 관련해서, 공부하기 (Trie)

문자열 관련한 알고리즘 중에 하나, 그러나, 굳이 트라이를 사용하지 않고도, 문제 풀이가 가능


'''


t = int(input())

def check():
    for i in range(len(a)-1):
        # a 값의 원소가 문자열이기 때문에 [][] 이렇게 사용이 가능해지는 것
        if a[i] == a[i+1][0:len(a[i])]:
            print('NO')
            return
    print('YES')

for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        # 문자열로 입력받기
        a.append(input().strip())
    a.sort()
    check()


#start_with을 활용한 풀이
import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    numbers = sorted([input().rstrip() for _ in range(n)])

    res = True
    for i in range(n - 1):
        if (numbers[i + 1].startswith(numbers[i])):
            res = False
            break

    print("YES" if res else "NO")


t = int(input())
for _ in range(t):
    solution()


#trie를 활용한 풀이

'''

Node를 Class로 만들기
- Key에는 해당 노드의 문자가 들어가고, Child에는 자식 노드가 포함되게 된다.
- Data는 문자열이 끝나는 위치를 알려주는 역할을 한다. 
  예를 들어서 “car”이 “r”에서 끝날 때, “r”을 key로 가지는 노드의 data에 “car”를 입력한다.
  해당 노드에서 끝나는 문자열이 없을 경우에는 None으로 그대로 놔둔다.

'''


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)
  # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        #문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string
    # 문자열이 존재하는지 search
    def search(self, string):
        #가장 아래에 있는 노드에서 부터 탐색 시작
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        #탐색이 끝난 후 해당 노드의 data값이 존재한다면
        #문자가 포함되어있다는 뜻이다.
        if curr_node.data != None:
            return True

T = int(input())

for _ in range(t):

    n = int(input())
    trie = Trie()
    nums = []
    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)


    flag = True
    nums.sort()
    for num in nums:
        if not trie.search(num):
            flag = False
            break

    if flag:
        print("YES")

    else:
        print("NO")