"""
def solution(numbers, target):

    answer = 0

    q = []
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    while q:
        now, idx = q.pop(0)
        if idx == len(numbers)-1:
            q.append((now, idx))
            break

        q.append((now + numbers[idx+1], idx+1))
        q.append((now - numbers[idx+1], idx+1))

    for num in q:
        if num[0] == target:
            answer += 1

    return answer

# 시간초과 ...
"""

answer = 0

def dfs(idx, now, numbers, target):
    global answer

    if idx == len(numbers):         # 끝까지 계산하면 target이 맞는지 확인 후 카운트
        if now == target:
            answer += 1
        return

    # -1, +1 을 곱한 값을 더해주면서 dfs
    for i in range(2):
        dfs(idx + 1, now + numbers[idx] * ((-1) ** i), numbers, target)

    return answer

def solution(numbers, target):

    dfs(0, 0, numbers, target)
    return answer