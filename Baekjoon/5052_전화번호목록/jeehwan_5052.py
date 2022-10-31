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