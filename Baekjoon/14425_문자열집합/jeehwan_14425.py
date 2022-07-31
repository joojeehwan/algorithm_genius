'''


문자열 집합

음 배열로 하니깐 시간 초과가 나네!

dict나 set으로 해야해!

그 이유는?!
https://ywtechit.tistory.com/30
여기가 설명 잘해놓음
'''


import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 집합으로 풀려면 이런식으로,,!
# 아래
# S = set([input().split() for _ in range(N)]

S = dict()

for _ in range(N):
    index = input()
    S[index] = True

ans = 0

for _ in range(M):
    target = input()
    if target in S.keys():
        ans += 1

print(ans)
