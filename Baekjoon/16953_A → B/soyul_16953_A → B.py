a, b = map(int, input().split())

q = []
q.append((a, 1))        # 계산 카운트와 숫자를 함께 넣어줌
result = -1

while q:
    now, cnt = q.pop(0)
    # 원하는 수에 도달하면
    if now == b:
        result = cnt
        break

    # 2배 한 수와 1을 붙인 수를 넣어줌
    for k in range(2):
        if k == 0:
            next = now * 2
        if k == 1:
            next = now * 10 + 1

        if next > b:
            continue

        q.append((next, cnt + 1))

print(result)