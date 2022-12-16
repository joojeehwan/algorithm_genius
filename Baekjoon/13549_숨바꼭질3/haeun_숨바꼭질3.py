"""
다른 풀이
1. 다익스트라 (https://www.acmicpc.net/source/52633892)
 - 시간 초를 가중치로 두어 heapq를 활용한 풀이
2. deque (https://www.acmicpc.net/source/52633273)
 - deque에 시간을 포함하여 전개

"""


from collections import deque

MIN_VALUE = 0
MAX_VALUE = 100000

n, k = map(int, input().split())
visited = [0] * (MAX_VALUE + 1)
queue = deque([n])
visited[n] = 1

while not visited[k]:
    now_pos = queue.popleft()

    # 순간이동 먼저 처리
    teleport = now_pos * 2
    if MIN_VALUE <= teleport <= MAX_VALUE:
        if not visited[teleport] or visited[teleport] >= visited[now_pos]:
            visited[teleport] = visited[now_pos]
            queue.append(teleport)

    for x in [-1, 1]:
        new_pos = now_pos + x

        if MIN_VALUE <= new_pos <= MAX_VALUE and \
                not visited[new_pos]:
            visited[new_pos] = visited[now_pos] + 1
            queue.append(new_pos)

print(visited[k] - 1)
