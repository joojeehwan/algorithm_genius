from collections import deque

a, b = map(int, input().split())

# 배열은 이 지나치게 넓은 숫자 범위를 감당하지 못해서 메모리 초과가 남
# 딕셔너리로 관리하는 것이 이 문제의 관건
reach = {}
reach[a] = 0

q = deque([a])

# BFS
while q:
    now = q.popleft()
    mul = now * 2
    pad = 10 * now + 1

    # 두 배
    if mul <= b and (not reach.get(mul) or reach[mul] > reach[now] + 1):
        reach[mul] = reach[now] + 1
        q.append(mul)

    # 끝에 1 추가
    if pad <= b and (not reach.get(pad) or reach[pad] > reach[now] + 1):
        reach[pad] = reach[now] + 1
        q.append(pad)

print(reach[b] + 1 if reach.get(b) else -1)