'''

비트 마스킹

두 가지의 풀이가 존재


1. 비트 마스크


2. 집합 풀이

'''


#비트 마스크 풀이
# 참고 https://vitriol95.github.io/posts/set_bitmask/
# s의 범위가  1 <= s <= 20 인것을 활용해, 비트 마스킹으로 풀이, 단순히 값이 있고 없음을
# 리스트에 표현하는 것이 아니라, bit를 통해서 표현

import sys
m = int(sys.stdin.readline())
S = 0b0
all_S = 0b111111111111111111111
not_S = 0b000000000000000000000

for i in range(m):
    cmd = sys.stdin.readline().rstrip().split(" ")
    if cmd[0] == "add":
        S = S | (1 << int(cmd[-1]))
    elif cmd[0] == "remove":
        S = S & ~(1 << int(cmd[-1]))
    elif cmd[0] == "check":
        if S & (1 << int(cmd[-1])):
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        S = S ^ (1 << int(cmd[-1]))

    elif cmd[0] == "all":
        S = S | all_S
    else:
        S = S & not_S



# https://yoonsang-it.tistory.com/38 참고
# 집합 풀이

import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)