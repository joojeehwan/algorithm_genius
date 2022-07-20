import sys

N, M = map(int, sys.stdin.readline().split())

# 집합 S를 만든다
S = set()
for _ in range(N):
    S.add(sys.stdin.readline().rstrip())

# 문자열을 받으면서 집합 S에 들어있는지 검사한다
cnt = 0
for _ in range(M):
    word = sys.stdin.readline().rstrip()

    if word in S:
        cnt += 1

print(cnt)


"""
S가
list 일 때 3764ms
dict 일 때 148ms
set 일 때 148ms
"""