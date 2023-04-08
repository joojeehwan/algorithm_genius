"""
sys 안쓰면 4044ms
sys 쓰면 140ms
"""
import sys

N, M = map(int, sys.stdin.readline().split())
unknowns = dict()
answer = list()

for _ in range(N+M): # 예전에는 N, M을 따로 받았는데 말야.. 사실 그럴 필요는 없었던거야
    unknown = sys.stdin.readline().rstrip()
    if unknowns.get(unknown):
        answer.append(unknown)
    else:
        unknowns[unknown] = 1

answer.sort()

print(len(answer))
for person in answer:
    print(person)