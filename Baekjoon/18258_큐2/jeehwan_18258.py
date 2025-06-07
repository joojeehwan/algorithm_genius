'''

정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

<예제 입력>
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
'''
# 1. 리스트 풀이 > 시간 초과 (deque를 사용 해야 함)
import sys
N = int(sys.stdin.readline())
TO_DO = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
myQueue = []

def solve(to_do, lst):
    if to_do[0] == "push":
        lst.append(to_do[1])
        return

    elif to_do[0] == "front":
        if len(lst) == 0:
            print("-1")
        else:
            print(lst[0])
        return

    elif to_do[0] == "back":
        if len(lst) == 0:
            print("-1")
        else:
            print(lst[-1])
        return

    elif to_do[0] == "size":
        print(len(lst))
        return

    elif to_do[0] == "pop":
        if len(lst) == 0:
            print("-1")
        else:
            print(lst.pop(0))
        return

    elif to_do[0] == "empty":
        if len(lst) == 0:
            print("1")
        else:
            print("0")
        return

for to_do in TO_DO:
    debug = 1
    solve(to_do, myQueue)


#2 deque 풀이

from collections import deque

N = int(input())
TO_DO = [list(input().split()) for _ in range(N)]
myQueue = deque()

def solve(to_do, queue):
    cmd = to_do[0]

    if cmd == "push":
        queue.append(to_do[1])

    elif cmd == "pop":
        print(queue.popleft() if queue else "-1")

    elif cmd == "size":
        print(len(queue))

    elif cmd == "empty":
        print("0" if queue else "1")

    elif cmd == "front":
        print(queue[0] if queue else "-1")

    elif cmd == "back":
        print(queue[-1] if queue else "-1")

for to_do in TO_DO:
    solve(to_do, myQueue)